from fastapi import FastAPI
import happybase
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

connection = happybase.Connection('localhost')
connection.open()

class User(BaseModel):
    username: str
    email: str

class Chatroom(BaseModel):
    room_name: str

class Chat(BaseModel):
    user_id: str
    room_id: str
    message: str

# @app.get("/")       # => urls.py
# def read_root():    # => views.py
#     return {"Hello": "World"}

# @app.get('/item/{item_id}')
# def read_item(item_id: int):
#     return {'item_id': item_id}

@app.post('/user')
def create_user(user: User):
    table = connection.table('user')
    user_id = user.username
    table.put(
        user_id.encode('utf-8'),  # user_id를 바이트로 인코딩
        {
            b'info:username': user.username.encode('utf-8'),  # 키와 값을 바이트로 인코딩
            b'info:email': user.email.encode('utf-8'),  # 키와 값을 바이트로 인코딩
        }
    )
    return {
        'user_id': user_id,
        'username': user.username,
        'email': user.email
    }

@app.get('/user/{user_id}')
def get_user(user_id: str):
    table = connection.table('user')
    row = table.row(user_id.encode('utf-8'))  # user_id를 바이트로 인코딩

    return {
        'user_id': user_id,
        'username': row[b'info:username'].decode('utf-8'),  # 값을 디코딩
        'email': row[b'info:email'].decode('utf-8')  # 값을 디코딩
    }

@app.post('/chatroom')
def create_chatroom(chatroom: Chatroom):
    table = connection.table('chatroom')
    chatroom_id = chatroom.room_name
    table.put(chatroom_id, {'info:room_name': chatroom.room_name})
    return {'chatroom_id': chatroom_id, 'room_name':chatroom.room_name}

@app.post('/chat')
def create_chat(chat: Chat):
    table = connection.table('chat')
    timestamp = datetime.now().timestamp()
    MAX_TIMESTAMP = 2**64 - 1

    chat_id = f'{chat.room_id}_{int(MAX_TIMESTAMP - timestamp)}'
    table.put(
        chat_id.encode('utf-8'),  # chat_id를 바이트로 인코딩
        {
            b'info:user_id': chat.user_id.encode('utf-8'),  # 키와 값을 바이트로 인코딩
            b'info:room_id': chat.room_id.encode('utf-8'),  # 키와 값을 바이트로 인코딩
            b'info:message': chat.message.encode('utf-8')  # 키와 값을 바이트로 인코딩
        }
    )

    return {
        'chat_id': chat_id,
        'user_id': chat.user_id,
        'room_id': chat.room_id,
        'message': chat.message
    }

@app.get('/chatroom/{room_id}')
def get_chatroom(room_id: str):
    table = connection.table('chat')

    rows = table.scan(filter=f"SingleColumnValueFilter('info', 'room_id', =, 'binary:{room_id}')")

    chats = []

    for k, v in rows:
        chats.append(
            {
                'chat_id': k,
                'room_id': v[b'info:room_id'],
                'user_id': v[b'info:user_id'],
                'message': v[b'info:message']
            }
        )

    return chats
- install

```
pip3 install fastapi
pip3 install uvicorn

pip3 install happybase
```

- `main.py`
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

- thrift start
```
$HBASE_HOME/bin/hbase thrift start
```

- run server
```
uvicorn main:app --reload
```
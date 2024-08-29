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

## HBase 개념

### 1. **HBase란?**

HBase는 **Hadoop Distributed File System(HDFS)** 위에 구축된 **컬럼 기반 분산 NoSQL 데이터베이스**입니다. HBase는 대규모의 비정형 데이터를 처리할 수 있도록 설계된 시스템으로, 특히 **실시간으로 대량의 데이터를 읽고 쓰는** 작업에 최적화되어 있습니다. HBase는 Google의 Bigtable을 모델로 삼아 개발되었으며, 주로 **수평 확장성**과 **고가용성**을 강조합니다.

### 2. **HBase의 데이터 구조**

HBase의 데이터 모델은 전통적인 관계형 데이터베이스(RDBMS)와는 다릅니다. HBase는 데이터를 **Row Key**, **Column Family**, **Column Qualifier**, 그리고 **Timestamp**로 구성된 테이블에 저장합니다. 이를 통해 복잡한 데이터 구조를 유연하게 다룰 수 있습니다.

- **Row Key**: 각 데이터 행(Row)은 Row Key에 의해 고유하게 식별됩니다. Row Key는 사전순으로 정렬되며, 효율적인 조회를 위해 설계됩니다. 예를 들어, 사용자 로그를 저장하는 경우, 사용자 ID를 Row Key로 사용할 수 있습니다.
- **Column Family**: HBase 테이블은 여러 Column Family로 나뉩니다. Column Family는 데이터를 물리적으로 분리하여 저장하는 단위로, 각 Column Family는 HDFS 상의 별도 파일로 관리됩니다. 예를 들어, 사용자 데이터베이스에서는 `personal_info`와 `activity_log`와 같은 Column Family를 둘 수 있습니다.
- **Column Qualifier**: Column Family 내의 컬럼들을 구분하는 역할을 합니다. 예를 들어, `personal_info`라는 Column Family 내에는 `name`, `email`, `phone` 등의 Column Qualifier가 있을 수 있습니다.
- **Timestamp**: HBase는 데이터의 버전을 관리하기 위해 Timestamp를 사용합니다. 동일한 Row와 Column에 대해 여러 버전의 데이터를 저장할 수 있으며, 기본적으로 최신 버전이 반환됩니다. 이를 통해, 데이터의 변경 이력이나 타임 시리즈 데이터를 효과적으로 관리할 수 있습니다.
    

### 3. **HBase와 RDBMS의 차이점**

HBase는 전통적인 RDBMS와 본질적으로 다릅니다.

- **스키마 유연성**: RDBMS는 고정된 스키마를 필요로 하지만, HBase는 스키마가 유연합니다. 이는 데이터 구조가 자주 변하거나, 컬럼의 수가 동적으로 증가하는 상황에서 큰 이점을 제공합니다.
- **확장성**: RDBMS는 주로 수직 확장(Scale-Up)을 통해 성능을 향상시키는 반면, HBase는 수평 확장(Scale-Out)을 통해 성능과 저장 용량을 확장합니다. 새로운 서버(Region Server)를 추가하면 HBase 클러스터 전체의 처리 능력이 증가합니다.
- **데이터 모델링**: RDBMS는 정규화된 테이블 구조를 사용하여 데이터를 관리하지만, HBase는 비정형 데이터나 반정형 데이터에 더 적합한 컬럼 패밀리 구조를 사용합니다. 이로 인해 HBase는 복잡한 데이터 모델링 없이도 대규모 데이터를 효과적으로 관리할 수 있습니다.

### 4. **HBase의 활용 사례**

- 채팅: 카카오톡과 같은 메시징 시스템에서 HBase를 사용하여 각 채팅방에서 누적되는 채팅을 개별 리전서버로 관리하여 각 사용자들이 충돌없이 사용할 수 있으며, 이러한 활동을 실시간으로 추적하고 저장할 수 있다.
- **검색 엔진**: HBase는 네이버, 구글, 다음과 같은 검색 엔진에서 웹 페이지 정보를 크롤링하고 인덱싱하는 데 사용됩니다. 이러한 시스템에서는 각 페이지의 수많은 속성을 빠르고 효율적으로 수집 및 관리해야 하기에 HBase를 통해 각 리전 서버를 두고 데이터를 분산되어 수집할 수 있다.

### 📚 오늘 배운 것 (TIL)

오늘은 HBase의 개념과 구조에 대해 깊이 있게 배웠다. HBase는 대규모 데이터 처리에 적합한 **컬럼 기반 분산 NoSQL 데이터베이스**로, Google의 Bigtable과 유사한 모델을 채택하고 있었다. HBase의 주요 개념과 기능, RDBMS와의 차이점을 배우면서 NoSQL 데이터베이스가 어떻게 구조화되지 않은 데이터를 효율적으로 관리하는지에 대해 이해할 수 있었다.

### 📝 배운 점

- **HBase의 데이터 구조**: HBase는 Row Key, Column Family, Column Qualifier, Timestamp로 구성된 데이터 구조를 통해 데이터를 관리한다. 이를 통해 각 데이터의 여러 버전을 저장하고 관리할 수 있는 강력한 기능을 제공한다는 점을 배웠다.
- **HBase와 RDBMS의 차이점**: 스키마 유연성, 수평 확장성, 데이터 모델링의 차이점을 이해함으로써 HBase가 특히 대규모 비정형 데이터 처리에 적합하다는 것을 알게 되었다.

### 🤔 이해하기 위해 노력한 점

- HBase의 복잡한 구조와 관계를 이해하기 위해 인터넷 검색을 통해 관련된 이미지를 구성했다. 시각적인 자료를 통해 각 요소들이 어떻게 연결되고 동작하는지 파악하는 데 도움이 되었다.
- 공부하는 과정에서 많은 설명이 표 형태로 되어 있어, 이를 구조적으로 이해하는 데 어려움이 있었다. 특히, 각 Column Family와 Column Qualifier의 관계를 테이블로 이해하려고 하니 다소 복잡하게 느껴졌다.
- 강사님이 설명해주신 대로 데이터를 호출할 때 한 줄씩 출력되는 모습을 보면서, HBase의 데이터 구조와 Row Key의 중요성을 더 잘 이해할 수 있었다. 이를 통해 데이터가 실제로 어떻게 저장되고 조회되는지를 시각적으로 확인할 수 있었다.

### 🛠️ 앞으로의 학습 방향

앞으로는 HBase의 실전 적용 사례를 더 탐구하고, 실제 데이터를 HBase에 저장하고 조회해보는 실습을 통해 이해를 심화시킬 계획이다. 특히, 대규모 데이터를 처리하는 환경에서 HBase가 어떻게 성능을 최적화하고 확장하는지를 직접 경험해 보고 싶다.
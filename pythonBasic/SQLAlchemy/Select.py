# 1. 오라클 접속정보
DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'
USERNAME = 'pythonTest' #enter your username
PASSWORD = '1234' #enter your password
HOST = 'localhost' #enter the oracle db host url
PORT = 1521 # enter the oracle port number
SERVICE = 'pythonTest' # enter the oracle db service name
ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE

# 2. 두부 연결을 위한 engine 생성 - lazy connecting
from sqlalchemy import create_engine
engine = create_engine(ENGINE_PATH_WIN_AUTH, echo=True, future=True)

# 3. DB Connection instance
conn = engine.connect()  # connection

# 4. Mapping and Create tables
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Sequence
metadata = MetaData()

users = Table('users', metadata,
             Column('id', Integer, Sequence('user_id_seq'), primary_key=True)
             ,Column('name', String(50))
             ,Column('fullname', String(50))
)

addresses = Table('addresses', metadata,
                  Column('id', Integer, Sequence('user_id_seq2'), primary_key=True)
                  ,Column('user_id', None, ForeignKey('users.id'))
                  ,Column('email_address', String(200), nullable=False)
)

# 5. select All
from sqlalchemy import select

s = select(users)
select_result = conn.execute(s)

for item in select_result:
    print(item)
# 데이터를 조회하고나면 조회한 부분은 사라진다. 하단의 fetchone() 메소드를 쓴 것과 같다.

select_result = conn.execute(s)
row = select_result.fetchone()
print(row[1], row[2])
row = select_result.fetchone()
print(row[1], row[2])
row = select_result.fetchone()
print(row[1], row[2])
row = select_result.fetchone()
print(row[1], row[2])
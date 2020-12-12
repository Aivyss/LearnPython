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

# insert 1 transaction
ins = users.insert().values(name='jack', fullname='Jack Jones')
conn.execute(ins)

# insert multiple transaction
ins = users.insert()
conn.execute(ins,
             [{"id": 2, "name": "wendy", "fullname": "Wendy Williams"},
             {"id": 3, "name": "taylor", "fullname": "Taylor Swift"},
             {"id": 4, "name": "Amelia", "fullname": "Amelia Baker"}]
) # [values1, values2, values3, ....] 구조로 insert를 복수수행 가능
# commit
conn.commit()

address_data = [{'user_id': 1, 'email_address': 'jack@gmail.com'},
                {'user_id': 1, 'email_address': 'jack@naver.com'},
                {'user_id': 2, 'email_address': 'wendy@gmail.com'},
                {'user_id': 2, 'email_address': 'wendy@daum.net'}]
conn.execute(addresses.insert(), address_data)
conn.commit()
import sqlalchemy as sa
import pandas as pd

def connect_db():
  LINK = 'postgresql://zlxwfroetvieql:4c6a9be7cfdb2a1fdd675c551c96ee873df393ecd31ba713fb2d8d5ac7d23e8c@ec2-52-3-60-53.compute-1.amazonaws.com:5432/d78i8bapo95qh'

  engine = sa.create_engine(LINK)

  return engine




def connect_dm():
  print("Abrindo conexão com o banco!")
  DIALECT = 'oracle'
  SQL_DRIVER = 'cx_oracle'
  USERNAME = 'uprova' #enter your username
  PASSWORD = '123456789' #enter your password
  HOST = 'oracle-74473-0.cloudclusters.net' #enter the oracle db host url
  PORT = 12272 # enter the oracle port number
  SERVICE = 'XE' # enter the oracle db service name
  ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE

  engine = sa.create_engine(ENGINE_PATH_WIN_AUTH)
  return engine








# engine_live = engine.connect()

# print(engine.has_table('relacional.vendas'))
# metadata = sa.MetaData(bind=None)
# sql = 'SELECT * FROM relacional.clientes'
# table_vendas = sa.Table('vendas', metadata, )
# result = engine.execute('SELECT COUNT(*) FROM relacional.clientes')
# print(type(result))

# df = pd.read_sql(sql, engine)

# for index,row in df.iterrows():
#   print(row)
from connect import connect_dm
import sqlalchemy as sa

engine = connect_dm()

metadata = sa.MetaData(bind=None)

table_test = sa.Table('CLIENTESDM', metadata, autoload=True, autoload_with=engine)

print('COLUMNS IN TABLE')
for column in table_test.c:
  print(column.name)
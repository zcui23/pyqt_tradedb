import sqlalchemy
import pyodbc





engine = sqlalchemy.create_engine('mssql+pyodbc://sqlserver')
conn = engine.connect()

metadata = sqlalchemy.MetaData(engine, reflect=True)

fd = metadata.tables['FundamentalData']
select_st = sqlalchemy.select([fd]).limit(10)

res = conn.execute(select_st)
result = res.fetchall()

print(result)
import psycopg2
import pandas as pd

def execute(query):
    pc.execute(query)
    return pc.fetchall()


#아래 정보를 입력
user = 'postgres'
password = 'pass'
host_product = 'localhost'
dbname = 'test'
port='5432'

product_connection_string = "dbname={dbname} user={user} host={host} password={password} port={port}"\
                            .format(dbname=dbname,
                                    user=user,
                                    host=host_product,
                                    password=password,
                                    port=port)    
try:
    product = psycopg2.connect(product_connection_string)
except:
    print("I am unable to connect to the database")

pc = product.cursor()

print(pc)
import mysql.connector
import os
'''
Run this file atleast once
'''

connection = mysql.connector.connect(host='localhost',
                                    database='',
                                    user='',
                                    password='')

mycursor = connection.cursor()


def new_func(filename):
    with open(filename,"rb") as fi:
        x = fi.read()
    return x


for i in os.listdir():
    query = """INSERT INTO IMAGES(ID,IMAGE) VALUES(%s,%s)"""  
    try:  
        mycursor.execute(query,(f"{i.replace('.png','')}",new_func(i),))
    except Exception:
        pass    

connection.commit()


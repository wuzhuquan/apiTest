import pymysql
import basedata

def getcursor():
    localhost = basedata.SQL_LOCALHOST
    user = basedata.SQL_USERNAME
    password = basedata.SQL_PASSWORD
    database = basedata.SQL_DATABASENAME
    db = pymysql.connect(localhost,user,password,database)
    cursor = db.cursor()
    return cursor



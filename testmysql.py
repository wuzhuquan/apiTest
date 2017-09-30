import getmysql
cursor = getmysql.getcursor()
cursor.execute("select * from test_info")
data = cursor.fetchone()
print(data)
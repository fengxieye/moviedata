import pymysql

connection = pymysql.connect(host='lcoalhost',
                             port=3306,
                             user='root',
                             password='root')
cur = connection.cursor()
cur.execute("use movie")

def insert(name, cover, start, count, value, tag, douban_id, t):
    sql = 'insert into movie(name, cover, start, count, )'

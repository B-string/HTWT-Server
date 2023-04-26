import pymysql


class DatabaseManager:

    db_con = None

    def database_connecting(self, host: str, port: int, user: str, passwd: str, db: str, charset: str = 'utf8'):
        if self.db_con == None:
            self.db_con = pymysql.Connect(
                host=host, port=port, user=user, password=passwd, db=db, charset=charset
            )
        else:
            print("이미 연결이 존재합니다.")

    def database_closing(self):
        self.db_con.close()


test = DatabaseManager()
host = "htwt-database-01.cojbxlb1vduo.ap-northeast-2.rds.amazonaws.com"
port = 3306
user = "admin"
passwd = "ZdTz73qh4YuB5quDLdvP"
db = "htwt"


a = DatabaseManager()
a.database_connecting(host, port, user, passwd, db)

cursor = a.db_con.cursor()
sql = """
select * from test;
"""

cursor.execute(sql)
print(cursor.fetchall())

a.database_closing()

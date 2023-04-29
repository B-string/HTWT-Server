import pymysql


class DatabaseManager:

    db_con = None
    cursor = None

    def database_connecting(self, host: str, port: int, user: str, passwd: str, db: str, charset: str = 'utf8'):
        if self.db_con == None:
            self.db_con = pymysql.Connect(
                host=host, port=port, user=user, password=passwd, db=db, charset=charset
            )
            self.cursor = self.db_con.cursor()
        else:
            print("이미 연결이 존재합니다.")

    def insert_short_term_forecast(self, table: str, key: str, val: dict = {}):
        sql = f"insert into {table} values(\"{key}\""

        for i in val.values():
            sql += f", \"{i}\""
        sql += ");"
        print(sql)
        self.cursor.execute(sql)
        self.db_con.commit()

    # def insert_medium_term_tem_forecast(self, table: str, key: str, val: dict = {}):

    def database_closing(self):
        self.db_con.close()

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

    def insert_short_term_forecast(self, items: list):
        for item in items:
            sql = f"insert into short_term_weather_data(base_datetime, fcst_datetime, nx, ny, temperature, max_temperature, min_temperature, u_wind, v_wind, wind_direction, wind_speed, sky_condition, precipitation_type, probability_of_precipitation, wave_height, precipitation_amount, relative_humidity, snowfall_amount) values(\"{item['base_datetime']}\", \"{item['fcst_datetime']}\", {item['nx']}, {item['ny']}, {item['temperature']}, {item['max_temperature']}, {item['min_temperature']}, {item['u_wind']}, {item['v_wind']}, {item['wind_direction']}, {item['wind_speed']}, {item['sky_condition']}, {item['precipitation_type']}, {item['probability_of_precipitation']}, {item['wave_height']}, \"{item['precipitation_amount']}\", {item['relative_humidity']}, \"{item['snowfall_amount']}\")"
            print(sql)
            self.cursor.execute(sql)

        self.db_con.commit()
        # sql = f"insert into {table} values(\"{key}\""

        # for i in val.values():
        #     sql += f", \"{i}\""
        # sql += ");"
        # print(sql)
        # self.cursor.execute(sql)
        # self.db_con.commit()

    # def insert_medium_term_tem_forecast(self, table: str, key: str, val: dict = {}):

    def database_closing(self):
        self.db_con.close()

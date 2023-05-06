import pymysql


class DatabaseManager:

    db_con = None
    cursor = None
    tables = ["short_term_weather_data",
              "mid_term_outlook", "mid_term_temperature"]

    def database_connecting(self, host: str, port: int, user: str, passwd: str, db: str, charset: str = 'utf8'):
        if self.db_con == None:
            self.db_con = pymysql.Connect(
                host=host, port=port, user=user, password=passwd, db=db, charset=charset
            )
            self.cursor = self.db_con.cursor()
        else:
            print("이미 연결이 존재합니다.")

    def init_table(self):
        try:
            with self.db_con.cursor() as cursor:
                for table in self.tables:
                    sql = f"TRUNCATE {table}"
                    cursor.execute(sql)
        except pymysql.err as e:
            print(e)
            self.db_con.rollback()
        # self.db_con.commit()

    def insert_short_term_forecast(self, items: list):
        try:
            with self.db_con.cursor() as cursor:
                for item in items:
                    # sql 문을 개선할 수 있는지 고민해보자
                    sql = f"insert into short_term_weather_data(base_datetime, fcst_datetime, nx, ny, temperature, max_temperature, min_temperature, u_wind, v_wind, wind_direction, wind_speed, sky_condition, precipitation_type, probability_of_precipitation, wave_height, precipitation_amount, relative_humidity, snowfall_amount) values(STR_TO_DATE(\"{item.base_datetime}\", \"%Y%m%d%H%i\"), STR_TO_DATE(\"{item.fcst_datetime}\", \"%Y%m%d%H%i\"), {item.nx}, {item.ny}, {item.temperature}, {item.max_temperature}, {item.min_temperature}, {item.u_wind}, {item.v_wind}, {item.wind_direction}, {item.wind_speed}, {item.sky_condition}, {item.precipitation_type}, {item.probability_of_precipitation}, {item.wave_height}, \"{item.precipitation_amount}\", {item.relative_humidity}, \"{item.snowfall_amount}\")"
                    print(sql)
                    cursor.execute(sql)
        except pymysql.err as e:
            print(e)
            self.db_con.rollback()

        # self.db_con.commit()
        # sql = f"insert into {table} values(\"{key}\""

        # for i in val.values():
        #     sql += f", \"{i}\""
        # sql += ");"
        # print(sql)
        # self.cursor.execute(sql)
        # self.db_con.commit()

    # def insert_medium_term_tem_forecast(self, table: str, key: str, val: dict = {}):

    def insert_mid_term_outlook(self, item):
        try:
            with self.db_con.cursor() as cursor:
                sql = f"insert into mid_term_outlook(base_datetime, stn_id, wf_sv) values(STR_TO_DATE(\"{item.base_datetime}\",\"%Y%m%d%H%i\"), {item.stn_id}, \"{item.wf_sv}\")"
                print(sql)
                cursor.execute(sql)
        except pymysql.err as e:
            print(e)
            self.db_con.rollback()
        # self.db_con.commit()

    def insert_mid_term_temperature(self, item):

        try:
            with self.db_con.cursor() as cursor:
                sql = "INSERT INTO mid_term_temperature (base_datetime, reg_id"

                values = f"VALUES (STR_TO_DATE(\"{item.base_datetime}\", \"%Y%m%d%H%i\"), '{item.reg_id}'"
                for key, val in item.ta_max.items():
                    sql += f", {key}"
                    values += f", {val}"

                for key, val in item.ta_max_low.items():
                    sql += f", {key}"
                    values += f", {val}"

                for key, val in item.ta_max_high.items():
                    sql += f", {key}"
                    values += f", {val}"

                for key, val in item.ta_min.items():
                    sql += f", {key}"
                    values += f", {val}"

                for key, val in item.ta_min_low.items():
                    sql += f", {key}"
                    values += f", {val}"

                for key, val in item.ta_min_high.items():
                    sql += f", {key}"
                    values += f", {val}"
                sql += ")"
                values += ");"

                sql += values
                print(sql)
                cursor.execute(sql)
        except pymysql.err as e:
            print(e)
            self.db_con.rollback()

    def database_closing(self):
        self.db_con.commit()
        self.db_con.close()
        self.db_con = None
        self.cursor = None

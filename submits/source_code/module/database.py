
import pymysql


class Database:
    def connect(self):

        return pymysql.connect(host="127.0.0.1", user="root", password="", database="dm", charset='utf8mb4')

    def getTmeSiries(self,date):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("SELECT * FROM timeseries where date = %s", (date,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()


    def insertTmeSiries(self,date,vol):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            print("storing in db")
            cursor.execute("INSERT INTO timeseries(date, vol) VALUES (%s,%s)",(date,vol,))

            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM phone_book order by name asc")
            else:
                cursor.execute(
                    "SELECT * FROM phone_book where id = %s order by name asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()


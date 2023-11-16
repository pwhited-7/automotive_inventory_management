import pymysql as sql
import Config
from DatabaseConnector import DatabaseConnector

if __name__ == '__main__':
    # connection = DatabaseConnector(host=Config.HOST, username=Config.USER, password=Config.PASSWORD)
    # connection.connect()
    # print(connection.get_table_names())
    # connection.use_database("automotive_inventory")
    # # print(connection.execute_query("insert into Suppliers (name, contact_info) values ('wix', 'wix@gmail.com')"))
    # print(connection.execute_query("select * from Suppliers"))

    # connection.close_connection()
    conn = sql.connect(host=Config.HOST, user=Config.USER, password=Config.PASSWORD)
    conn.connect()

    cursor = conn.cursor()
    cursor.execute("use automotive_inventory")
    # cursor.execute("insert into Suppliers (name, contact_info) values ('Wix', 'Wix@gmail.com')")
    cursor.execute("ALTER TABLE Suppliers AUTO_INCREMENT = 1")
    # cursor.execute("delete from Suppliers")
    conn.commit()
    cursor.execute("select * from Suppliers")
    data = cursor.fetchall()
    print(data)

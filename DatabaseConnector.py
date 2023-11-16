import pymysql
import Config

class DatabaseConnector:

    def __init__(self, host=Config.HOST, username=Config.USER, password=Config.PASSWORD):
        self.host = host
        self.username = username
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.username,
                password=self.password,
            )
            print("Connected to the automotive database.")
        except pymysql.Error as e:
            print(f"Error connecting to the automotive database: {e}")

    def execute_query(self, query):
        if self.connection:
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute(query)
                    self.connection.commit()
                    result = cursor.fetchall()
                    return result
            except pymysql.Error as e:
                print(f"Error executing query: {e}")
        else:
            print("Database connection is not established.")

    def use_database(self, database_name):
        if self.connection:
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute(f"USE {database_name};")
                    print(f"Using database: {database_name}")
            except pymysql.Error as e:
                print(f"Error switching database: {e}")
        else:
            print("Database connection is not established.")

    def get_table_names(self):
        if self.connection:
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute("SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = %s;",
                                   ('automotive_inventory',))
                    table_names = cursor.fetchall()
                    return [table[0] for table in table_names]  # Extracting table names from the result
            except pymysql.Error as e:
                print(f"Error retrieving table names: {e}")
        else:
            print("Database connection is not established.")

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")


if __name__ == '__main__':
    from Config import USER, HOST, PASSWORD

    db = DatabaseConnector(HOST, USER, PASSWORD)
    db.connect()
    db.use_database("automotive_inventory")
    # query = """
    #
    # """
    print(db.get_table_names())
    # print(db.execute_query(query))
    db.close_connection()

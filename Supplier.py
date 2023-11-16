from DatabaseConnector import DatabaseConnector
import pymysql
class Supplier:
    def __init__(self, connector):
        self.connector = connector

    def create_supplier(self, name, contact_info):
        result = self.check_supplier_name(name)
        if result > 0:
            id = self.get_supplier_id_by_name(name)
            print(f"This Supplier already exists with supplier_id: {id}")

        else:
            query = f"INSERT INTO Suppliers (name, contact_info) VALUES ('{name}', '{contact_info}')"
            return self.connector.execute_query(query)

    def get_supplier_info(self):
        # self.connector.connect()
        # self.connector.use_database("automotive_inventory")
        query = "SELECT * FROM Suppliers"
        return self.connector.execute_query(query)

    def delete_supplier_table(self):
        query = "DELETE FROM Suppliers"
        self.connector.execute_query(query)
        print("Suppliers table deleted")
        query = "ALTER TABLE Suppliers AUTO_INCREMENT = 1"
        self.connector.execute_query(query)
        print("Table auto increment reset to 1")

    def check_supplier_name(self, name):
        query = f"SELECT COUNT(*) FROM Suppliers WHERE LOWER(name) = LOWER('{name}')"
        result = self.connector.execute_query(query)
        if result and result[0][0] > 0:
            return True  # Name exists in the table
        else:
            return False  # Name doesn't exist or query failed

    def get_supplier_id_by_name(self, name):
        query = f"SELECT supplier_id FROM Suppliers WHERE LOWER(name) = LOWER('{name}')"
        result = self.connector.execute_query(query)
        if result:
            return result[0][0]  # Returns the supplier ID if found
        else:
            return None  # Supplier name not found or query failed

if __name__ == '__main__':
    conn = DatabaseConnector()
    conn.connect()
    conn.use_database('automotive_inventory')
    # query = "SELECT * FROM Suppliers"
    name = "Husky"
    contact_info = "wix@gmail.com"
    # query = f"INSERT INTO Suppliers (name, contact_info) VALUES ('{name}', '{contact_info}')"
    # query = f"SELECT supplier_id FROM Suppliers WHERE name = '{name}'"
    # rows = conn.execute_query(query)
    # print(rows)
    supp = Supplier(conn)
    # print(supp.get_supplier_id_by_name("Husky"))
    supp.create_supplier("wix", "wix@gmail.com")
    # print(supp.get_supplier_info())
    # supp.delete_supplier_table()
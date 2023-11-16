from DatabaseConnector import DatabaseConnector
class Warehouse:
    def __init__(self, connector):
        self.connector = connector

    def create_warehouse(self, location, capacity):
        result = self.check_warehouse_location(location)
        if result > 0:
            id = self.get_warehouse_id_by_location(location)
            print(f"This Warehouse already exists with warehouse_id: {id}")
        else:
            query = f"INSERT INTO Warehouses (location, capacity) VALUES ('{location}', {capacity})"
            return self.connector.execute_query(query)

    def get_warehouse_info(self):
        query = "SELECT * FROM Warehouses"
        return self.connector.execute_query(query)

    def check_warehouse_location(self, location):
        query = f"SELECT COUNT(*) FROM Warehouses WHERE LOWER(location) = LOWER('{location}')"
        result = self.connector.execute_query(query)
        if result and result[0][0] > 0:
            return True  # Location exists in the table
        else:
            return False  # Location doesn't exist or query failed
    def delete_warehouse_table(self):
        query = "DELETE FROM Warehouses"
        self.connector.execute_query(query)
        print("Warehouses table deleted")
        query = "ALTER TABLE Warehouses AUTO_INCREMENT = 1"
        self.connector.execute_query(query)
        print("Table auto increment reset to 1")
    def get_warehouse_id_by_location(self, location):
        query = f"SELECT warehouse_id FROM Warehouses WHERE LOWER(location) = LOWER('{location}')"
        result = self.connector.execute_query(query)
        if result:
            return result[0][0]  # Returns the warehouse ID if found
        else:
            return None  # Warehouse location not found or query failed

if __name__ == '__main__':
    conn = DatabaseConnector()
    conn.connect()
    conn.use_database("automotive_inventory")

    warehouse = "Denver"
    capacity = 1000

    ware = Warehouse(conn)
    ware.create_warehouse(warehouse, capacity)
    # print(ware.get_warehouse_info())
    # print(ware.check_warehouse_location(warehouse))
    # print(ware.get_warehouse_id_by_location(warehouse))
    # ware.delete_warehouse_table()
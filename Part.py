from DatabaseConnector import DatabaseConnector


class Part:

    def __init__(self, connector):
        self.connector = connector

    def add_part(self, part_number, description, quantity, price, supplier_id, warehouse_id):

        supplier_ids = self.get_supplier_ids()
        warehouse_ids = self.get_warehouse_ids()
        supplier_flag = self.check_supplies_id(supplier_ids, supplier_id)
        warehouse_flag = self.check_warehouse_id(warehouse_ids, warehouse_id)

        if warehouse_flag is False and supplier_flag is False:
            print("The provided supplier and warehouse ID's do not exist in the database")

        elif warehouse_flag is False:
            print("The provided warehouse_id does not match warehouses in the databse")

        elif supplier_flag is False:
            print("The provided supplier_id does not match suppliers in the database")

        else:
            query = f"INSERT INTO Parts (part_number, description, quantity, price, supplier_id, warehouse_id) " \
                f"VALUES ('{part_number}', '{description}', {quantity}, {price}, {supplier_id}, {warehouse_id})"
            return self.connector.execute_query(query)
        return None

    def get_supplier_ids(self):
        query = "SELECT supplier_id FROM Suppliers"
        result = self.connector.execute_query(query)
        arr = []
        for row in result:
            arr.append(row[0])
        return arr

    def get_warehouse_ids(self):
        query = "SELECT warehouse_id FROM Warehouses"
        result = self.connector.execute_query(query)
        arr = []
        for row in result:
            arr.append(row[0])
        return arr

    def check_supplies_id(self, supplier_ids, supp_id):
        supp_flag = True
        if supp_id not in supplier_ids:
            supp_flag = False
        return supp_flag

    def check_warehouse_id(self, warehouse_ids, ware_id):
        ware_flag = True
        if ware_id not in warehouse_ids:
            ware_flag = False
        return ware_flag

    def get_parts(self):
        query = "SELECT * FROM Parts"
        return self.connector.execute_query(query)


if __name__ == '__main__':
    conn = DatabaseConnector()
    conn.connect()
    conn.use_database('automotive_inventory')

    part = Part(conn)
    part_number = "P001"
    description = "Engine Oil Filter"
    quantity = 100
    price = 15.99
    supplier_id = 1  # Assuming a valid supplier ID
    warehouse_id = 1

    # result = part.add_part(part_number, description, quantity, price, supplier_id, warehouse_id)
    # print(part.get_parts())

    # result = part.add_part(part_number, description, quantity, price, supplier_id, warehouse_id)
    # if result:
    #     print("Part added successfully!")
    # else:
    #     print("Failed to add the part.")

    conn.close_connection()

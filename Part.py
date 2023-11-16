from DatabaseConnector import DatabaseConnector


class Part:

    def __init__(self, connector):
        self.connector = connector

    def add_part(self, part_number, description, quantity, price, supplier_id, warehouse_id):
        query = f"INSERT INTO Parts (part_number, description, quantity, price, supplier_id, warehouse_id) " \
                f"VALUES ('{part_number}', '{description}', {quantity}, {price}, {supplier_id}, {warehouse_id})"
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

    result = part.add_part(part_number, description, quantity, price, supplier_id, warehouse_id)
    if result:
        print("Part added successfully!")
    else:
        print("Failed to add the part.")

    conn.close_connection()



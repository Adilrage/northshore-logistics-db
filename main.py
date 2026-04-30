import sqlite3
from datetime import datetime


DB_NAME = r"C:\Users\anasr\northshore_logistics.db"


def connect_db():
    return sqlite3.connect(DB_NAME)


def view_shipments():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.shipment_id, s.order_number, s.status, s.cost,
               c1.name AS sender_name,
               c2.name AS receiver_name
        FROM Shipments s
        JOIN Customers c1 ON s.sender_id = c1.customer_id
        JOIN Customers c2 ON s.receiver_id = c2.customer_id
    """)

    rows = cursor.fetchall()

    print("\nShipment Records")
    print("-" * 70)

    for row in rows:
        print(f"ID: {row[0]} | Order: {row[1]} | Status: {row[2]} | Cost: £{row[3]}")
        print(f"Sender: {row[4]} | Receiver: {row[5]}")
        print("-" * 70)

    conn.close()


def view_incidents():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT i.incident_id, s.order_number, i.incident_type,
               i.description, i.reported_date, i.resolution_status
        FROM Incidents i
        JOIN Shipments s ON i.shipment_id = s.shipment_id
    """)

    rows = cursor.fetchall()

    print("\nIncident Reports")
    print("-" * 70)

    for row in rows:
        print(f"Incident ID: {row[0]} | Order: {row[1]}")
        print(f"Type: {row[2]} | Date: {row[4]} | Resolution: {row[5]}")
        print(f"Details: {row[3]}")
        print("-" * 70)

    conn.close()


def view_available_vehicles():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT vehicle_id, registration_number, capacity, status
        FROM Vehicles
        WHERE status = 'Available'
    """)

    rows = cursor.fetchall()

    print("\nAvailable Vehicles")
    print("-" * 70)

    for row in rows:
        print(f"Vehicle ID: {row[0]} | Reg: {row[1]} | Capacity: {row[2]}kg | Status: {row[3]}")

    conn.close()


def check_low_inventory():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT w.name, i.item_name, i.quantity, i.reorder_level
        FROM Inventory i
        JOIN Warehouses w ON i.warehouse_id = w.warehouse_id
        WHERE i.quantity <= i.reorder_level
    """)

    rows = cursor.fetchall()

    print("\nLow Inventory Report")
    print("-" * 70)

    if len(rows) == 0:
        print("No low stock items found.")
    else:
        for row in rows:
            print(f"Warehouse: {row[0]} | Item: {row[1]} | Quantity: {row[2]} | Reorder Level: {row[3]}")

    conn.close()


def add_audit_log(user_id, action, table_name):
    conn = connect_db()
    cursor = conn.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO AuditLog (user_id, action, table_name, timestamp)
        VALUES (?, ?, ?, ?)
    """, (user_id, action, table_name, timestamp))

    conn.commit()
    conn.close()


def update_delivery_status():
    delivery_id = input("Enter delivery ID: ")
    new_status = input("Enter new delivery status: ")

    allowed_statuses = ["In Transit", "Delivered", "Delayed", "Returned", "Failed"]

    if new_status not in allowed_statuses:
        print("Invalid status. Use: In Transit, Delivered, Delayed, Returned, or Failed.")
        return

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Deliveries
        SET delivery_status = ?
        WHERE delivery_id = ?
    """, (new_status, delivery_id))

    conn.commit()
    conn.close()

    add_audit_log(1, f"Updated delivery {delivery_id} status to {new_status}", "Deliveries")

    print("Delivery status updated successfully.")


def main_menu():
    while True:
        print("\nNorthshore Logistics Database System")
        print("1. View shipments")
        print("2. View incident reports")
        print("3. View available vehicles")
        print("4. Check low inventory")
        print("5. Update delivery status")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_shipments()
        elif choice == "2":
            view_incidents()
        elif choice == "3":
            view_available_vehicles()
        elif choice == "4":
            check_low_inventory()
        elif choice == "5":
            update_delivery_status()
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Try again.")


main_menu()
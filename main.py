import sqlite3
import hashlib
from datetime import datetime


DB_NAME = r"C:\Users\anasr\northshore_logistics.db"


def connect_db():
    return sqlite3.connect(DB_NAME)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def setup_default_users():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM Users")
    user_count = cursor.fetchone()[0]

    if user_count == 0:
        users = [
            ("admin", hash_password("admin123"), "admin"),
            ("manager", hash_password("manager123"), "manager"),
            ("staff", hash_password("staff123"), "warehouse_staff")
        ]

        cursor.executemany("""
            INSERT INTO Users (username, password_hash, role)
            VALUES (?, ?, ?)
        """, users)

        conn.commit()

    conn.close()


def login():
    print("\nNorthshore Logistics Login")
    print("-" * 40)

    username = input("Username: ")
    password = input("Password: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT user_id, username, role
        FROM Users
        WHERE username = ? AND password_hash = ?
    """, (username, hash_password(password)))

    user = cursor.fetchone()
    conn.close()

    if user:
        print(f"\nLogin successful. Welcome, {user[1]} ({user[2]}).")
        return {
            "user_id": user[0],
            "username": user[1],
            "role": user[2]
        }

    print("Login failed. Incorrect username or password.")
    return None


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

    if not rows:
        print("No shipment records found.")
    else:
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

    if not rows:
        print("No incident reports found.")
    else:
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

    if not rows:
        print("No available vehicles found.")
    else:
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

    if not rows:
        print("No low stock items found.")
    else:
        for row in rows:
            print(f"Warehouse: {row[0]} | Item: {row[1]} | Quantity: {row[2]} | Reorder Level: {row[3]}")

    conn.close()


def update_delivery_status(current_user):
    allowed_roles = ["admin", "manager"]

    if current_user["role"] not in allowed_roles:
        print("Access denied. Only admin and manager users update delivery status.")
        return

    delivery_id = input("Enter delivery ID: ")
    new_status = input("Enter new delivery status: ")

    allowed_statuses = ["In Transit", "Delivered", "Delayed", "Returned", "Failed"]

    if new_status not in allowed_statuses:
        print("Invalid status. Use: In Transit, Delivered, Delayed, Returned, or Failed.")
        return

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT delivery_id FROM Deliveries WHERE delivery_id = ?", (delivery_id,))
    delivery = cursor.fetchone()

    if not delivery:
        print("Delivery ID not found.")
        conn.close()
        return

    cursor.execute("""
        UPDATE Deliveries
        SET delivery_status = ?
        WHERE delivery_id = ?
    """, (new_status, delivery_id))

    conn.commit()
    conn.close()

    add_audit_log(
        current_user["user_id"],
        f"Updated delivery {delivery_id} status to {new_status}",
        "Deliveries"
    )

    print("Delivery status updated successfully.")


def view_audit_logs(current_user):
    if current_user["role"] != "admin":
        print("Access denied. Only admin users view audit logs.")
        return

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT a.log_id, u.username, a.action, a.table_name, a.timestamp
        FROM AuditLog a
        JOIN Users u ON a.user_id = u.user_id
        ORDER BY a.timestamp DESC
    """)

    rows = cursor.fetchall()

    print("\nAudit Log")
    print("-" * 80)

    if not rows:
        print("No audit log entries found.")
    else:
        for row in rows:
            print(f"Log ID: {row[0]} | User: {row[1]} | Table: {row[3]} | Time: {row[4]}")
            print(f"Action: {row[2]}")
            print("-" * 80)

    conn.close()


def main_menu(current_user):
    while True:
        print("\nNorthshore Logistics Database System")
        print(f"Logged in as: {current_user['username']} | Role: {current_user['role']}")
        print("1. View shipments")
        print("2. View incident reports")
        print("3. View available vehicles")
        print("4. Check low inventory")
        print("5. Update delivery status")
        print("6. View audit logs")
        print("7. Exit")

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
            update_delivery_status(current_user)
        elif choice == "6":
            view_audit_logs(current_user)
        elif choice == "7":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Try again.")


setup_default_users()

user = login()

if user:
    main_menu(user)
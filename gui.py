import sqlite3
import tkinter as tk
from tkinter import messagebox


DB_NAME = r"C:\Users\anasr\northshore_logistics.db"


def connect_db():
    return sqlite3.connect(DB_NAME)


def show_shipments():
    output_box.delete("1.0", tk.END)

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
    conn.close()

    if not rows:
        output_box.insert(tk.END, "No shipment records found.")
        return

    for row in rows:
        output_box.insert(tk.END, f"Shipment ID: {row[0]}\n")
        output_box.insert(tk.END, f"Order Number: {row[1]}\n")
        output_box.insert(tk.END, f"Status: {row[2]}\n")
        output_box.insert(tk.END, f"Cost: £{row[3]}\n")
        output_box.insert(tk.END, f"Sender: {row[4]}\n")
        output_box.insert(tk.END, f"Receiver: {row[5]}\n")
        output_box.insert(tk.END, "-" * 50 + "\n")


def show_delivery_progress():
    output_box.delete("1.0", tk.END)

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT d.delivery_id, s.order_number, d.delivery_status,
               dr.name AS driver_name,
               v.registration_number,
               d.route_info,
               d.delivery_date
        FROM Deliveries d
        JOIN Shipments s ON d.shipment_id = s.shipment_id
        JOIN Drivers dr ON d.driver_id = dr.driver_id
        JOIN Vehicles v ON d.vehicle_id = v.vehicle_id
    """)

    rows = cursor.fetchall()
    conn.close()

    if not rows:
        output_box.insert(tk.END, "No delivery records found.")
        return

    for row in rows:
        output_box.insert(tk.END, f"Delivery ID: {row[0]}\n")
        output_box.insert(tk.END, f"Order Number: {row[1]}\n")
        output_box.insert(tk.END, f"Status: {row[2]}\n")
        output_box.insert(tk.END, f"Driver: {row[3]}\n")
        output_box.insert(tk.END, f"Vehicle: {row[4]}\n")
        output_box.insert(tk.END, f"Route: {row[5]}\n")
        output_box.insert(tk.END, f"Date: {row[6]}\n")
        output_box.insert(tk.END, "-" * 50 + "\n")


def show_incidents():
    output_box.delete("1.0", tk.END)

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT i.incident_id, s.order_number, i.incident_type,
               i.description, i.reported_date, i.resolution_status
        FROM Incidents i
        JOIN Shipments s ON i.shipment_id = s.shipment_id
    """)

    rows = cursor.fetchall()
    conn.close()

    if not rows:
        output_box.insert(tk.END, "No incident records found.")
        return

    for row in rows:
        output_box.insert(tk.END, f"Incident ID: {row[0]}\n")
        output_box.insert(tk.END, f"Order Number: {row[1]}\n")
        output_box.insert(tk.END, f"Type: {row[2]}\n")
        output_box.insert(tk.END, f"Description: {row[3]}\n")
        output_box.insert(tk.END, f"Reported Date: {row[4]}\n")
        output_box.insert(tk.END, f"Resolution: {row[5]}\n")
        output_box.insert(tk.END, "-" * 50 + "\n")


def show_low_inventory():
    output_box.delete("1.0", tk.END)

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT w.name, i.item_name, i.quantity, i.reorder_level
        FROM Inventory i
        JOIN Warehouses w ON i.warehouse_id = w.warehouse_id
        WHERE i.quantity <= i.reorder_level
    """)

    rows = cursor.fetchall()
    conn.close()

    if not rows:
        output_box.insert(tk.END, "No low stock items found.")
        return

    for row in rows:
        output_box.insert(tk.END, f"Warehouse: {row[0]}\n")
        output_box.insert(tk.END, f"Item: {row[1]}\n")
        output_box.insert(tk.END, f"Quantity: {row[2]}\n")
        output_box.insert(tk.END, f"Reorder Level: {row[3]}\n")
        output_box.insert(tk.END, "-" * 50 + "\n")


def update_delivery_status():
    delivery_id = delivery_id_entry.get()
    new_status = status_entry.get()

    allowed_statuses = ["In Transit", "Delivered", "Delayed", "Returned", "Failed"]

    if new_status not in allowed_statuses:
        messagebox.showerror("Error", "Invalid status. Use: In Transit, Delivered, Delayed, Returned, or Failed.")
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

    messagebox.showinfo("Success", "Delivery status updated successfully.")
    show_delivery_progress()


root = tk.Tk()
root.title("Northshore Logistics Database System")
root.geometry("850x600")

title_label = tk.Label(root, text="Northshore Logistics Database System", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="View Shipments", width=22, command=show_shipments).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Delivery Progress", width=22, command=show_delivery_progress).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="View Incidents", width=22, command=show_incidents).grid(row=0, column=2, padx=5, pady=5)
tk.Button(button_frame, text="Low Inventory", width=22, command=show_low_inventory).grid(row=1, column=0, padx=5, pady=5)

update_frame = tk.LabelFrame(root, text="Update Delivery Status")
update_frame.pack(pady=10)

tk.Label(update_frame, text="Delivery ID:").grid(row=0, column=0, padx=5, pady=5)
delivery_id_entry = tk.Entry(update_frame)
delivery_id_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(update_frame, text="New Status:").grid(row=0, column=2, padx=5, pady=5)
status_entry = tk.Entry(update_frame)
status_entry.grid(row=0, column=3, padx=5, pady=5)

tk.Button(update_frame, text="Update", command=update_delivery_status).grid(row=0, column=4, padx=5, pady=5)

output_box = tk.Text(root, height=22, width=100)
output_box.pack(pady=10)

root.mainloop()
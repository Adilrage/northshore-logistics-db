CREATE TABLE Warehouses (
warehouse_id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
address TEXT NOT NULL,
phone TEXT
);

CREATE TABLE Customers (
customer_id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
phone TEXT,
address TEXT NOT NULL,
email TEXT
);

CREATE TABLE Vehicles (
vehicle_id INTEGER PRIMARY KEY,
registration_number TEXT NOT NULL,
capacity REAL NOT NULL,
status TEXT NOT NULL,
last_maintenance TEXT
);

CREATE TABLE Drivers (
driver_id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
phone TEXT,
license_number TEXT NOT NULL,
status TEXT NOT NULL
);

CREATE TABLE Shipments (
shipment_id INTEGER PRIMARY KEY,
order_number TEXT NOT NULL UNIQUE,
sender_id INTEGER NOT NULL,
receiver_id INTEGER NOT NULL,
description TEXT,
cost REAL NOT NULL,
status TEXT NOT NULL,
warehouse_id INTEGER NOT NULL,
created_date TEXT NOT NULL,
FOREIGN KEY (sender_id) REFERENCES Customers(customer_id),
FOREIGN KEY (receiver_id) REFERENCES Customers(customer_id),
FOREIGN KEY (warehouse_id) REFERENCES Warehouses(warehouse_id)
);

CREATE TABLE Deliveries (
delivery_id INTEGER PRIMARY KEY,
shipment_id INTEGER NOT NULL UNIQUE,
vehicle_id INTEGER NOT NULL,
driver_id INTEGER NOT NULL,
route_info TEXT,
delivery_date TEXT,
delivery_status TEXT NOT NULL,
FOREIGN KEY (shipment_id) REFERENCES Shipments(shipment_id),
FOREIGN KEY (vehicle_id) REFERENCES Vehicles(vehicle_id),
FOREIGN KEY (driver_id) REFERENCES Drivers(driver_id)
);

CREATE TABLE Incidents (
incident_id INTEGER PRIMARY KEY,
shipment_id INTEGER NOT NULL,
incident_type TEXT NOT NULL,
description TEXT,
reported_date TEXT NOT NULL,
resolution_status TEXT NOT NULL,
FOREIGN KEY (shipment_id) REFERENCES Shipments(shipment_id)
);

CREATE TABLE Inventory (
inventory_id INTEGER PRIMARY KEY,
warehouse_id INTEGER NOT NULL,
item_name TEXT NOT NULL,
quantity INTEGER NOT NULL,
reorder_level INTEGER NOT NULL,
FOREIGN KEY (warehouse_id) REFERENCES Warehouses(warehouse_id)
);

CREATE TABLE Users (
user_id INTEGER PRIMARY KEY,
username TEXT NOT NULL UNIQUE,
password_hash TEXT NOT NULL,
role TEXT NOT NULL
);

CREATE TABLE AuditLog (
log_id INTEGER PRIMARY KEY,
user_id INTEGER NOT NULL,
action TEXT NOT NULL,
table_name TEXT NOT NULL,
timestamp TEXT NOT NULL,
FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
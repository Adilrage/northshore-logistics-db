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
INSERT INTO Warehouses (name, address, phone) VALUES
('North Hub', 'Birmingham Industrial Park', '0121 555 1000'),
('South Depot', 'London River Road', '020 555 2000');

INSERT INTO Customers (name, phone, address, email) VALUES
('Aisha Khan', '07111111111', 'Manchester', 'aisha@email.com
'),
('Omar Ali', '07222222222', 'Leeds', 'omar@email.com
');

INSERT INTO Drivers (name, phone, license_number, status) VALUES
('Daniel Smith', '07333333333', 'DRV123', 'Active'),
('Hassan Malik', '07444444444', 'DRV456', 'Active');

INSERT INTO Vehicles (registration_number, capacity, status, last_maintenance) VALUES
('NX21ABC', 1200, 'Available', '2026-03-01'),
('LT22XYZ', 900, 'Available', '2026-03-10');

INSERT INTO Shipments (order_number, sender_id, receiver_id, description, cost, status, warehouse_id, created_date) VALUES
('ORD001', 1, 2, 'Electronics package', 150.00, 'In Transit', 1, '2026-04-01'),
('ORD002', 2, 1, 'Clothing delivery', 80.00, 'Delivered', 2, '2026-04-02');

INSERT INTO Deliveries (shipment_id, vehicle_id, driver_id, route_info, delivery_date, delivery_status) VALUES
(1, 1, 1, 'Route A1', '2026-04-03', 'In Transit'),
(2, 2, 2, 'Route B2', '2026-04-04', 'Delivered');

INSERT INTO Incidents (shipment_id, incident_type, description, reported_date, resolution_status) VALUES
(1, 'Delay', 'Traffic delay on route', '2026-04-03', 'Pending');
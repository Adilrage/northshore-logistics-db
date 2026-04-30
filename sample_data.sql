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
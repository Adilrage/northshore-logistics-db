SELECT d.delivery_id, d.delivery_status, d.delivery_date,
dr.name AS driver_name,
v.registration_number
FROM Deliveries d
JOIN Drivers dr ON d.driver_id = dr.driver_id
JOIN Vehicles v ON d.vehicle_id = v.vehicle_id;

SELECT i.incident_id, i.incident_type, i.description, i.reported_date,
s.order_number
FROM Incidents i
JOIN Shipments s ON i.shipment_id = s.shipment_id;

SELECT w.name AS warehouse_name, i.item_name, i.quantity, i.reorder_level
FROM Inventory i
JOIN Warehouses w ON i.warehouse_id = w.warehouse_id;

SELECT order_number, status, cost
FROM Shipments
WHERE status = 'Delivered';
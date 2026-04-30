# northshore-logistics-db
# Northshore Logistics Database System

## Project Overview

This project is a database-driven system for Northshore Logistics Ltd. It manages shipment records, deliveries, incidents, warehouses, inventory, drivers, vehicles, users, and audit logs.

The system uses SQLite for the database and Python for the application. It includes both a command-line interface and a Tkinter graphical user interface.

## Main Features

- View shipment records with sender and receiver details
- Track delivery progress
- View and add incident reports
- View available vehicles and active drivers
- Check low inventory levels
- Update delivery status
- Assign drivers and vehicles to deliveries
- User login with hashed passwords
- Role-based access control
- Audit logging of key actions
- Tkinter graphical interface

## Tools Used

- Python 3.11+
- SQLite 3
- SQLiteStudio
- PyCharm
- Git and GitHub
- DBML
- Draw.io
- Tkinter
- hashlib
- datetime
- sqlite3

## Files Included

- main.py, command-line version of the system
- gui.py, graphical user interface version
- database.sql, database table creation script
- sample_data.sql, sample data insertion script
- queries.sql, test queries used to validate the database
- schema.dbml, DBML schema design
- er_diagram.png, entity relationship diagram
- northshore_logistics.db, SQLite database file

## Login Details

Admin account:

Username: admin  
Password: admin123  

Manager account:

Username: manager  
Password: manager123  

Warehouse staff account:

Username: staff  
Password: staff123  

## How to Run the Command-Line System

1. Open the project in PyCharm.
2. Open main.py.
3. Run the file.
4. Login using one of the accounts above.
5. Use the menu options to view, update, and manage records.

## How to Run the GUI

1. Open the project in PyCharm.
2. Open gui.py.
3. Run the file.
4. Use the buttons to view shipments, delivery progress, incidents, low inventory, and update delivery status.

## Database Notes

The database contains normalised tables for warehouses, customers, shipments, deliveries, incidents, drivers, vehicles, inventory, users, and audit logs.

Foreign keys link related records together. For example, deliveries link to shipments, drivers, and vehicles. Incidents link to shipments. Audit logs link to users.

## Security Features

Passwords are stored as SHA-256 hashes rather than plain text. User roles control access to sensitive actions. Admin and manager users can update delivery records, while only admin users can view audit logs.

## Version Control

This project uses Git and GitHub. Each major development stage was committed with a clear commit message, including database design, SQL queries, Python functionality, security features, business rules, and the graphical interface.
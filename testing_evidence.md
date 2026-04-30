# Testing Evidence

## T01 Login with valid admin account
Input: admin / admin123  
Expected result: User logs in successfully  
Actual result: User logs in successfully  
Status: Pass

## T02 View shipment records
Input: Menu option 1  
Expected result: System displays shipment records with sender and receiver names  
Actual result: Shipment records displayed correctly  
Status: Pass

## T03 View incident reports
Input: Menu option 2  
Expected result: System displays incident records linked to shipments  
Actual result: Incident reports displayed correctly  
Status: Pass

## T04 Add incident report
Input: Menu option 3  
Expected result: New incident is added to the database  
Actual result: Incident added successfully  
Status: Pass

## T05 View available vehicles
Input: Menu option 4  
Expected result: System displays vehicles marked Available  
Actual result: Available vehicles displayed correctly  
Status: Pass

## T06 View active drivers
Input: Menu option 5  
Expected result: System displays drivers marked Active  
Actual result: Active drivers displayed correctly  
Status: Pass

## T07 Check low inventory
Input: Menu option 6  
Expected result: System shows low stock items or a no low stock message  
Actual result: Correct inventory message displayed  
Status: Pass

## T08 View delivery progress
Input: Menu option 7  
Expected result: System displays delivery status, driver, vehicle and route  
Actual result: Delivery progress displayed correctly  
Status: Pass

## T09 Assign delivery resources
Input: Menu option 8, delivery 1, driver 1, vehicle 1  
Expected result: Active driver and available vehicle are assigned  
Actual result: Assignment completed successfully  
Status: Pass

## T10 Update delivery status
Input: Menu option 9, delivery 1, Delivered  
Expected result: Delivery status updates successfully  
Actual result: Delivery status updated successfully  
Status: Pass

## T11 View audit logs
Input: Menu option 10  
Expected result: Admin can view audit log entries  
Actual result: Audit logs displayed correctly  
Status: Pass

## T12 Manager dashboard
Input: Menu option 11  
Expected result: System displays operational summary report  
Actual result: Dashboard displayed correctly  
Status: Pass

## T13 Vehicle utilisation report
Input: Menu option 12  
Expected result: System displays assigned deliveries per vehicle  
Actual result: Vehicle utilisation displayed correctly  
Status: Pass

## T14 Staff access restriction
Input: staff / staff123, menu option 10  
Expected result: Staff cannot access audit logs  
Actual result: Access denied message displayed  
Status: Pass

## T15 Invalid delivery status
Input: Menu option 9, status = Unknown  
Expected result: System rejects invalid status  
Actual result: Invalid status message displayed  
Status: Pass
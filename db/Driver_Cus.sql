-- Assuming you have a table named 'Deliveries' with the appropriate columns

INSERT INTO Driver_Cus (deliveryId, DriverId, PickupLocId, DropLocId, DeliveryInstruction, Delivered, DeliveryTime, OrderId, DriverEarning)
VALUES
(1, 17, 19, 18, 'Handle with care and deliver promptly.', false, '2023-06-27', 16, 4),
(2, 34, 7, 1, 'Leave at front door, ring bell once.', true, '2023-03-31', 20, 1),
(3, 13, 18, 27, 'Deliver to side entrance, avoid blocking driveway.', true, '2023-09-16', 20, 2),
(4, 6, 6, 19, 'Urgent delivery, please expedite.', true, '2023-08-05', 22, 0),
(5, 9, 2, 6, 'Contact recipient upon arrival for instructions.', true, '2023-05-31', 35, 3),
(6, 40, 24, 23, 'Fragile items inside, handle with extra care.', false, '2023-09-13', 37, 3),
(7, 4, 2, 25, 'No contact delivery, leave in secure location.', false, '2023-03-09', 38, 3),
(8, 14, 15, 26, 'Please deliver to reception, office building.', false, '2023-03-10', 15, 1),
(9, 1, 36, 1, 'Gate code 1234, leave package under the porch.', true, '2022-12-26', 7, 0),
(10, 39, 2, 13, 'Call upon arrival, security gate access needed.', false, '2023-01-14', 17, 4),
(11, 10, 19, 16, 'Deliver to back door, beware of dog.', false, '2023-10-13', 18, 1),
(12, 39, 39, 19, 'Quiet neighborhood, please be discreet during delivery.', false, '2023-11-02', 16, 0),
(13, 2, 11, 9, 'Sensitive package, require signature upon delivery.', false, '2023-07-31', 13, 5),
(14, 14, 25, 34, 'Please double-check address, similar streets nearby.', false, '2023-08-23', 24, 4),
(15, 40, 12, 19, 'If no response, leave with neighbor at #20.', false, '2023-11-30', 2, 2),
(16, 7, 12, 28, 'Deliver before 5 PM, business closes early.', true, '2023-07-18', 12, 2),
(17, 37, 36, 36, 'Ring bell twice, leave on the doorstep if no answer.', true, '2023-11-22', 27, 1),
(18, 16, 36, 10, 'Keep package out of direct sunlight.', true, '2023-01-08', 27, 4),
(19, 22, 2, 12, 'Use side gate, package is for the backyard office.', true, '2023-08-13', 3, 5),
(20, 14, 35, 7, 'Please confirm ID before handing over the package.', false, '2023-02-23', 5, 0),
(21, 2, 33, 26, 'Apartment complex, use intercom for access.', false, '2023-03-23', 2, 3),
(22, 34, 13, 36, 'Please be discreet, surprise gift inside.', false, '2023-07-19', 3, 3),
(23, 5, 28, 24, 'Deliver to the third floor, elevator available.', true, '2023-01-30', 2, 4),
(24, 20, 37, 33, 'Need assistance to carry heavy package upstairs.', false, '2023-04-10', 12, 3),
(25, 7, 2, 21, 'Notify 10 minutes before arrival for gate opening.', false, '2023-01-22', 5, 0),
(26, 34, 30, 17, 'Sensitive medical supplies, handle with care.', true, '2023-07-11', 15, 4),
(27, 14, 7, 34, 'Deliver to office reception, ask for Mr. Johnson.', false, '2023-01-18', 30, 0),
(28, 33, 35, 39, 'Leave in mail room, notify via call after delivery.', false, '2023-03-15', 29, 3),
(29, 6, 40, 25, 'Alert security at gate for entry, deliver to main hall.', false, '2023-11-20', 21, 5),
(30, 35, 8, 39, 'Require immediate delivery, time-sensitive materials enclosed.', true, '2023-01-04', 27, 1),
(31, 30, 38, 23, 'Please call upon arrival, special handling required.', true, '2023-11-19', 38, 5),
(32, 26, 33, 13, 'Residential area, please deliver quietly in the evening.', false, '2023-09-07', 17, 4),
(33, 9, 22, 21, 'Please handle with care, fragile items inside.', false, '2023-05-08', 10, 5),
(34, 35, 24, 25, 'Leave package at the front porch if no one is home.', true, '2023-10-03', 25, 2),
(35, 36, 5, 5, 'Deliver to the office reception on the 3rd floor.', true, '2023-04-14', 3, 3),
(36, 12, 3, 34, 'Call recipient when nearby for instructions.', true, '2023-06-22', 1, 2),
(37, 29, 15, 15, 'Please leave package in the mailbox if it fits.', false, '2023-02-02', 12, 1),
(38, 30, 35, 20, 'Recipient will be waiting in the lobby with ID.', false, '2023-02-06', 4, 5),
(39, 2, 12, 17, 'Delivery to the rear entrance, please knock.', true, '2023-07-18', 26, 4),
(40, 13, 39, 8, 'Recipient is a neighbor, deliver next door at 42 Maple St.', true, '2023-02-17', 6, 0);
-- Assuming you have a table named 'Customers' with the appropriate columns
ALTER TABLE Customer
MODIFY phoneNumber varchar(255);

INSERT INTO Customer (customerID, info, phoneNumber, addressId, paymentMethod, deliveryPreference, loginTime, adminId)
VALUES
(1, 'Consistent and reliable customer with a preference for healthy options.', '661-819-4541', 32, 'mastercard', 'Prefers quick and timely deliveries, especially for dinner orders.', '2023-01-07', 17),
(2, 'Enjoys a wide variety of cuisines, often orders in bulk.', '865-217-0034', 32, 'mastercard', 'Likes family-sized orders with special attention to packaging.', '2022-03-22', 35),
(3, 'Health-conscious, often orders salads and vegan meals.', '485-124-9647', 6, 'mastercard', 'Prefers no-contact delivery and eco-friendly packaging.', '2023-01-26', 30),
(4, 'Frequent orderer of fast food, especially late at night.', '766-188-7697', 15, 'mastercard', 'Requests deliveries to be made directly to the doorstep.', '2022-10-13', 1),
(5, 'Loves experimenting with different international cuisines.', '811-587-9226', 31, 'mastercard', 'Seeks recommendations for new dishes to try with each order.', '2023-05-16', 32),
(6, 'Prefers ordering comfort food, especially during weekends.', '752-874-7519', 1, 'mastercard', 'Likes quick delivery services, especially for surprise gatherings.', '2022-07-07', 17),
(7, 'Enjoys gourmet meals, often orders from high-end restaurants.', '377-752-7270', 20, 'mastercard', 'Requests detailed information about ingredients due to allergies.', '2023-04-02', 7),
(8, 'A fan of traditional dishes, prefers homemade-style cooking.', '983-629-9384', 9, 'mastercard', 'Prefers eco-friendly packaging and sustainable delivery options.', '2022-09-14', 22),
(9, 'Regular customer, often orders light snacks and tea.', '150-357-9083', 14, 'mastercard', 'Enjoys trying new cafes and bakeries for afternoon snacks.', '2023-08-31', 6),
(10, 'Frequent diner of Italian cuisine, loves pasta and pizza.', '993-369-4328', 24, 'mastercard', 'Appreciates quick delivery, often orders for movie nights.', '2023-01-29', 5),
(11, 'Appreciates gourmet coffee and pastries, orders frequently.', '327-714-6771', 2, 'mastercard', 'Prefers early morning deliveries for breakfast items.', '2022-12-03', 5),
(12, 'Enjoys spicy food, often orders from Indian and Thai restaurants.', '333-440-3386', 35, 'mastercard', 'Requests extra condiments and spices with meals.', '2022-10-03', 10),
(13, 'Prefers organic and farm-to-table dining options.', '922-416-9002', 1, 'mastercard', 'Looks for seasonal and fresh produce in orders.', '2023-09-25', 34),
(14, 'Regular customer at local eateries, supports small businesses.', '594-861-4133', 29, 'mastercard', 'Enjoys local cuisine, often orders regional specialties.', '2022-06-13', 8),
(15, 'Health enthusiast, prefers gluten-free and low-carb options.', '651-797-8487', 36, 'mastercard', 'Requests for nutritional information with each meal.', '2023-03-22', 25),
(16, 'A lover of seafood, often experiments with different recipes.', '615-684-3289', 23, 'mastercard', 'Prefers freshly prepared seafood, requests immediate delivery.', '2022-03-13', 15),
(17, 'Enjoys weekend brunches, often orders for the whole family.', '147-633-2068', 25, 'mastercard', 'Requests delivery to align with family brunch time.', '2023-10-02', 16),
(18, 'Student, often orders affordable and quick meals.', '519-209-9479', 1, 'mastercard', 'Looks for budget-friendly options with fast delivery.', '2023-02-13', 30),
(19, 'Busy professional, often orders healthy meals for convenience.', '875-263-3851', 19, 'mastercard', 'Prefers meals that can be eaten on the go.', '2023-10-23', 32),
(20, 'Family-focused, prefers ordering large meals for family gatherings.', '449-585-6246', 32, 'mastercard', 'Looks for family meal deals, appreciates timely delivery.', '2022-09-02', 6),
(21, 'Loves exploring new restaurants and cuisines, very adventurous.', '161-480-7474', 21, 'mastercard', 'Enjoys diverse cuisines, often orders exotic dishes.', '2022-07-22', 22),
(22, 'Active in social events, often orders catering for parties.', '719-335-3976', 16, 'mastercard', 'Requests detailed catering services for special events.', '2023-03-27', 38),
(23, 'Sports enthusiast, prefers high-protein meals post-workout.', '743-800-0930', 3, 'mastercard', 'Orders nutritious, protein-rich meals after gym sessions.', '2022-04-06', 34),
(24, 'Coffee aficionado, loves trying different coffee blends.', '269-256-7366', 10, 'mastercard', 'Prefers morning coffee deliveries from various local cafes.', '2022-11-10', 3),
(25, 'Avid baker, often orders baking supplies and ingredients.', '471-938-8534', 29, 'mastercard', 'Seeks prompt delivery of fresh baking ingredients.', '2023-08-03', 2),
(26, 'Likes to host dinner parties, orders gourmet meals.', '305-618-8412', 24, 'mastercard', 'Prefers elaborate meals for hosting dinner events.', '2022-12-01', 14),
(27, 'Vegetarian, prefers a variety of plant-based options.', '255-946-0489', 4, 'mastercard', 'Requests a range of vegetarian dishes, focusing on taste and variety.', '2023-09-30', 14),
(28, 'Likes casual dining, often orders burgers and fries.', '106-129-9841', 38, 'mastercard', 'Enjoys fast food, prefers quick and casual meal options.', '2023-10-10', 29),
(29, 'Dessert lover, frequently orders cakes and pastries.', '476-428-5100', 10, 'mastercard', 'Often orders sweet treats for family celebrations.', '2023-06-15', 9),
(30, 'Reliable and consistent in service, with a focus on quality.', '401-133-0411', 5, 'mastercard', 'Prioritizes efficient delivery with attention to detail.', '2022-07-30', 26),
(31, 'Known for exceptional attention to customer needs and preferences.', '448-618-9450', 31, 'mastercard', 'Seeks quick, reliable delivery service every time.', '2023-01-06', 17),
(32, 'Values timely and respectful interaction with service providers.', '407-251-9448', 33, 'mastercard', 'Prefers swift and secure delivery methods.', '2022-11-30', 6),
(33, 'Appreciates efficient service with a personal touch.', '407-209-0744', 15, 'mastercard', 'Favors personalized delivery options tailored to schedule.', '2023-11-26', 31),
(34, 'Praises quick resolution of issues and effective communication.', '768-188-9736', 30, 'mastercard', 'Opt for fast and reliable delivery services.', '2023-03-29', 23),
(35, 'Highlights the importance of timely and accurate deliveries.', '295-133-1493', 23, 'mastercard', 'Enjoys expedited delivery with real-time tracking.', '2023-05-20', 17),
(36, 'Commends the blend of speed and safety in deliveries.', '111-267-2106', 32, 'mastercard', 'Values prompt and careful handling of deliveries.', '2023-05-24', 3),
(37, 'Emphasizes the need for respectful and professional service.', '860-600-0872', 13, 'mastercard', 'Prefers a delivery service that ensures product safety.', '2023-03-25', 28),
(38, 'Admires efficiency and attention to detail in service.', '341-405-5605', 21, 'mastercard', 'Chooses delivery options with a focus on punctuality.', '2022-08-17', 8),
(39, 'Values prompt responses and clear communication from service.', '403-576-9780', 1, 'mastercard', 'Looks for speedy and efficient delivery solutions.', '2022-03-21', 15),
(40, 'Appreciates quick service and responsiveness from providers.', '402-257-2874', 35, 'mastercard', 'Prefers fast and reliable delivery, especially for urgent needs.', '2023-07-01', 22);
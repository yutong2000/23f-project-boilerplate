-- Assuming you have a table named 'Drivers' with the appropriate columns
ALTER TABLE Driver
MODIFy phoneNumber Varchar(255);

ALTER TABLE Driver
MODIFy License Varchar(255);

INSERT INTO Driver (DriverID, Info, PhoneNumber, License, Insurance, Availability, AdminID)
VALUES
(1, 'Audi', '449-390-9270', 'WBABV13415J950610', 'Flashspan', true, 13),
(2, 'Nissan', '271-492-7193', 'JTHBB1BA4C2501494', 'Fliptune', true, 2),
(3, 'Saab', '424-278-5561', 'WAULF78K09A262499', 'Wikido', true, 4),
(4, 'Cadillac', '630-918-1117', '1GD21ZCG0CZ347665', 'Blogspan', true, 37),
(5, 'Mitsubishi', '239-914-8225', '5UXFE43568L436354', 'Oyonder', false, 2),
(6, 'Mitsubishi', '630-236-9276', '3VW4T7AT1EM981628', 'Fivechat', true, 5),
(7, 'Mazda', '793-295-8575', '4JGCB2FE1AA046269', 'Yambee', false, 13),
(8, 'BMW', '542-564-2994', '1G6DX6EDXB0236074', 'Skyba', false, 22),
(9, 'Chrysler', '157-105-6358', 'WVGDF9BP3ED190385', 'Meevee', true, 4),
(10, 'Toyota', '362-168-5798', '5UXWX7C56EL417746', 'Vitz', false, 9),
(11, 'Mazda', '560-225-3498', 'WBAFZ9C5XCC306179', 'Buzzster', true, 14),
(12, 'Lamborghini', '335-905-4204', 'WA1CM94L39D197854', 'Twitterlist', false, 38),
(13, 'Chevrolet', '136-722-9107', 'WAUKFAFL6DN100530', 'Fivebridge', true, 12),
(14, 'Chevrolet', '401-486-2780', '5GAKRAKD9FJ626834', 'Edgeblab', true, 9),
(15, 'Ford', '480-830-7545', '3GYFNFEYXBS646178', 'Zoomdog', true, 22),
(16, 'Subaru', '900-647-0554', 'WBA3C1C5XCF398575', 'Zoomlounge', false, 13),
(17, 'Toyota', '201-473-2185', '1GYEK63N22R655957', 'Thoughtbridge', false, 10),
(18, 'GMC', '254-280-1436', 'WDDGF4HB4CF756819', 'Innotype', false, 21),
(19, 'Mazda', '412-941-6008', 'WA1KK78R29A493843', 'Youspan', false, 36),
(20, 'Pontiac', '554-557-2003', '19UUB3F55FA338627', 'JumpXS', false, 26),
(21, 'Oldsmobile', '687-349-2776', '2FMDK3GC6AB637321', 'Zoonder', false, 11),
(22, 'Porsche', '984-889-3751', '2G61S5S36D9220518', 'Fadeo', true, 32),
(23, 'Kia', '854-949-1012', '5XYZG3ABXBG523060', 'Aimbu', false, 35),
(24, 'Toyota', '488-233-5813', 'JTDKTUD30DD820492', 'Agimba', true, 31),
(25, 'Ford', '557-371-3904', 'WAUPL58E64A344979', 'Trilia', true, 33),
(26, 'Volkswagen', '168-122-0337', 'KL4CJDSBXEB102217', 'Jabberbean', true, 24),
(27, 'GMC', '367-740-0932', '2LMHJ5FK2FB243788', 'Jabberstorm', true, 28),
(28, 'Mitsubishi', '973-136-1969', 'WA1BV74L48D079405', 'Skiba', false, 13),
(29, 'Chevrolet', '639-802-7581', 'WAUAFAFL2EN012328', 'Zazio', false, 9),
(30, 'Chevrolet', '819-736-7648', '1FMJU1J5XAE580816', 'Quatz', true, 24),
(31, 'Volkswagen', '242-400-7432', '5FRYD3H93GB284665', 'Agivu', true, 18),
(32, 'Volkswagen', '710-591-1836', 'JN1CV6FE2DM597366', 'Jabbersphere', true, 18),
(33, 'Audi', '871-724-6837', '1GT010CG2CF888077', 'Skipfire', true, 27),
(34, 'Ford', '172-186-5522', '3C6TD5GT3CG765550', 'Oozz', false, 39),
(35, 'Ferrari', '166-960-3113', 'WAUJT68E34A267029', 'Skinder', true, 12),
(36, 'Bentley', '180-677-7647', 'YV1612FH5D2245512', 'Jazzy', true, 3),
(37, 'Chevrolet', '402-439-1950', 'WBAFR7C55CC323119', 'Trupe', true, 29),
(38, 'Ford', '770-635-5322', '1FTEW1CW7AK428645', 'Skiba', true, 31),
(39, 'Toyota', '825-707-6633', 'WAUNF78P68A213343', 'Ailane', true, 19),
(40, 'Mercedes-Benz', '115-993-8783', 'JTHCL5EFXF5841431', 'Kayveo', true, 40);

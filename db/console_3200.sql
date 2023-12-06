CREATE Database if not exists GroupWork3200;
USE GroupWork3200;

CREATE TABLE if not exists Location
(
    locationId int auto_increment,
    zip        varchar(5)  not null, -- Zip code of an address
    state      VARCHAR(20) not null, -- Whole name of a State
    city       varchar(25) not null, -- Whole name of a city
    street     varchar(50) not null, -- street
    apt        varchar(15),          -- optional

    PRIMARY KEY (LocationId)
);

CREATE TABLE if not exists Admin
(
    AdminId        int,
    Performance    varchar(200), -- evaluate the performance of an admin
    Rating         double,       -- rating of an admin
    PhoneNumber    varchar(15) not null unique,
    TransactionFee double,
    SupportPolicy  text,
    LegalStatus    boolean,

    PRIMARY KEY (AdminId)
);


CREATE TABLE if not exists Admin_FeedBack
(
    FeedBackId int auto_increment,
    AdminId    int not null, -- which admin' feedback
    FeedBack   VARCHAR(200), -- feedback content

    PRIMARY KEY (FeedBackId),
    CONSTRAINT FOREIGN KEY (AdminId) REFERENCES Admin (AdminId)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE if not exists Restaurant
(
    restaurantID int,
    name         varchar(30) NOT NULL,        -- Restaurant name
    phoneNumber  int         NOT NULL UNIQUE, -- Restaurant phone number
    performance  varchar(200),                -- evaluate the performance of a Restaurant
    sale         double      NOT NULL,        -- total sale
    revenue      double      NOT NULL,        -- total revenue
    locationId   int,                         -- Restaurant location
    adminId      int,                         -- Restaurant's admin

    PRIMARY KEY (restaurantID),
    CONSTRAINT FOREIGN KEY (locationId) REFERENCES Location (locationId)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT FOREIGN KEY (adminId) REFERENCES Admin (adminId)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE if not exists FoodItem_Ava_P
(
    FoodId       int,
    FoodName     VARCHAR(50) not null, -- food's name
    availability boolean     not null, -- is the food available
    Price        double      not null, -- the price of food

    PRIMARY KEY (FoodId)
);

CREATE TABLE if not exists Restaurant_foodItem
(
    RestaurantId int,
    FoodItem     int,

    CONSTRAINT FOREIGN KEY (RestaurantId) REFERENCES Restaurant (restaurantID)
        ON UPDATE Cascade ON DELETE CASCADE,
    CONSTRAINT FOREIGN KEY (FoodItem) REFERENCES FoodItem_Ava_P (FoodId)
        ON UPDATE Cascade ON DELETE CASCADE
);



CREATE TABLE if not exists Driver
(
    DriverId     int,
    Info         varchar(100),
    PhoneNumber  varchar(15) not null unique,
    License      varchar(16) not null,
    Insurance    varchar(25),
    Availability boolean     not null,
    AdminId      int,

    PRIMARY KEY (DriverId),
    CONSTRAINT FOREIGN KEY (AdminId) REFERENCES Admin (AdminId)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE if not exists Driver_VehicleId
(
    VehicleId int,
    DriverId  int not null,

    PRIMARY KEY (VehicleId),
    CONSTRAINT FOREIGN KEY (DriverId) REFERENCES Driver (DriverId)
);



CREATE TABLE IF NOT EXISTS Customer
(
    customerID         int,
    info               varchar(100) NOT NULL,
    phoneNumber        int          NOT NULL,
    addressId          int          NOT NULL,
    paymentMethod      varchar(20),
    deliveryPreference varchar(100),
    loginTime          DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    adminId            int          not null,

    PRIMARY KEY (customerID),
    CONSTRAINT FOREIGN KEY (addressId) REFERENCES Location (locationId)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT FOREIGN KEY (adminId) REFERENCES Admin (adminId)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE if not exists Customer_FavoriteFood
(
    CustomerId int not null,
    FoodId     int not null,

    CONSTRAINT FOREIGN KEY (CustomerId) REFERENCES Customer (customerID)
        ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT FOREIGN KEY (FoodId) REFERENCES FoodItem_Ava_P (FoodId)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE if not exists Customer_FavoriteRestaurant
(
    CustomerId   int not null,
    RestaurantId int not null,

    CONSTRAINT FOREIGN KEY (CustomerId) REFERENCES Customer (customerID)
        ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT FOREIGN KEY (RestaurantId) REFERENCES Restaurant (RestaurantId)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE if not exists CardNumber
(
    CardNumber VARCHAR(20),
    ExpireDate Date       not null,
    SecCode    varchar(3) not null,
    CustomerId int,

    PRIMARY KEY (CardNumber),

    CONSTRAINT FOREIGN KEY (CustomerId) REFERENCES Customer (customerID)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE if not exists OrdersInfo
(
    OrderId         int,
    CustomerId      int    not null, -- customer
    PaymentMethod   varchar(50),
    TransactionDate DATETIME default CURRENT_TIMESTAMP,

    Cost            double not null, -- The cost of this order
    Tax             double,          -- The tax of this order

    PRIMARY KEY (OrderId)
);

CREATE TABLE if not exists Order_Foods
(
    OrderId int,
    FoodId  int,

    CONSTRAINT FOREIGN KEY (OrderId) REFERENCES OrdersInfo (OrderId)
        ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT FOREIGN KEY (FoodId) REFERENCES FoodItem_Ava_P (FoodId)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE if not exists Driver_Cus -- delivery details
(
    deliveryId          int,
    DriverId            int    not null,                    -- driver


    PickupLocId         int    not null,                    -- restaurant
    DropLocId           int    not null,                    -- customer address
    DeliveryInstruction VARCHAR(100),                       -- detail requirements of a delivery

    Delivered           boolean  default false,             -- whether a order is delivered
    DeliveryTime        DATETIME default CURRENT_TIMESTAMP, -- the time of a delivery

    OrderId             int    not null,                    -- link to order details

    DriverEarning       double not null,                    -- how much driver earns from this delivery


    PRIMARY KEY (deliveryId),
    CONSTRAINT FOREIGN KEY (DriverId) REFERENCES Driver (DriverId)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT FOREIGN KEY (PickupLocId) REFERENCES Location (locationId)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT FOREIGN KEY (DropLocId) REFERENCES Location (locationId)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT FOREIGN KEY (OrderId) REFERENCES OrdersInfo (OrderId)
        ON UPDATE CASCADE ON DELETE RESTRICT
);


INSERT INTO Location (zip, state, city, street, apt)
VALUES ('02120', 'Massachusetts', 'Boston', 'Curry student center ', 'apt 1'),
       ('10001', 'New York', 'New York', 'New York Street', 'apt 2'),
       ('00000', 'Massachusetts', 'Boston', 'NEU dorm', 'apt 3');

INSERT INTO Admin (adminid, performance, rating, phonenumber, transactionfee, supportpolicy, legalstatus)
VALUES (1, 'Good performance', 10.0, '1234567890', 2.0, 'support policy of admin 1', true),
       (2, 'bad performance', 0.0, '0987654321', 2.0, 'support policy of admin 2', false);

INSERT INTO Admin_FeedBack (adminid, feedback)
VALUES (1, 'Good service! Admin 1!'),
       (2, 'Bad service, Admin 2.');

INSERT INTO Restaurant (restaurantID, name, phoneNumber, performance, sale, revenue, locationId, adminId)
VALUES (10, 'St*rbucks', '1231231234', 'Good performance St*rbucks!', 1000, 500, 1, 1),
       (20, 'P1zza', '2345', 'Normal performance P1zza.', 300, 200, 2, 1);

INSERT INTO FoodItem_Ava_P(foodid, foodname, availability, price)
VALUES (101, 'iced coffee', true, 5.0),
       (102, 'iced tea', false, 3.0),
       (201, 'cheese pizza', true, 2.0);

INSERT INTO Restaurant_foodItem (RestaurantId, FoodItem)
VALUES (10, 101),
       (10, 102),
       (20, 201);

INSERT INTO Driver (DriverId, Info, PhoneNumber, License, Insurance, Availability, AdminId)
VALUES (1, 'Driver 1 age 30.', '0009998888', 'A000-222-4444', 'Driver1s insurance', true, 1),
       (2, 'Driver 2 fast in delivery.', '1110003333', 'B111-3333-555', 'Driver2s insurance', false, 1);

INSERT INTO Driver_VehicleId (VehicleId, DriverId)
VALUES (1, 1),
       (2, 2);

INSERT INTO Customer (customerID, info, phoneNumber, addressId, paymentMethod, deliveryPreference, adminId)
VALUES (0, 'first customer', '1111111111', 3, 'Credit card', 'Put at the front desk.', 1),
       (1, 'second customer', '1111111111', 3, 'Paypal', 'Call me when arrived.', 1);

INSERT INTO Customer_FavoriteFood (customerid, foodid)
VALUES (0, 101),
       (1, 102),
       (1, 101);

INSERT INTO Customer_FavoriteRestaurant(customerid, restaurantid)
VALUES (0, 10),
       (1, 10),
       (1, 20);

INSERT INTO CardNumber(cardnumber, expiredate, seccode, customerid)
VALUES ('1234567890', '2027-11-26', '123', 0),
       ('0987654321', '2025-11-29', '321', 0),
       ('1029384756', '2024-10-26', '345', 1);

INSERT INTO OrdersInfo(orderid, customerid, paymentmethod, cost, tax)
VALUES (0, 0, 'credit card : 1234567890', 5.0, 1.0),
       (1, 0, 'Paypal', 8.0, 0.5),
       (2, 1, 'Paypal', 50.0, 3.2);

INSERT INTO Order_Foods(orderid, foodid)
VALUES (0, 101),
       (0, 101),
       (1, 101),
       (1, 102);


INSERT INTO Driver_Cus (deliveryId, DriverId, PickupLocId, DropLocId, DeliveryInstruction, Delivered,
                        OrderId, DriverEarning)
VALUES (0, 1, 1, 3, 'OK', false, 0, 3.0),
       (1, 2, 1, 3, 'OK', true, 1, 2.0);
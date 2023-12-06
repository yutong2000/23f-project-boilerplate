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
    phoneNumber  varchar(25)        NOT NULL UNIQUE, -- Restaurant phone number
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
    PhoneNumber  varchar(25) not null unique,
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
    phoneNumber        varchar(25)          NOT NULL,
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
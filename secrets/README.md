# MySQL + Flask Boilerplate Project

This repo contains a boilerplate setup for spinning up 3 Docker containers: 
1. A MySQL 8 container for obvious reasons
1. A Python Flask container to implement a REST API
1. A Local AppSmith Server

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 



### Project Overview
This app is designed to manage customer orders, stock orders, and ingredient production across multiple boba stores organized by region. An app was created via AppSmith - it contains two sample pages for use from a barista's standpoint as well as a manager's standpoint. 


## This repository contains two pages that interact with the [HungryHuh Database](https://github.com/yutong2000/23f-project-boilerplate)


## Pages
There are 3 main pages, Customer, Restaurant, and Admin.

# Customer Page
Inside customer page, we have order, order history, addCustomer.

# Admin Page
Inside admin page, we have add customer, delete customer, update restaurant, add restaurant, delete restaurant, add driver, delete driver.

# Restaurant Page
Inside restaurant page, we have add new food, update resaurant.

##### You can view our presentation through the link below 
##### (https://youtu.be/0DrnmG7pzBI)

##### You can view the application using the link below
##### https://github.com/nhzq-1010/AppSmith.git

##### You can vie our git repo using the link below
##### https://github.com/yutong2000/23f-project-boilerplate.git


##### Thank you!
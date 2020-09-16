[![Build Status](https://travis-ci.org/Nkoli/food_vendor_app.svg?branch=staging)](https://travis-ci.org/Nkoli/food_vendor_app)
[![Coverage Status](https://coveralls.io/repos/github/Nkoli/food_vendor_app/badge.svg)](https://coveralls.io/github/Nkoli/food_vendor_app)

# FOOD_VENDOR

Food Vendor is a backend based restaurant-like application where vendors can list their meals and/or menus and customers can place an order.

## Development

Restaurant API built with [Django](https://www.djangoproject.com/start/) and [Django Rest Framework](https://www.django-rest-framework.org/)

## Tech

Food Vendor is written in Python3 and Django 3.0.9

## Installation

- Install Python3 on your machine. If it's already preinstalled, upgrade to [Python3](https://www.python.org/download/releases/3.0/).

- Clone the repository `$ git clone https://github.com/Nkoli/food_vendor.git`

- Install the required dependencies with `$ pip install -r requirements.txt`

- Create a `.env file` in your root directory using the .env.example file as a guide.

## Usage

- Start the application `$ python manage.py runserver`

- Use [Postman](https://www.postman.com/downloads/) to consume the available endpoints.

- A user can:
- Create an account.
- Log into their account.
- Log out
- If the user is a vendor, they can:
  - Add their business name to their profile.
  - Create menus
  - Update menu
  - Delete menu
  - Create meals
  - Update meal
  - Delete meal
  - Determine how many times they want a menu to occur every week.
  - Check and update customer order status.
- If the user is a customer, they can:
  - View all available meals.
  - View all available menus.
  - Place an order for a meal or several meals.
  - Place an order for a menu if they prefe.
  - Check their order status.
  - Cancel an order

## Endpoints

| Request type |    Endpoint    |             Action |
| ------------ | :------------: | -----------------: |
| POST         | /auth/register |      Create a user |
| POST         |  /auth/login/  |      Log a user in |
| POST         | /auth/logout/  |    Sign a user out |
| POST         |    /meals/     |      Create a meal |
| GET          |    /meals/     |      Get all meals |
| GET          |   /meals/:id   |  Get a single meal |
| PATCH        |   /meals/:id   |      Update a meal |
| DELETE       |   /meals/:id   |      Delete a meal |
| POST         |    /menus/     |      Create a menu |
| GET          |    /menus/     |      Get all menus |
| GET          |   /menus/:id   |  Get a single meal |
| PATCH        |   /menus/:id   |      Update a menu |
| DELETE       |   /menus/:id   |      Delete a menu |
| POST         |    /orders/    |    Create an order |
| GET          |    /orders/    |     Get all orders |
| GET          |  /orders/:id   | Get a single order |
| PATCH        |  /orders/:id   |    Update an order |
| DELETE       |  /orders/:id   |    Delete an order |

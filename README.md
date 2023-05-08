# City Handbook

City Handbook is the back-end of a web application developed using Django and Django Rest Framework. It allows users to browse information about various establishments in different cities. It provides an API for developers to access this information programmatically and an admin panel for managing the content.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Django 3.2 or higher

### Installation

1. Clone the repository
   ```
   git clone https://github.com/qwerty2053/city_handbook.git
   ```
2. Create a virtual environment and activate it
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the dependencies
   ```
   pip install -r requirements.txt
   ```
4. Create the database
   ```
   python manage.py migrate
   ```
5. Run the development server
   ```
   python manage.py runserver
   ```
6. Access the API Root at `http://localhost:8000/api`

### Usage

The admin panel provides the following features:

- Add, edit, and delete establishments, categories, cities
- Add, edit, and delete images, contact information for each establishment

### API Documentation

The API provides the following endpoints:

- `/api/category_list/`: Retrieve a list of all categories
- `/api/city_list/`: Retrieve a list of all cities
- `/api/est_list/`: Retrieve a list of all establishments (not all fields)
- `/api/category/{id}/`: Retrieve a list of all establishments by category
- `/api/city/{id}/`: Retrieve a list of all establishments by city
- `/api/est/{id}/`: Retrieve a single establishment by ID
- `/api/search/title/{title}/`: Retrieve a list of establishments with a title field that matches the {title}
- `/api/search/address/{address}/`: Retrieve a list of establishments with an address field that matches the {address}

The API uses the JSON format for data exchange.

### Admin Panel

The admin panel can be accessed at `/admin/`. You will need to create a superuser to access it:
```
python manage.py createsuperuser
```
Once you have created a superuser, you can log in to the admin panel and manage the establishments data.

E-commerce Product API
This project is an E-commerce Product API built using Django and Django REST Framework. It allows users to manage products on an e-commerce platform with functionalities for creating, reading, updating, and deleting products. The API also provides user authentication, product search, and filtering features. This is a backend API suitable for e-commerce applications that require product management.

Features
Product Management (CRUD)
Create, Read, Update, and Delete (CRUD) operations for products.
Products have attributes such as:
Name
Description
Price
Category
Stock Quantity
Image URL
Created Date
Stock Quantity is validated for required fields like Name, Price, and Stock.
User Management (CRUD)
Users can:
Register
Log in
Manage products (authenticated users only).
Product Search and Filtering
Search products by:
Name (with partial matching support).
Category.
Filter products by:
Price Range
Stock Availability
Pagination for product listings to improve performance.
Authentication
Token-based authentication using JWT (JSON Web Tokens) for securing the API.
Authenticated users can perform CRUD operations.
API Documentation
API follows RESTful principles:
GET for reading data.
POST for creating new data.
PUT/PATCH for updating data.
DELETE for deleting data.
Technology Stack
Backend: Django, Django REST Framework (DRF)
Database: PostgreSQL (or any other relational database)
Authentication: Token-based authentication with JWT (optional)
Deployment: Heroku or PythonAnywhere
Installation
Clone the repository:
bash

git clone https://github.com/yourusername/ecommerce_product_api.git
cd ecommerce_product_api
Create and activate a virtual environment:
bash

python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
Install the dependencies:
bash

pip install -r requirements.txt
Run the migrations:
bash

python manage.py makemigrations
python manage.py migrate
Create a superuser (for admin access):
bash

python manage.py createsuperuser
Run the development server:
bash

python manage.py runserver
The API will be accessible at http://127.0.0.1:8000/.

API Endpoints
Product Endpoints
GET /api/products/ – Retrieve a list of products.
GET /api/products/<id>/ – Retrieve product details by ID.
POST /api/products/ – Create a new product (Authenticated).
PUT/PATCH /api/products/<id>/ – Update a product by ID (Authenticated).
DELETE /api/products/<id>/ – Delete a product by ID (Authenticated).
User Authentication Endpoints
POST /api/auth/register/ – Register a new user.
POST /api/auth/login/ – Log in to obtain a token.
POST /api/auth/logout/ – Log out a user.
Search and Filtering Endpoints
GET /api/products/?search=<product_name> – Search products by name.
GET /api/products/?category=<category_name> – Filter products by category.
GET /api/products/?price_min=<min_price>&price_max=<max_price> – Filter products by price range.
GET /api/products/?in_stock=True – Filter products by stock availability.
Running Tests
To run the tests, use:

bash
Copy code
python manage.py test
Postman Collection
You can test the API using Postman. Import the provided Postman collection to test various endpoints.

Deployment
To deploy the API, follow these steps:

Heroku Deployment:

Create a Heroku account and install the Heroku CLI.
Login to Heroku:
bash

heroku login
Create a new Heroku app:
bash

heroku create your-app-name
Push the project to Heroku:
bash

git push heroku main
Set up environment variables (e.g., DATABASE_URL, SECRET_KEY) in the Heroku dashboard.
PythonAnywhere Deployment:

Create a PythonAnywhere account.
Follow the official documentation to deploy your Django project.
Challenges Faced
Understanding Django ORM: Designing relationships between products, categories, and users.
User Authentication: Setting up token-based authentication and restricting access to product management endpoints.
Search and Filtering: Implementing scalable search functionality with pagination and filters.
Future Enhancements
Implement order management.
Integrate payment gateway.
Add product reviews and ratings.
License
This project is licensed under the MIT License.

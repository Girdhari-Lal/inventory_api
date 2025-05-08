# 📂 Product Inventory Management System

This Django-based Product Inventory Management System provides a comprehensive backend API to manage products, their variants, and associated metadata such as brands, categories, units of measure, and attributes.

---

## 📂 Libraries and Technologies Used
-  Django: Framework for backend development.
-  Django Rest Framework: For building the API.
-  DRF Simple JWT: For generating JWT tokens.
-  Django Authentication: For authenticating users.

## 📂 Models Overview

-  Brand – Manufacturer or label of a product
-  Unit – Measurement unit for products (kg, liter, etc.)
-  Category – Classification of products (e.g., Electronics, Clothing)
-  Attribute – Characteristics like color, size
-  AttributeValue – Values for an attribute (e.g., Red, XL)
-  Product – Core product entity with support for combos and services
-  ProductAttribute – Represents variants of a product (SKU, stock, price)
-  User – Represents a user of the system (can be a customer, admin, etc.). Handles authentication and profile  management.
-  UserManager – Custom manager for the User model, providing user creation and authentication methods.



## 🚀 Endpoints Overview

### Brand Endpoints

- **GET http://127.0.0.1:8000/products/**: List all brands
- **POST http://127.0.0.1:8000/products/**: Create a new brand
- **GET http://127.0.0.1:8000/products/{id}/**: Retrieve a single brand by ID
- **PUT http://127.0.0.1:8000/products/{id}/**: Update a brand by ID
- **DELETE http://127.0.0.1:8000/products/{id}/**: Delete a brand by ID

### Unit Endpoints

- **GET http://127.0.0.1:8000/units/**: List all units
- **POST http://127.0.0.1:8000/units/**: Create a new unit
- **GET http://127.0.0.1:8000/units/{id}/**: Retrieve a single unit by ID
- **PUT http://127.0.0.1:8000/units/{id}/**: Update a unit by ID
- **DELETE http://127.0.0.1:8000/units/{id}/**: Delete a unit by ID

### Category Endpoints

- **GET http://127.0.0.1:8000/categories/**: List all categories
- **POST http://127.0.0.1:8000/categories/**: Create a new category
- **GET http://127.0.0.1:8000/categories/{id}/**: Retrieve a single category by ID
- **PUT http://127.0.0.1:8000/categories/{id}/**: Update a category by ID
- **DELETE http://127.0.0.1:8000/categories/{id}/**: Delete a category by ID

### Product Endpoints

- **GET http://127.0.0.1:8000/products/**: List all products
- **POST http://127.0.0.1:8000/products/**: Create a new product
- **GET http://127.0.0.1:8000/products/{id}/**: Retrieve a single product by ID
- **PUT http://127.0.0.1:8000/products/{id}/**: Update a product by ID
- **DELETE http://127.0.0.1:8000/products/{id}/**: Delete a product by ID

### Attribute Endpoints

- **GET http://127.0.0.1:8000/attributes/**: List all attributes
- **POST http://127.0.0.1:8000/attributes/**: Create a new attribute
- **GET http://127.0.0.1:8000/attributes/{id}/**: Retrieve a single attribute by ID
- **PUT http://127.0.0.1:8000/attributes/{id}/**: Update an attribute by ID
- **DELETE http://127.0.0.1:8000/attributes/{id}/**: Delete an attribute by ID

### Attribute Value Endpoints

- **GET http://127.0.0.1:8000/attribute-values/**: List all attribute values
- **POST http://127.0.0.1:8000/attribute-values/**: Create a new attribute value
- **GET http://127.0.0.1:8000/attribute-values/{id}/**: Retrieve a single attribute value by ID
- **PUT http://127.0.0.1:8000/attribute-values/{id}/**: Update an attribute value by ID
- **DELETE http://127.0.0.1:8000/attribute-values/{id}/**: Delete an attribute value by ID

### Product Attribute Endpoints

- **GET http://127.0.0.1:8000/product-attributes/**: List all product attributes
- **POST http://127.0.0.1:8000/product-attributes/**: Create a new product attribute
- **GET http://127.0.0.1:8000/product-attributes/{id}/**: Retrieve a single product attribute by ID
- **PUT http://127.0.0.1:8000/product-attributes/{id}/**: Update a product attribute by ID
- **DELETE http://127.0.0.1:8000/product-attributes/{id}/**: Delete a product attribute by ID

### User Endpoints
- **POST http://127.0.0.1:8000/register/**: Register a new user.
- **POST http://127.0.0.1:8000/login/**: Log in to an existing user account and get the JWT tokens.
- **GET http://127.0.0.1:8000/user/**: Retrieve the authenticated user's profile information.
- **PUT http://127.0.0.1:8000/user/**: Update user's profile information.
---

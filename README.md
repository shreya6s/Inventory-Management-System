# 📦 Inventory Management System

## Project Description

We created an Inventory Management System using HTML, CSS, Flask, and MySQL. This system allows users to add, remove, and update stocks, as well as view product, provider, and customer information. It includes a login page for authentication, ensuring secure access. The database is managed using XAMPP.

## Features

- ➕ **Add Stock**: Easily add new products to the inventory.
- ➖ **Remove Stock**: Remove products from the inventory when they are no longer available.
- 🔄 **Update Stock**: Update the quantity or details of existing products.
- 👁️ **View Information**: View detailed information about products, providers, and customers.
- 🔒 **Login Page**: Secure login page for user authentication.

## Technologies Used

- **Frontend**: HTML, CSS
- **Backend**: Flask (Python)
- **Database**: MySQL (managed using XAMPP)

## Prerequisites

- 🐍 [Python](https://www.python.org/downloads/)
- 🛠️ [XAMPP](https://www.apachefriends.org/index.html)
- 📦 Flask: `pip install flask`
- 🗄️ MySQL Connector: `pip install mysql-connector-python`

## Installation and Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/shreya6s/inventory-management-system.git
    cd inventory-management-system
    ```

2. **Set Up XAMPP**:
   - Download and install XAMPP from the [official website](https://www.apachefriends.org/index.html).
   - Start the Apache and MySQL modules from the XAMPP control panel.

3. **Configure the Database**:
   - Open your web browser and go to `http://localhost/phpmyadmin`.
   - Create a new database named `inventory_db`.
   - Import the database schema from the provided SQL file in the repository:
     ```sql
     -- path: /path/to/your/sqlfile.sql
     ```

4. **Set Up Flask Application**:
   - Create a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate   # On Windows use `venv\Scripts\activate`
     ```

5. **Run the Application**:
   - Start the Flask server:
     ```bash
     python app.py
     ```
   - Open your web browser and go to `http://localhost:5000` to access the inventory management system.

## Usage

- 🏠 **Dashboard**: View overall inventory status.
- ➕ **Add Stock**: Use the form to add new products.
- ➖ **Remove Stock**: Remove products that are no longer available.
- 🔄 **Update Stock**: Modify the details of existing products.
- 👁️ **View Information**: Access detailed views of products, providers, and customers.
- 🔒 **Login**: Authenticate yourself to use the system securely.

## Screenshots

### Home Page
![Home Page](https://github.com/shreya6s/Inventory-Management-System/assets/120666315/1f1680de-520e-43f0-bbe6-a1cb311a68fc)

### Product Table
![Product Table](https://github.com/shreya6s/Inventory-Management-System/assets/120666315/417e77e6-ffa9-4ffc-bfd9-e5fa1e470483)

### Update Stock
![Update Stock](https://github.com/shreya6s/Inventory-Management-System/assets/120666315/dea582b8-c375-4127-a524-0a6ffed01ffb)

### Customer Table
![Customer Table](https://github.com/shreya6s/Inventory-Management-System/assets/120666315/099effa2-48f8-4fb5-b096-1c2026ca749f)


## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.



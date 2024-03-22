# Invoice Management API

This is a Django Rest Framework (DRF) based API for managing invoices and their details.

## Features

- Create, retrieve, update, and delete invoices.
- Create, retrieve, update, and delete invoice details.
- Associate invoice details with invoices.
- Supports CRUD operations via RESTful endpoints.
- Comprehensive test suite for all API endpoints.

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/yourusername/invoice-management-api.git
    ```

2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```
    python manage.py migrate
    ```

4. Run the development server:

    ```
    python manage.py runserver
    ```

## Usage

### Endpoints

- **`/invoices/`**
  - `GET`: Retrieve a list of all invoices or create a new invoice.
- **`/invoices/<int:pk>/`**
  - `GET`: Retrieve details of a specific invoice.
  - `PUT`: Update details of a specific invoice.
  - `DELETE`: Delete a specific invoice.
- **`/invoicedetails/`**
  - `GET`: Retrieve a list of all invoice details or create a new invoice detail.
- **`/invoicedetails/<int:pk>/`**
  - `GET`: Retrieve details of a specific invoice detail.
  - `PUT`: Update details of a specific invoice detail.
  - `DELETE`: Delete a specific invoice detail.

#### Create Invoice

```json
{
  "date": "YYYY-MM-DD",
  "customer_name": "Customer Name"
}

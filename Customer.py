from datetime import datetime
import csv
import json

class Customer:
    """A class to represent a customer."""
    
    def __init__(self, id, name, email, phone_number, date_of_birth, address):
        """Initialize a customer object with provided attributes."""
        if not isinstance(id, int):
            raise TypeError("ID must be an integer.")
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not isinstance(email, str) or "@" not in email:
            raise TypeError("Email must be a valid string.")
        if not isinstance(phone_number, str):
            raise TypeError("Phone number must be a string.")
        try:
            datetime.strptime(date_of_birth, '%Y-%m-%d')
        except ValueError:
            raise TypeError("Date of birth must be a string in the format YYYY-MM-DD.")
        if not isinstance(address, str):
            raise TypeError("Address must be a string.")
        
        self.id = id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.address = address
    
    def __repr__(self):
        """Return a string representation of the customer object."""
        return f"Customer(id={self.id}, name={self.name}, email={self.email}, phone_number={self.phone_number}, date_of_birth={self.date_of_birth}, address={self.address})"
    
    def calculate_age(self):
        """Calculate the age of the customer based on date of birth."""
        dob = datetime.strptime(self.date_of_birth, '%Y-%m-%d')
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phone_number

    def get_address(self):
        return self.address

    def set_name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string.")
        self.name = new_name

    def set_email(self, new_email):
        if not isinstance(new_email, str) or "@" not in new_email:
            raise TypeError("Email must be a valid string.")
        self.email = new_email

    def set_phone_number(self, new_phone_number):
        if not isinstance(new_phone_number, str):
            raise TypeError("Phone number must be a string.")
        self.phone_number = new_phone_number

    def set_address(self, new_address):
        if not isinstance(new_address, str):
            raise TypeError("Address must be a string.")
        self.address = new_address

class CustomerManager:
    """A class to manage customers."""
    
    def __init__(self):
        """Initialize the CustomerManager."""
        self.customers = []
    
    def add_customer(self, customer):
        """Add a customer to the list of customers."""
        if not isinstance(customer, Customer):
            raise TypeError("The 'customer' parameter must be an instance of the Customer class.")
        
        self.customers.append(customer)
    
    def remove_customer(self, customer):
        """Remove a customer from the list of customers."""
        if not isinstance(customer, Customer):
            raise TypeError("The 'customer' parameter must be an instance of the Customer class.")
        
        try:
            self.customers.remove(customer)
        except ValueError:
            raise ValueError("Customer not found.")
    
    def get_customers_by_age_range(self, min_age, max_age):
        """Retrieve customers within the specified age range."""
        filtered_customers = [customer for customer in self.customers if min_age <= customer.calculate_age() <= max_age]
        return filtered_customers
    
    def get_customers_by_address(self, address):
        """Retrieve customers with matching address."""
        filtered_customers = [customer for customer in self.customers if customer.address == address]
        return filtered_customers
    
    def export_data(self, filename, format='csv', delimiter=','):
        """Export customer data to a file."""
        try:
            if format == 'csv':
                with open(filename, 'w', newline='') as csvfile:
                    fieldnames = ['id', 'name', 'email', 'phone_number', 'date_of_birth', 'address']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=delimiter)
                    writer.writeheader()
                    for customer in self.customers:
                        writer.writerow({
                            'id': customer.id,
                            'name': customer.name,
                            'email': customer.email,
                            'phone_number': customer.phone_number,
                            'date_of_birth': customer.date_of_birth,
                            'address': customer.address
                        })
            elif format == 'json':
                with open(filename, 'w') as jsonfile:
                    data = [{'id': customer.id,
                             'name': customer.name,
                             'email': customer.email,
                             'phone_number': customer.phone_number,
                             'date_of_birth': customer.date_of_birth,
                             'address': customer.address} for customer in self.customers]
                    json.dump(data, jsonfile, indent=4)
            else:
                raise ValueError("Unsupported format. Use 'csv' or 'json'.")
        except Exception as e:
            print(f"Error exporting data: {e}")

def main():
    manager = CustomerManager()

    while True:
        try:
            id = int(input("Enter customer ID: "))
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            phone_number = input("Enter customer phone number: ")
            date_of_birth = input("Enter customer date of birth (YYYY-MM-DD): ")
            address = input("Enter customer address: ")
            
            customer = Customer(id, name, email, phone_number, date_of_birth, address)
            manager.add_customer(customer)
            
            choice = input("Do you want to add another customer? (yes/no): ")
            if choice.lower() != 'yes':
                break
        except Exception as e:
            print(f"Error: {e}")
    
    while True:
        try:
            choice = input("Do you want to export customer data to a file? (yes/no): ")
            if choice.lower() == 'yes':
                filename = input("Enter filename to export customer data: ")
                format = input("Enter export format (csv/json): ")
                manager.export_data(filename, format=format)
            break
        except Exception as e:
            print(f"Error: {e}")

    while True:
        try:
            choice = input("Do you want to retrieve customers within a certain age range? (yes/no): ")
            if choice.lower() == 'yes':
                min_age = int(input("Enter minimum age: "))
                max_age = int(input("Enter maximum age: "))
                customers_in_range = manager.get_customers_by_age_range(min_age, max_age)
                print("Customers within the age range:")
                for customer in customers_in_range:
                    print(customer)
            break
        except Exception as e:
            print(f"Error: {e}")

    while True:
        try:
            choice = input("Do you want to retrieve customers with a matching address? (yes/no): ")
            if choice.lower() == 'yes':
                address = input("Enter address to search customers: ")
                customers_with_address = manager.get_customers_by_address(address)
                print("Customers with matching address:")
                for customer in customers_with_address:
                    print(customer)
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

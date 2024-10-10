# Advanced CRM System

This repository contains the code for the **Advanced Customer Relationship Management (CRM) System**, a Python-based application designed for managing customer data efficiently. The system provides robust functionalities for adding, updating, removing, and filtering customers, making it a valuable tool for organizations looking to streamline their customer management processes.

## Project Overview

The CRM system is designed for a multinational corporation to manage customer data effectively. The system provides comprehensive customer management functionalities, including the ability to add, remove, and filter customers based on various criteria. The application is built using **Python 3** and follows object-oriented programming (OOP) principles with a focus on best practices and design patterns.

## Features

- **Customer Class:**
  - Properties: `id`, `name`, `email`, `phone_number`, `date_of_birth`, `address`
  - Getters: `getId()`, `getName()`, `getEmail()`, `getPhoneNumber()`, `getAddress()`
  - Setters: `setName()`, `setEmail()`, `setPhoneNumber()`, `setAddress()`
  - Methods: 
    - `__repr__()`: Displays detailed customer information.
    - `calculate_age()`: Calculates the age of the customer based on their date of birth.

- **CustomerManager Class:**
  - Manages a list of `Customer` objects.
  - Add or remove customers from the system.
  - Filter customers by age range or address.
  - Export customer data to a CSV file (JSON export also available).

- **Exception Handling:**
  - Robust error handling for invalid inputs and file operations.
  - User-friendly error messages.

- **Unit Tests:**
  - Comprehensive unit tests to ensure the correctness of the system.
  - Tests cover various scenarios, including edge cases for customer data management.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.
- Required libraries can be installed using the following command:

## Best Practices Implemented
Object-Oriented Design: The system follows OOP principles, allowing for modular, reusable, and maintainable code.
Error Handling: Includes exception handling to prevent system crashes and provide clear error messages.
Code Readability: Adheres to PEP 8 coding standards for clean, readable, and maintainable code.

## Future Enhancements
- Add more advanced features like customer segmentation and data analytics.
- Extend the system to integrate with third-party APIs for data enrichment.
- Develop a web-based or GUI version of the CRM system for enhanced usability.

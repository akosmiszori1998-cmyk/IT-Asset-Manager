Corporate IT Asset Manager:

A modular Python application designed to track and manage company hardware (Laptops and Servers). This project demonstrates advanced Object-Oriented Programming (OOP) concepts and Design Patterns.

Key Features:

- Factory Pattern: Automatically creates correct object types (Server or WorkStation) from raw text input.
- OOP Principles: Implements Inheritance, Polymorphism (custom error reporting), and Encapsulation.
- Data Validation: Uses properties and setters to ensure valid device states (Active, Service, Reject).
- JSON Export: Saves the final inventory state to a structured inventory.json file.

Project Structure:

- main.py: The entry point. Handles data loading and execution.
- system.py: Manages the inventory logic (ITSystem class).
- devices.py: Contains the device blueprints and factory logic.

How to Run:

1. Clone the repository.
2. Run the main script:
   python main.py
3. Check the console for the status report and find the generated inventory.json in the folder.


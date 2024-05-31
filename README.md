# Price Tracker Application

## Project Goal

This project aims to develop a user-friendly and efficient Price Tracker application that allows users to easily compare products from different stores on Arfigyelo. Users can select desired products from various stores and then decide whether to save the shopping list or check how the cost changes if they shop at a single store.

## Technologies Used

- **Webscraper: Selenium**: Selenium is a popular automation tool used for browsing websites and collecting data. We use this tool to gather product data from Arfigyelo website.
- **Transformation: Pandas**: Pandas is a Python library used for data manipulation and analysis. We use this tool to format and transform the collected data to make it easily processable and comprehensible.
- **Data Orchestrator: Airflow**: Apache Airflow is a platform used for automating and scheduling workflows. We use this tool to schedule and coordinate the data collection, transformation, and analysis processes.
- **Database: MySQL**: MySQL is an open-source relational database management system used for storing and managing data. This ensures reliable data storage and fast querying.
- **User Interface: Tkinter**: Tkinter is a Python library for creating graphical user interfaces (GUI). Through this, users can browse and compare products from different stores, create and save shopping lists, and check how the cost changes if they shop at a single store.

## Application Workflow

1. **Data Collection**: Using Selenium, the application automatically browses various store websites and collects product data, such as prices, product names, and availability.
2. **Data Processing**: The collected data is cleaned and transformed using Pandas. This includes formatting, filtering, and handling any missing data.
3. **Data Orchestration**: Airflow automates and schedules the data collection and processing workflows, ensuring the data is always up-to-date and accurate.
4. **Data Storage**: The cleaned data is stored in a MySQL database, allowing for efficient and reliable data access.
5. **User Interface**: The user interface is implemented using Tkinter. This Python library enables the creation of graphical user interfaces (GUI). Users can browse and compare products from different stores, create and save shopping lists, and check how the cost changes if they shop at a single store.

## Demonstration

A detailed presentation and demonstration of the project's functionality can be viewed in the following YouTube video: [Application Workflow](https://youtu.be/Ktty0BKLczk).

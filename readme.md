# FastAPI and React Web Application

This web application is built using FastAPI and React, and it allows you to fetch data from a PostgreSQL database, as well as upload a CSV file to add data to the database.

## Features

- Seed the database with provided CSV file.
- Fetch data from the database and display it on the web page.
- Upload a CSV file to add data to the database.

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/): A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- [React](https://reactjs.org/): A JavaScript library for building user interfaces.
- [PostgreSQL](https://www.postgresql.org/): A powerful, open-source relational database management system.
- [psycopg](https://www.psycopg.org/): A PostgreSQL adapter for Python.

## Installation

1. Clone the repository:

   ```
   git clone <repository-url>
   ```

2. Set up the backend:

   - Install the required Python packages using pip:

     ```
     pip install -r backend/requirements.txt
     ```

   - Set up the PostgreSQL database using pgAdmin or any other preferred method. Create a table in the database manually using the desired schema.

   - Update the database connection details in the `backend/app/config.py` file.

3. Set up the frontend:

   - Navigate to the `frontend` directory:

     ```
     cd frontend
     ```

   - Install the required dependencies using npm:

     ```
     npm install
     ```

4. Start the backend server:

   - From the `backend` directory, run the following command:

     ```
     uvicorn app.main:app --reload
     ```

   - The backend server will start running on `http://localhost:8000`.

5. Start the frontend development server:

   - From the `frontend` directory, run the following command:

     ```
     npm start
     ```

   - The frontend development server will start running on `http://localhost:3000`.

6. Access the web application:

   - Open a web browser and navigate to `http://localhost:3000`.

7. Seed the database:

   - Use the provided CSV file to seed the database. Replace the placeholder with the actual CSV file in the backend code.
   using: $python seed.py
   warning: do not attempt to run the program without seeding as it will crash
   warning: in the main.py you should configure th postgres connectiion to match your device


8. Interact with the web application:

   - Click the "Fetch Data" button to retrieve data from the database and display it on the page.
   - Click the "Upload CSV" button to select and upload a CSV file. The data from the file will be added to the database.

Note: Make sure to have PostgreSQL and the required Python and Node.js dependencies installed before running the application.

Feel free to modify the installation instructions and provide additional details based on your project structure and specific requirements.

Please let me know if there's anything else I can assist you with!

# Screenshots:

# Before fetching
![Alt text](/sc/beforefetch.png?raw=true "")

# After Fetching
![Alt text](/sc/afterfetch.png?raw=true "")

# Upload
![Alt text](/sc/upload.png?raw=true "")

# Test.csv
![Alt text](/sc/testcsv.png?raw=true "")

# After Upload
![Alt text](/sc/afterupload.png?raw=true "")



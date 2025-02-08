Final Project for 110a

# Superstore Data Analysis Flask App

This is a web application for analyzing a superstore's inventory dataset, built using Flask and Pandas. The application allows users to filter the dataset based on various categories and run predefined queries, presenting the results in a user-friendly format. It uses data that was provided in class. 

## Features

- **Filter the Data**: Users can filter data by Category, Sub-Category, Region, and Segment.
- **Run Queries**: Perform various queries on the filtered data, such as:
  - Total Sales and Profit
  - Average Discount by Product
  - Total Sales by Year
  - Profit by Region
  - Products with Negative Profit
- **Flash Messages**: Displays flash messages for validation, such as when conflicting selections are made.
- **Reset Functionality**: Allows users to reset the filter selections easily.

## Project Structure

```
my_flask_app/
├── app.py                # Main Flask application file
├── templates/
│   └── index.html        # HTML template for the application
├── static/
│   └── style.css         # CSS styling for the application
└── data/
    └── superstore_sales.csv # Dataset used in the application
```

## Setup Instructions

### Prerequisites

- Python 3.7+
- VSCode or any code editor
- Required Python libraries:
  - Flask
  - Pandas

### Step-by-Step Setup

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd my_flask_app
   ```
   **OR**
  Download the ZIP, then extract to a `my_flask_app` folder.

3. **Open Project in VSCode**:
   - Open VSCode and use the "Open Folder" option to open the `my_flask_app` directory.
   - Open the command palette to create a venv.
   - Select the Python 3.7+ interpreter. 
   - Make sure you have the Python extension installed in VSCode for better development experience.

4. **Verify Project Structure**: Ensure your project files are organized as follows:
   - `app.py`: The main Flask application.
   - `templates/index.html`: HTML template for rendering the interface.
   - `static/style.css`: CSS file to enhance the look and feel.
   - `data/superstore_sales.csv`: The dataset file.

5. **Install Dependencies**:
   - Open the terminal in VSCode (`Ctrl + \` or View > Terminal).
   - Run the following:
     ```bash
     pip install flask pandas
     ```

5. **Run the Application**:
   - Open the terminal in VSCode (`Ctrl + \` or View > Terminal).
   - Run the Flask application using the command:
     ```bash
     python app.py
     ```
     **OR**
     Run the project with the IDE debugger.

6. **Access the Application**:
   - Open your web browser and go to `http://127.0.0.1:5000` to see the application.

## How to Use the Application

1. **Filters**: Use the dropdown menus to select filters such as Category, Sub-Category, Region, and Segment.
2. **Query Selection**: Select a query from the provided dropdown to analyze the filtered data.
3. **Run Query**: Click on the "Run Query" button to get results based on your selected filters and query.
4. **Reset Filters**: Click on the "Reset" button to clear all selections and start over.

## Notable Features

- The application includes input validation to ensure that conflicting selections are not allowed (e.g., selecting a Sub-Category that doesn't match the selected Category).
- Flash messages are used to provide feedback to users when a conflicting selection occurs.
- Display type adjusts automatically for user readability depending on data type. 

## Troubleshooting

- If the Flask server does not start, make sure you are in the correct folder and have installed all dependencies.
- Ensure that Python 3.7+ is being used. 
- Use VSCode's built-in debugger to add breakpoints in `app.py` if you need to troubleshoot any errors.

## Contributing

I will not continue to support this project, so no new pull requests will be mereged. However feel free to fork it or use it as a template to build upon. 

## License

This is a school project that I decided to go deeper on, it is licensed under the MIT License.


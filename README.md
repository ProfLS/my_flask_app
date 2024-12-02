# Superstore Data Analysis Flask App

This is a web application for analyzing the Superstore dataset, built using Flask and Pandas. The application allows users to filter the dataset based on various categories and run predefined queries, presenting the results in a user-friendly format.

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

2. **Install Dependencies**: Install the required Python libraries using pip.
   ```bash
   pip install flask pandas
   ```

3. **Open Project in VSCode**:
   - Open VSCode and use the "Open Folder" option to open the `my_flask_app` directory.
   - Make sure you have the Python extension installed in VSCode for better development experience.

4. **Create Project Structure**: Ensure your project files are organized as follows:
   - `app.py`: The main Flask application.
   - `templates/index.html`: HTML template for rendering the interface.
   - `static/style.css`: CSS file to enhance the look and feel.
   - `data/superstore_sales.csv`: The dataset file.

5. **Run the Application**:
   - Open the terminal in VSCode (`Ctrl + \` or View > Terminal).
   - Run the Flask application using the command:
     ```bash
     python app.py
     ```

6. **Access the Application**:
   - Open your web browser and go to `http://127.0.0.1:5000` to see the application.

## How to Use the Application

1. **Filters**: Use the dropdown menus to select filters such as Category, Sub-Category, Region, and Segment.
2. **Query Selection**: Select a query from the provided dropdown to analyze the filtered data.
3. **Run Query**: Click on the "Run Query" button to get results based on your selected filters and query.
4. **Reset Filters**: Click on the "Reset" button to clear all selections and start over.

## Notes

- The application includes input validation to ensure that conflicting selections are not allowed (e.g., selecting a Sub-Category that doesn't match the selected Category).
- Flash messages are used to provide feedback to users when a conflicting selection occurs.

## Example Screenshots

You can add screenshots here to show what the application looks like.

## Troubleshooting

- If the Flask server does not start, make sure you are in the correct folder and have installed all dependencies.
- Use VSCode's built-in debugger to add breakpoints in `app.py` if you need to troubleshoot any errors.

## Contributing

Feel free to submit issues or contribute to the project by creating pull requests.

## License

This project is licensed under the MIT License.


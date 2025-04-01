# Cricket Stats Application

This project is a full-stack web application designed to display statistics of Indian cricket players. It includes features for data extraction, cleaning, and analysis, providing users with insights into player performance.

## Demo Video

[Watch the Demo Video](https://drive.google.com/file/d/19El6PfcGlnfkCnkJohM_GC-lDFEV0b_h/view?usp=drive_link)

## Project Structure

The project is organized into the following main directories:

- **backend**: Contains the Django application responsible for handling requests, managing data, and serving the frontend.
  - **cricket_stats**: The main Django app containing settings, URLs, views, models, and templates.
  - **manage.py**: Command-line utility for managing the Django project.
  - **requirements.txt**: Lists the required Python packages for the backend.

- **frontend**: Contains the React application that serves as the user interface.
  - **public**: Contains the main HTML file for the React app.
  - **src**: Contains the React components, styles, and entry point for the application.
  - **package.json**: Configuration file for npm, listing dependencies and scripts.
  - **webpack.config.js**: Configuration for bundling the frontend application.

- **data**: Contains scripts for data extraction, cleaning, and analysis.
  - **extraction**: Scripts for extracting data from various sources.
  - **cleaning**: Scripts for cleaning and preprocessing the extracted data.
  - **analysis**: Scripts for analyzing the cleaned data and generating insights.
  - **raw_data**: Contains the raw data files used for extraction and analysis.

## Features

- **Data Extraction**: Automatically fetches player statistics from various sources.
- **Data Cleaning**: Processes and cleans the extracted data to ensure accuracy and usability.
- **Data Analysis**: Analyzes the cleaned data to generate meaningful statistics and insights about players.
- **User Interface**: A responsive frontend built with React, allowing users to view player statistics easily.

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd cricket-stats-app
   ```

2. **Set up the backend**:
   - Navigate to the `backend` directory.
   - Install the required Python packages:
     ```
     pip install -r requirements.txt
     ```
   - Run the Django server:
     ```
     python manage.py runserver
     ```

3. **Set up the frontend**:
   - Navigate to the `frontend` directory.
   - Install the required npm packages:
     ```
     npm install
     ```
   - Start the React application:
     ```
     npm start
     ```

## Usage

Once both the backend and frontend are running, you can access the application in your web browser at `http://localhost:3000`. Explore the statistics of Indian cricket players and gain insights into their performance.

For in now backend is running on http://127.0.0.1:8000/

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

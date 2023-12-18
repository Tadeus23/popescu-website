# Cătălin Popescu's Portfolio Website

## Introduction
Welcome to my official portfolio website. This Flask-based web application showcases my professional work and skills. The website parses data from Python's `data.py` file and renders it into HTML, providing a dynamic and interactive user experience.

Access the live website at: [this link](https://popescu-website-flask-883aeefd7871.herokuapp.com/)

## Features
- **Portfolio Showcase**: Displays my professional projects and achievements.
- **Data-driven Content**: Dynamically parses data from `data.py` to HTML, ensuring up-to-date content.
- **Responsive Design**: Offers an optimal browsing experience across different devices.
- **Flask CLI Commands**: Custom command-line interface commands for advanced interactions.

## Technologies Used
- Flask
- Python
- HTML/CSS
- JavaScript
- Heroku

## Installation and Setup
### Installing Python
If Python is not already installed on your system, download and install it from [python.org](https://www.python.org/downloads/). Follow the instructions for your specific operating system.

### Setting Up the Project
1. Clone the repository:
> git clone [repository URL]

2. In the project directory, install the required dependencies:
> pip install -r requirements.txt

### Running Locally
To run the application:
> python app.py

The website will be accessible locally at `http://localhost:5000`.

## Application Routes
- **Home Page (`/`)**: Main portfolio page, displaying data parsed from `data.py`.
- **Personal Info (`/personal`)**: Returns my personal information in JSON format.
- **Experience (`/experience`)**: Returns my professional experience in JSON format.
- **Education (`/education`)**: Returns my educational background in JSON format.
- **Skills (`/skills`)**: Returns my skills in JSON format.
- **Certifications (`/certifications`)**: Returns my certifications in JSON format.

## Using Flask CLI Commands
Custom Flask CLI commands for managing my CV data:
- **Get CV Data**: `flask get-cv` - Displays the complete CV data.
- **Add Skill**: `flask add-skill` - Adds a new skill to the CV.
- **Delete Skill**: `flask delete-skill [index]` - Deletes a skill from the CV based on its index.
- **Update Skill**: `flask update-skill [index]` - Updates a specific skill in the CV.

## Heroku CLI Commands
Interact with the application on Heroku using the Heroku CLI:
> heroku logs --tail -a popescu-website-flask
> heroku ps:scale web=1 -a popescu-website-flask

## Testing
Run the included tests to ensure the application's functionality:
> python tests.py

## Code Style and Linting
The project adheres to PEP 8 standards, enforced using flake8:
> flake8 --config app.flake8

## Deployment
The website is deployed on Heroku. Visit the live site at [this link](https://popescu-website-flask-883aeefd7871.herokuapp.com/).

## Contributing
Contributions are welcome to enhance the website. Please follow standard git workflow procedures for contributions.

## Contact
For any inquiries or suggestions, please reach out to me at popescu351@gmail.com .
# Catalin Popescu's Portfolio Website

## Introduction
Welcome to Catalin Popescu's official portfolio website. This Flask-based web application showcases Catalin's professional work and skills. The website parses data from Python's `data.py` file and renders it into HTML, providing a dynamic and interactive user experience.

Access the live website at: [https://popescu-website-flask-883aeefd7871.herokuapp.com/](https://popescu-website-flask-883aeefd7871.herokuapp.com/)

## Features
- **Portfolio Showcase**: Displays Catalin's professional projects and achievements.
- **Data-driven Content**: Dynamically parses data from `data.py` to HTML, ensuring up-to-date content.
- **Responsive Design**: Offers an optimal browsing experience across different devices.
- **Flask CLI Commands**: Custom command-line interface commands for advanced interactions.

## Technologies Used
- Flask
- Python
- HTML/CSS
- JavaScript (if used)
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
- **Personal Info (`/personal`)**: Returns Catalin's personal information in JSON format.
- **Experience (`/experience`)**: Returns Catalin's professional experience in JSON format.
- **Education (`/education`)**: Returns Catalin's educational background in JSON format.
- **Skills (`/skills`)**: Returns Catalin's skills in JSON format.
- **Certifications (`/certifications`)**: Returns Catalin's certifications in JSON format.

## Using Flask CLI Commands
Custom Flask CLI commands for managing Catalin's CV data:
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

## License
This project is open-sourced under the MIT License.

## Contact
For any inquiries or suggestions, please reach out to Catalin Popescu at popescu351@gmai.com .
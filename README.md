# CV Data Flask Application

Welcome to the CV Data Flask Application!

Follow the steps below to get started.

## Getting Started

### ‣ Prerequisites

1. Make sure you have [Python](https://www.python.org/downloads/) installed on your computer.
2. Download this project and extract it to a folder of your choice.

### ‣ Install Dependencies

Open a command prompt or terminal in the project folder and run the following command to install the required dependencies:

> pip install -r requirements.txt

In the command prompt or terminal, run the following command to start the application:

> python app.py

The application will start, and you'll see some output indicating that the server is running.

> * Serving Flask app 'app'
> * Debug mode: on
> WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
> * Running on http://127.0.0.1:5000
> Press CTRL+C to quit
> * Restarting with stat
> * Debugger is active!
> * Debugger PIN: 694-322-092

### ‣ Access the data via local web server

You can access your CV data using the following endpoints:

**Personal Information: http://localhost:5000/personal (GET)**

**Experience: http://localhost:5000/experience (GET)**

**Education: http://localhost:5000/education (GET)**

**Skills: http://localhost:5000/skills (GET)**

**Certifications: http://localhost:5000/certifications (GET)**


### ‣ Access the data via CLI Command - Local

Open a new command prompt or terminal in the project folder and run the following:

Get CV Data:

> flask get-cv


### ‣ Access the data via Heroku web server

**Personal Information: https://flask-cv-app-5c06e202e6d2.herokuapp.com/personal (GET)**

**Experience: https://flask-cv-app-5c06e202e6d2.herokuapp.com/experience (GET)**

**Education: https://flask-cv-app-5c06e202e6d2.herokuapp.com/education (GET)**

**Skills: https://flask-cv-app-5c06e202e6d2.herokuapp.com/skills (GET)**

**Certifications: https://flask-cv-app-5c06e202e6d2.herokuapp.com/certifications (GET)**


### ‣ Access the data via Heroku CLI Commands

**Install Heroku CLI:**

Download and install the Heroku CLI from the official [Heroku Dev Center](https://devcenter.heroku.com/articles/heroku-cli).

**Login to Heroku:**

[Register](https://signup.heroku.com/login) in order to get an account.

Open your terminal or command prompt.

Run the following command to log in to your Heroku account:

'heroku login'

**Access Remote Shell:**

To access a remote shell on your Heroku app (flask-cv-app), run:

> heroku run bash -a flask-cv-app

**Run CLI Command:**

Once in the remote shell, execute the following command to get the entire CV data:

> flask get-cv

**View Data:**

The CLI command will display the CV data in JSON format.

**Exit the Remote Shell:**

After reviewing the data, type:

> exit

Press Enter to close the remote connection.



**If you have any issues or questions, feel free to reach out for assistance.**


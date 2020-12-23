## virtualenv

Install virtual environment

> pip install virtualenv

Create a virtual environment

> cd .venv

> mkdir flask

> virtualenv flask

> source .venv/flask/bin/activate

# Prerequisites

Use 'yarn build' from package.json to install the prerequisites, or run directly from the command line...

> pip install -r requirements.txt


# Run the website

1. Switch to the virtual environment

> cd src/student_web

> source .venv/flask/bin/activate

2. Run the web service

> yarn start:test--flask

3. Launch the website

http://127.0.0.1:3001
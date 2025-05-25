Report Dashboard

A simple Flask web application that tracks reports stored in an SQLite database.

Live demo: https://gallybear.pythonanywhere.com/

#Features

    Create, Read, Update, Delete report entries for keeping track of Investment Manager reporting

    SQLite-backed data storage

    Lightweight and responsive UI

    JSON API for creating and fetching reports:

        GET /api/reports — returns all reports

        POST /api/reports — creates a new report

        Test data via /test_report

#Tech Stack

    Python 3

    Flask

    SQLite

    HTML
    
    Javascript (Ajax)

#Routes

    [/] — View all reports

    [/test_report] — Check if the test report was successful

    [/ajax] — Load AJAX-friendly test page

    [/api/reports] — API GET/POST endpoints in JSON

#Project Structure

flask_webapp/
├── templates/
│   ├── index.html
│   ├── edit_form.html
│   └── ajax.html
├── instance/
│   └── reports.db (created automatically)
└── app.py

#Clone the repository:

git clone https://github.com/CianGallagher/IM_Report_Tracker.git


#Deployment

This app is deployed on PythonAnywhere. The database is stored in the instance/ directory, and WSGI is configured to point to flask_webapp.app.

#Reference Material 


    Flask Official Quickstart — General structure of the app and routing logic
    https://flask.palletsprojects.com/en/stable/quickstart/

    Flask-SQLAlchemy Documentation — Defining models, using db.create_all(), querying
    https://flask-sqlalchemy.palletsprojects.com/en/latest/models/
    https://docs.sqlalchemy.org/en/20/

    PythonAnywhere Flask Deployment Guide — Hosting this project
    https://help.pythonanywhere.com/pages/Flask/

    GeeksForGeeks Flask Routing Guide — Helpful during route creation
    https://www.geeksforgeeks.org/flask-app-routing/

    MDN Fetch API Reference — Used for building /ajax and understanding fetch behavior
    https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch

    StackOverflow – Fetching HTML via JS — Used in ajax.html to load data dynamically
    https://stackoverflow.com/questions/36631762/returning-html-with-fetch
    https://stackoverflow.com/questions/57987543/how-do-i-use-the-fetch-api-to-load-html-page-with-its-javascript

Large Language Models (LLMs), including ChatGPT, were used throughout development to:

    Explore best practices for structuring Flask applications.

    Troubleshoot common deployment issues (database access on PythonAnywhere).

    Clarify form handling, and POST/GET routing patterns.

    Refactor and clean up code for readability and maintainability.

All LLM-guided code was validated by cross-referencing official documentation or working examples.
# TechTreds Web Application

This is a Flask application that lists the latest articles within the cloud-native ecosystem.

## Run 

To run this application there are 2 steps required:

1. Initialize the database by using the `python init_db.py` command. This will create or overwrite the `database.db` file that is used by the web application.
2.  Run the TechTrends application by using the `python app.py` command. The application is running on port `3111` and you can access it by querying the `http://127.0.0.1:3111/` endpoint.

## Changelog

### 2024-03-02 23:28:05: Step 2

- Dockerize the application

### 2024-03-02 18:03:42: Step 1

- Added the /healthz endpoint
- Added the /metrics endpoint
- Added logging

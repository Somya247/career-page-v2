from flask import Flask, render_template, jsonify  # Import necessary modules
from database import load_jobs_from_db  # Import the database and function
from sqlalchemy import text  # Import the text module from SQLAlchemy
from jinja2 import Template, Environment

app = Flask(__name__)  # Create a Flask application



@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()  # Call the 'load_jobs_from_db' function to retrieve the job listings
    return render_template("home.html", jobs=jobs)  # Render the 'home.html' template and pass the 'jobs' data


@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()  # Call the 'load_jobs_from_db' function to retrieve the job listings
    return jsonify(jobs)  # Return the job listings as JSON


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)  # Start the Flask application
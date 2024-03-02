import sqlite3
from flask import (
    Flask,
    jsonify,
    json,
    render_template,
    request,
    url_for,
    redirect,
    flash,
)
from werkzeug.exceptions import abort
from logs import init_logger

logger = init_logger()


# Function to get a database connection.
# This function connects to database with the name `database.db`
def get_db_connection():
    connection = sqlite3.connect("database.db")
    connection.execute("INSERT INTO connections DEFAULT VALUES")
    connection.commit()
    connection.row_factory = sqlite3.Row
    return connection


# Function to get a post using its ID
def get_post(post_id: int) -> sqlite3.Row:
    connection = get_db_connection()
    post = connection.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    connection.close()
    return post


def get_connection_count():
    connection = get_db_connection()
    conn_result = connection.execute("SELECT MAX(id) FROM connections")
    conn_count = conn_result.fetchone()[0]
    connection.close()
    return conn_count


# Define the Flask application
app = Flask(__name__)
app.config["SECRET_KEY"] = "your secret key"


# Define the main route of the web application
@app.route("/")
def index():
    connection = get_db_connection()
    posts = connection.execute("SELECT * FROM posts").fetchall()
    connection.close()
    return render_template("index.html", posts=posts)


# Define how each individual article is rendered
# If the post ID is not found a 404 page is shown
@app.route("/<int:post_id>")
def post(post_id):
    post = get_post(post_id)
    if post is None:
        logger.warning(f"Article {post_id} not found!")
        return render_template("404.html"), 404
    else:
        title = post["title"]
        logger.info(f"Article {post_id}: '{title}' retrieved!")
        return render_template("post.html", post=post)


# Define the About Us page
@app.route("/about")
def about():
    logger.info("About Us page retrieved!")
    return render_template("about.html")


# Define the post creation functionality
@app.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        if not title:
            flash("Title is required!")
        else:
            connection = get_db_connection()
            connection.execute(
                "INSERT INTO posts (title, content) VALUES (?, ?)", (title, content)
            )
            connection.commit()
            connection.close()

            logger.info(f"Created a new page: '{title}'!")
            return redirect(url_for("index"))

    return render_template("create.html")


# Healthz endpoint: 200 JSON with result: OK - healthy
@app.route("/healthz")
def healthz():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype="application/json",
    )
    return response


# Metrics endpoint: 200 JSON
# post_count: Total amount of posts in the database
# db_connection_count: Total amount of connections to the database.
# For example, accessing an article will query the database, hence will count as a connection.
@app.route("/metrics")
def metrics():
    connection = get_db_connection()
    post_count = connection.execute("SELECT COUNT(*) FROM posts").fetchone()[0]
    connection_count = get_connection_count()
    connection.close()

    response = app.response_class(
        response=json.dumps(
            {
                "db_connection_count": connection_count,
                "post_count": post_count,
            }
        ),
        status=200,
        mimetype="application/json",
    )
    return response


# start the application on port 3111
if __name__ == "__main__":
    logger.info("Starting the application!")
    app.run(host="0.0.0.0", port="3111")

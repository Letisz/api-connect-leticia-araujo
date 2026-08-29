from flask import Flask
from routes.connect_routes import connect_routes

app = Flask(__name__)

app.register_blueprint(connect_routes)


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )

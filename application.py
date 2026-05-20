from flask import Flask

# Elastic Beanstalk looks for exactly the variable with the name "application"
application = Flask(__name__)


@application.route('/')
def index():
    return "<h1>Hello! Automated CI/CD works perfectly!</h1>"


if __name__ == "__main__":
    # Local development (AWS ignores this block and runs through WSGI)
    application.run(host="0.0.0.0", port=5000)

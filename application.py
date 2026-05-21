from flask import Flask

application = Flask(__name__)


@application.route('/')
def index():
    return "Hello from u3vaje75 Elastic Beanstalk CI-CD verification-2026052116050415548"

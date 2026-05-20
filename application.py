from flask import Flask

# Elastic Beanstalk шукає саме змінну з назвою "application"
application = Flask(__name__)


@application.route('/')
def index():
    return "<h1>Flask App is running on AWS Elastic Beanstalk!</h1>"


if __name__ == "__main__":
    # Локальний запуск (AWS ігнорує цей блок і запускає через WSGI)
    application.run(host="0.0.0.0", port=5000)

import sentry_sdk, os
from sentry_sdk.integrations.flask import FlaskIntegration

from flask import Flask, render_template

sentry_sdk.init(
    dsn=os.environ['SENTRY_DSN'],
    integrations=[FlaskIntegration()]
)

application = Flask(__name__)
application.templates_auto_reload = True


@application.route("/")
def index():
    # return "<h1 style='color:blue'>Hello There!</h1>"
    return render_template("index.html")


@application.route("/map")
def map():
    return render_template("map.html")


@application.route('/debug-sentry')
def trigger_error():
    foo = 1
    bar = 0
    division_by_zero = foo / bar + 1


if __name__ == "__main__":
    application.run(host="0.0.0.0")


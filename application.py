from flask import Flask, render_template

application = Flask(__name__)


@application.route("/")
def index():
    # return "<h1 style='color:blue'>Hello There!</h1>"
    return render_template("index.html")


if __name__ == "__main__":
    application.run(host="0.0.0.0")


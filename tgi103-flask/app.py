from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index_page():
    return "<h1>Hello Flask!</h1>123123123123"


@app.route("/hello/<username>")
def hello(username):
    return "Hello {}".format(username)


@app.route("/two_sum/<x>/<y>")
def two_sum(x, y):
    return str(int(x) + int(y))


# /hello_get?username=Allen&age=22
@app.route("/hello_get")
def hello_get():
    username = request.args.get("username")
    age = request.args.get("age")
    if username is None:
        return "What is your name?"
    elif age is None:
        return "Hello {}.".format(username)
    else:
        return "Hello {}, you are {} years old.".format(username, age)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)

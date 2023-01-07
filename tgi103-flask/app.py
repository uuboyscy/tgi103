from flask import Flask, request, jsonify, render_template
import poker as p
import model
from test_controller import test_controller

app = Flask(__name__, static_url_path="/resource", static_folder="./resource")
app.register_blueprint(test_controller, url_prefix='/test_controller')


@app.route("/")
def index_page():
    return "<h1>Hello Flask!</h1>123123123123"


# @app.route("/hello/<username>")
# def hello(username):
#     return "Hello {}".format(username)


@app.route("/hello/<username>")
def hello(username):
    return render_template("index_page.html", username=username)


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


# @app.route("/hello_post", methods=["GET", "POST"])
# def hello_post():
#     html = """
#     What is your name?
#     <br>
#     <form action="/hello_post" method="POST">
#         <input name="username">
#         <button type="submit">SUBMIT</button>
#     </form>
#     """
#     request_method = request.method
#     if request_method == "POST":
#         username = request.form.get("username")
#         html += f"""
#         <h1>Hello {username}</h1>
#         """
#
#     return html

@app.route("/hello_post", methods=["GET", "POST"])
def hello_post():
    request_method = request.method
    username = request.form.get("username")

    return render_template(
        "hello_post.html",
        request_method=request_method,
        username=username
    )


@app.route("/hello_json", methods=["POST"])
def hello_json():
    json_data = request.json
    print(json_data)
    print(type(json_data))
    print(json_data["name"])
    return ""


# /poker?player=5
# @app.route("/poker")
# def poker():
#     player = int(request.args.get("player"))
#     json_data = p.poker(player)
#     return jsonify(json_data)

@app.route('/poker', methods=['GET', 'POST'])
def poker():
    request_method = request.method
    players = 0
    cards = dict()
    if request_method == 'POST':
        players = int(request.form.get('players'))
        cards = p.poker(players)
    return render_template('poker.html', request_method=request_method,
                                         cards=cards)


@app.route('/show_staff')
def hello_google():
    staff_data = model.getStaff()
    column = ['ID', 'Name', 'DeptId', 'Age', 'Gender', 'Salary']
    return render_template('show_staff.html', staff_data=staff_data,
                                              column=column)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)

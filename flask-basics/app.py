from flask import Flask

# application object
app = Flask(__name__)

# activate app for error handling
app.config["DEBUG"] = True

@app.route("/")
@app.route("/hello")

def hello():
    return "Hello, world"

@app.route("/integer/<int:value>")
def int_type(num):
    print(num + 1)
    return f"{num}"

@app.route("/float/<float:value>")
def float_type(num):
    print(num + 1)
    return f"{num}"

@app.route("/path/<path:value>")
def path_type(value):
    print(value)
    return f"{value}"

# dynamic route
@app.route("/about/<search_q>")
def search(search_q):
    return search_q

# dynamic route with defined status code
@app.route("/name/<name>")
def home(name):
    if name.lower() == "tesfa":
        return f"Hello, {name}", 200
    else:
        return "Not Found", 404


if __name__ == "__main__":
    app.run()
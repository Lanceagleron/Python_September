from flask import Flask

app = Flask(__name__)
app.secret_key


@app.route('/')
def hello_world():
    return "Hello world!"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route('/say/<something>')
def say_something(something):
    return f"hi {something}"

@app.route('/repeat/<int:num>/<var>')
def repeatnumbervariable(num, var):
    return f'repeat {var * num}'



if __name__=="__main__":
    app.run(debug=True) 
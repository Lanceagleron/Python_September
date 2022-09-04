from flask import Flask, render_template 

app = Flask(__name__)
app.secret_key

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/play')
def play():
    
    return render_template("index.html", number=3)

@app.route('/play/<int:number>')
def iterate(number):
    print(number)
    return render_template("index.html", number=number)

@app.route('/play/<int:number>/<color>')
def color(color,number):

    return render_template("index.html", color=color, number=number)

if __name__=="__main__":
    app.run(debug=True) 
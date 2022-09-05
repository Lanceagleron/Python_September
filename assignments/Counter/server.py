from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = "No secrets on github"

@app.route('/')
def index():
    if "visit" not in session:
        session['visit'] = 1
    else:
        session['visit'] +=1

    return render_template("index.html")

@app.route('/addtwo')
def addtwo():
    session['visit'] +=1

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()

    return redirect('/')




if __name__ == '__main__':
    app.run(debug=True)
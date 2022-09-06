from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "No secrets on github"

@app.route('/')
def index():

    print("I am printing something into the terminal, this might be useful")
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process_form():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/show_info')

@app.route('/show_info')
def show_info():
    
    return render_template('gotinfo.html')



if __name__ == '__main__':
    app.run(debug=True)
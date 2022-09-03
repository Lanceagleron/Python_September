from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    print("I am printing someong into the terminal, this might be useful")
    return render_template('index.html')


@app.route('/fill_out_form')
def fill_out_form():
    return render_template('form.html')




if __name__ == '__main__':
    app.run(debug=True)
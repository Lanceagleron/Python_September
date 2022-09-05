from flask import Flask, render_template, request, redirect, session
#import request to be able to access the body of our post request (request.form)
app = Flask(__name__)
app.secret_key = "No secrets on github"


@app.route('/')
def index():
    print("I am printing someong into the terminal, this might be useful")
    return render_template('index.html')


@app.route('/fill_out_form')
def fill_out_form():
    return render_template('form.html')

@app.route('/process', methods=['POST']) #methods list for specifying methods to listen for
def process_form():
    session['name'] = request.form['name']
    session['fave_pokemon'] = request.form ['fave_pokemon']
    session['form_num'] = request.form['form_num']
    # return render_template("display.html", name=name, fave_pokemon=fave_pokemon) #typically we won't render on "ACTION ROUTES"
    return redirect("/show_info")

@app.route('/show_info')
def show_info():
    if 'form_num' in session:
        num = session['form_num']
    # name = session['name']
    # fave_pokemon = session['fave_pokemon']
    return render_template("display.html", num=num) #name=name, fave_pokemon=fave_pokemon)


@app.route('/clear_session')
def clear_session():
    session.clear() #would remove all keys
    # del session['name'] would remove one key 
    # name = session.pop('name')
    return redirect('/')







@app.route("/iterate")
def iterate():
    cats = [
        {
            'name': "Garfield",
            'color': 'orange'
        },
        {
            'name': 'scar',
            'color': 'darkbrown'
        },
        {
            'name': 'felix',
            'color': 'black'
        }
    ]
    return render_template("cat.html", cats = cats)

if __name__ == '__main__':
    app.run(debug=True)
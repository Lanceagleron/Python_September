from flask import Flask, render_template, session, request, redirect
from dog_model import Dog
app= Flask(__name__)

@app.route('/')
def index():
    all_dogs = Dog.get_all()
    print(all_dogs)
    return render_template('index.html', all_dogs = all_dogs)





















if __name__ == "__main__":
    app.run(debug=True)
# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
from minilab.app import minilab_bp
from minilab.isai import Factorial


#create a Flask instance
app = Flask(__name__)
app.register_blueprint(minilab_bp, url_prefix='/minilab')



#connects default URL of server to a python function
@app.route('/')
@app.route('/home')
def home():
    #function use Flask import (Jinja) to render an HTML template
    return render_template ("base.html")

@minilab_bp.route('/isai', methods=["GET", "POST"])
def isai():
    if request.form:
        return render_template("minilab/isai.html", factorial=Factorial(int(request.form.get("series"))))
    return render_template("minilab/isai.html", factorial=Factorial(2))



if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True)
    #app.run(debug=True, port="5001", host="127.0.0.1")
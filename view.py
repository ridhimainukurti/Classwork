# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template, request
import minilab.app
from minilab.isai import Factorial

#create a Flask instance
from minilab.ridhima_bubblesort import RidhimaBubblesort

app = Flask(__name__)
import minilab.bubblesort
app.register_blueprint(minilab.app.minilab_bp, url_prefix='/minilab')

#@app.route('/ridhima/')
#def ridhima():
@app.route('/ridhima/')
def ridhima():
    #function use Flask import (Jinja) to render an HTML template
    #   return render_template("/minilab/ridhima.html")
    return render_template("/minilab/ridhima.html")


@app.route('/ridhima_bubblesort', methods=["GET", "POST"])
def ridhimabubblesprt():
    if request.form:
        return render_template("/minilab/ridhima_bubblesort.html", bubblesort=RidhimaBubblesort(request.form.get("inputlist")))
    return render_template("/minilab/ridhima_bubblesort.html", bubblesort=RidhimaBubblesort(""))



#connects default URL of server to a python function
@app.route('/')
@app.route('/home')
def home():
    #function use Flask import (Jinja) to render an HTML template
    return render_template ("base.html")

@minilab.app.minilab_bp.route('/isai', methods=["GET", "POST"])
def isai():
    if request.form:
        return render_template("minilab/isai.html", factorial=Factorial(int(request.form.get("series"))))
    return render_template("minilab/isai.html", factorial=Factorial(2))


@app.route('/sriya')
def sriya():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("/minilab/templates/sriya.html")

@app.route('/bubblesort/', methods=['POST','GET'])
def bubblesort():
    print("hello")
    in_type = request.form.get("input_type", False)
    first = request.form.get("series1", False)
    second= request.form.get("series2", False)
    third= request.form.get("series3", False)
    fourth= request.form.get("series4", False)
    fifth= request.form.get("series5", False)
    sixth= request.form.get("series6", False)
    seventh= request.form.get("series7", False)
    eighth= request.form.get("series8", False)
    ninth= request.form.get("series9", False)
    tenth= request.form.get("series10", False)


    oglist= [first,second,third,fourth,fifth,sixth,seventh,eighth,ninth,tenth]
    if in_type == 'Number':
        input_lst=[int(first), int(second), int(third),int(fourth),int(fifth), int(sixth), int(seventh),int(eighth), int(ninth), int(tenth)]
    else:
        input_lst=[first, second, third,fourth,fifth, sixth, seventh,eighth, ninth, tenth]

    minilab.bubblesort.bubsort (input_lst)

    return render_template("/minilab/bubblesort.html", slist=input_lst, olist=oglist)

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True)
    #app.run(debug=True, port="5001", host="127.0.0.1")
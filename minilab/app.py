from flask import Blueprint, render_template, request
from minilab.ridhima import Exponential
from minilab.isai import Factorial
from minilab.grace import Addition
from minilab.iniyaa import lucas


minilab_bp = Blueprint('minilab',  __name__,
                       template_folder='templates',
                       static_folder='static')

@minilab_bp.route('/')
def minilab():
    return render_template("base.html")

@minilab_bp.route('/test')
def test():
    return "<h1>Grace Test</h1>"


@minilab_bp.route('/ridhima', methods=["GET", "POST"])
def ridhima():
    if request.form:
        return render_template("/minilab/ridhima.html", exponential = Exponential(int(request.form.get("series"))))
    return render_template("/minilab/ridhima.html", exponential= Exponential(2))

@minilab_bp.route('/sriya_bp', methods=["GET", "POST"])
def sriya():
    if request.form:
        return render_template("/minilab/sriya_bp.html", factorial = Factorial(int(request.form.get("series"))))
    return render_template("/minilab/sriya_bp.html", factorial = Factorial(2))

@minilab_bp.route('/isai', methods=["GET", "POST"])
def isai():
    if request.form:
        return render_template("/minilab/isai.html", factorial = Factorial (int(request.form.get("series"))))
    return render_template("/minilab/isai.html", factorial= Factorial(2))
 
@minilab_bp.route('/iniyaa', methods=["GET", "POST"])
def iniyaa():
    if request.form:
        return render_template("/minilab/iniyaa.html", lucas = lucas (int(request.form.get("series"))))
    return render_template("/minilab/iniyaa.html", lucas= lucas(2))


@minilab_bp.route('/addition' , methods=['GET', 'POST'])
def grace():
    if request.form:
        return render_template("/minilab/grace-minilab.html", addition = Addition (int(request.form.get("series"))))
    return render_template("/minilab/grace-minilab.html", addition= Addition(2))

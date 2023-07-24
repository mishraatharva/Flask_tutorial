# Simple Flask Application

from flask import Flask, redirect,url_for,render_template
from flask import request
app = Flask(__name__)

# redirect will redirect to the url

@app.route('/')
def home():
    return "<h1>Hello World</h1>"

@app.route('/welcome')
def welcome():
    return "Welcome To Flask Tutorial index page"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return "the score is :"+ str(score) # here return should be string only.

@app.route('/fail/<int:score>')
def fail(score):
    return "the score is " + str(score) + " and student is fail!"

@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method == 'GET':
        return render_template('calculate.html')
    else:
         maths_score = float(request.form['maths'])
         science_score = float(request.form['science'])
         history_score = float(request.form['history'])
         average_marks = (maths_score + science_score + history_score)/3
         result = average_marks
         
         if average_marks >= 50:
             result = "success"
         else:
             result = "fail"
        
        #  return redirect(url_for(result,score=average_marks))
         return render_template('result.html',result = average_marks)

@app.route('/calculatemarks')
def calculatemarks():
    return render_template('calculate.html')

# action="{{ url_for('calculatemarks')}}" means when submit button is pressed to
# run function with route == '/calculatemarks'

# redirect(url_for('index.html')) : when ever we want to redirect to route.
# render_tempelate() : when ever want to redirect to html page.

if __name__ == '__main__':
    app.run(debug=True) # debug = True only in development environment

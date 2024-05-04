import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY



question1 = "question1"
question2 = "question2"
question3 = "question3"
question4 = "question4"

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set on the server. 
                                     #To run locally, set in env.bat (env.sh on Macs) and include that file in gitignore so the secret key is not made public.

@app.route('/')
def renderMain():
    return render_template('home.html', nextpage = 'renderPage1', Answer1 = 'yes')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1')
def renderPage1():
    return render_template('page1.html', nextpage = 'renderPage2', question = question1)

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    if request.method == 'POST':
        try:
            session["answerTo1"] = request.form["2"]
        except:
            session["answerTo1"] = request.form["1"]
    return render_template('page2.html', nextpage = 'renderPage3', question = question2)

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    if request.method == 'POST':
        try:
            session["answerTo2"] = request.form["2"]
        except:
            session["answerTo2"] = request.form["1"]
    return render_template('page3.html', nextpage = 'renderPage4', question = question3)


@app.route('/page4',methods=['GET','POST'])
def renderPage4():
    if request.method == 'POST':
        try:
            session["answerTo3"] = request.form["2"]
        except:
            session["answerTo3"] = request.form["1"]
    return render_template('page4.html', nextpage = 'renderPage5', question = question4)

@app.route('/page5',methods=['GET','POST'])
def renderPage5():
    if request.method == 'POST':
        try:
            session["answerTo4"] = request.form["2"]
        except:
            session["answerTo4"] = request.form["1"]
    return render_template('page5.html', nextpage = 'renderPage5')

    
if __name__=="__main__":
    app.run(debug=True)


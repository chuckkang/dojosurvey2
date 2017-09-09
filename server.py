from flask import Flask, render_template, request, redirect, session, flash
import re
import random

app = Flask(__name__)
app.secret_key ="this is a secret"
@app.route('/', methods=['GET'])
def index():
      return render_template("index.html")


@app.route('/submitform', methods=['POST'])
def submitform():
    name = request.form["name"]
    location = request.form["location"].strip()
    language = request.form["language"].strip()
    comments = request.form["comments"].strip()
    isValid = False
    # check for name
    if len(name) < 1 :
            flash("Please enter your name")
    elif name.isalpha() != True:
            flash("Please use only letters for your first name")
    
    elif len(location) < 1 :
            flash("Please select a location")
    
    elif len(language) < 1 :
            flash("Please select a language")
    
    elif len(comments) < 1 or len(comments) > 120 :
            flash("Please submit some comments.  However do not exceed 120 characters.")
    else:
        isValid = True
    
    if isValid == True:
        return render_template("results.html", name=name, location=location, language=language, comments=comments)
    else:
        return redirect ("/")
    # print name, location, language, comments
    # return render_template("results.html")












app.run(debug=True) # run our server
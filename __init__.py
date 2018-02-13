from flask import Flask,render_template, url_for, send_from_directory
import requests
from flask import request #in order to be able towork with "GET POST etc "
import os
app = Flask(__name__)

@app.route("/")
@app.route("/mehmet/")
@app.route("/index")
def index():
    return render_template('index.html')

#static/vendor/font-awesome/css/font-awesome.min.css
#####################################################################
@app.route("/search", methods = ['GET', 'POST'])
def search_post():
    if request.method == 'POST': 
        flight_name = request.form["from_flight"]
        return "<html> <body><div><h2>input : %s </h2></div></body>\
        </html> "  % flight_name
    return render_template('search.html')

#####################################################################

@app.route("/create_account", methods = ['GET', 'POST'])
def post_info():
    if request.method == 'POST': 
        email = request.form["email"] #You find the fields by id
        password = request.form["pwd"]

        f = open('user_data.txt','a')
        f.write(email + ' ' + password + '\n')
        f.close()


        return "<html> <body><div><h2>it works, and your email : %s \n \
        your password: %s</h2></div></body> </html> " % (email,password)
    return render_template('create_account.html')

@app.route("/sign_in", methods = ['GET', 'POST'])
def sign_in():
    if request.method == 'POST': 
        email = request.form["email"] 
        password = request.form["pwd"]
        a = False
        try:
            for line in open("user_data.txt","r").readlines(): # Read the lines
                login_info = line.split() # Split on the space, and store the results in a list of two strings
                if email == login_info[0] and password == login_info[1]:
                    a = True
        except:
            return "<html> <body><div><h2>There is a problem here. You entered these values : %s \n \
        your password: %s</h2></div></body> </html> " % (email,password)
        
        if a:
            return "<html> <body><div><h2>CORRECT CREDENTIALS</h2></div></body> </html> "
        else:
            return "<html> <body><div><h2>WRONG CREDENTIALS</h2></div></body> </html> "
        
        return "<html> <body><div><h2>You entered these values : %s \n \
        your password: %s</h2></div></body> </html> " % (email,password)
    return render_template('sign_in.html')
    



if __name__ == "__main__":
    app.run( debug = True)
    app.debug = True




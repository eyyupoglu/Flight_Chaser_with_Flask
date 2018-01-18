from flask import Flask,render_template, url_for, send_from_directory
import requests
from flask import request #in order to be able towork with "GET POST etc "

app = Flask(__name__)


@app.route("/")
@app.route("/mehmet/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/static/<filepath>") 
def css(filepath):
    #the html files calls for css \in the head part of theirs. 
    #So this is another request.
    return send_from_directory('static', filepath)

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
        return "<html> <body><div><h2>it works, and your email : %s \n \
        your password: %s</h2></div></body> </html> " % (email,password)
    return render_template('create_account.html')

@app.route("/sign_in", methods = ['GET', 'POST'])
def sign_in():
    if request.method == 'POST': 
        email = request.form["email"] 
        password = request.form["pwd"]
        return "<html> <body><div><h2>You entered these values : %s \n \
        your password: %s</h2></div></body> </html> " % (email,password)
    return render_template('sign_in.html')
    



if __name__ == "__main__":
    app.run(host="0.0.0.0",    debug = True)




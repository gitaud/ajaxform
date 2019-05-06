from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
	return "Welcome to Flask!"

@app.route("/signup")
def signup():
	return render_template("signup.html")

@app.route("/signUpUser",methods=['POST'])
def signUpUser():
	user = request.form['username'];
	password = request.form['password'];
	return json.dumps({'status':'OK','user':user,'pass':password});

if __name__ == "__main__":
	app.run()
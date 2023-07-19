from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

dct = {"giladvo": "123", "jawadab": "2405", "gutwi": "4292"}
username = "giladvo"
password = "123"
facebook_friends=["Yahli","Jawad","Sam", "Nadeen", "Guy", "Rani"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		username1 = request.form['username'].lower()
		password1 = request.form['password']
		if username1 in dct and password1 == dct[username1]:
			return redirect(url_for('home'))
		else:
			return render_template('login.html')

@app.route('/home')
def home():
	return render_template('home.html', friends = facebook_friends)

@app.route('/friend_exists/<string:name>')
def friend_exists(name):
	return render_template('friend_exists.html', n = name, friends = facebook_friends)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)

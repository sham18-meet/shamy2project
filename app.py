from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from  flask_sqlalchemy import SQLAlchemy 
from flask.ext.session import Session


app = Flask(__name__)
app.debug=True
app.config['SQLAlCHEMY_DATABASE_URI']='sqlite:////tmp/test.db'
db= SQLAlchemy(app)
sess= Session()


class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	email=db.Column(db.String(100), nullable=False)
	pwd=db.Column(db.String(100), nullable=False)


db.create_all()

@app.route('/login_signup')
def login_signup():
	return render_template('login_signup.html')

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/Gallery')
def gallery():
	return render_template('gallery.html')

@app.route('/News')
def news():
	return render_template('News.html')

@app.route('/Statistics')
def Statistics():
	return render_template('statistics.html')

@app.route('/Contact')
def contact():
	return render_template('contact.html')

@app.route('/Button')
def button():
	return render_template('button.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
	if request.method == 'POST':
		user = Users()
		user.email= request.form['email']
		user.pwd=reqyuest.form['pwd']
		db.session.add(user)
		db.session.commit()
		return render_template('home.html', user= user)

	elif request.method=='GET':
		return render_template('login_signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if  request.method=='GET':
		return render_template('home.html', email=email, pwd=pwd)

	elif request.method=='POST':
		user=db.session.query(Users).filter_by(email=request.form['email']).first()
	if user.pwd==request.form.get('pwd'):
		session['logged_in']=True
		return render_template('home.html',user=user)

	else:
		flash('Wrong Password!')
		return render_template('login_signup.html')


if __name__=='__main__':
	#app.secret.key='super.secret.key'
	app.config['SESSION_TYPE']='filesystem'
	sess.init_app(app)
	app.run(debug=True)

		


















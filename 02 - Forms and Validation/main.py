from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

posts = [
	{
		'manufacturer': 'Honda',
		'model': 'Civic i-VTech Oriel 2019',
		'spec': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet laboriosam iure est quis ratione harum consequatur reprehenderit maxime, dolorum tempora natus mollitia sed, porro. Omnis officia nemo, quos optio praesentium.',
		'date_posted': 'July 23, 2019'
	},

	{
		'manufacturer': 'Toyota',
		'model': 'Corolla GLi 2019',
		'spec': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatibus magni reiciendis nesciunt maiores quia eaque rem maxime, voluptas mollitia non. Ut sed aspernatur delectus soluta perspiciatis repellat quod, commodi nemo.',
		'date_posted': 'May 05, 2019'
	}
]

#Instatiate Flask Class
app = Flask(__name__)

#default website route/address which by default shall be the home page i.e. http://localhost:5000
@app.route("/") 
#website route/address with location 'home' http://localhost:5000/home
@app.route("/home") 
def home():
	#Basic 'home page' to display only Hello World directly
	#return "<h1>Hello World</h1>"

	#Return webpage containing template for 'home'
	return render_template('home.html', posts = posts)

#website address with location 'contact' http://localhost:5000/contact
@app.route("/contact")
def contact():
	#Basic 'contact us' to display only Contact Us information directly
	#return "<h1>Contact us at: <i><strong>www.techsflex.net</strong></i>"

	#Return webpage containing template for 'contact'
	return render_template('contact.html', title = 'Contact')

@app.route("/login")
def login():
	#Create form instance
	form = LoginForm()
	#validate form entry i.e. similar ot database without implementing a database
	if form.validate_on_submit():
		if form.email.data == 'admin@admin.com' and form.password.data == 'password':
			flash('Login successful!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Unable to login! Please check username and password', 'danger')
	return render_template('login.html', title='Login')

@app.route("/register")
def register():
	#Create form instance
	form = RegistrationForm()
	#validate form entry
	if form.validate_on_submit():
		flash(f'Account Created: {form.username.data}', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Sign Up')

#Following lines identify procedure when script is run directly from command line instead of being imported
if __name__ == '__main__':
	app.run(debug=True)
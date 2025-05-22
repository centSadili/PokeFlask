from flask import render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .forms import RegistrationForm, LoginForm
from .models import User, db
from flask import Blueprint


main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Welcome {form.username.data}, registration successful!", "success")
        return redirect(url_for("main.home"))
    return render_template("register.html", form=form)

@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Logged in successfully!", "success")
            return redirect(url_for("main.dashboard"))  # change this to your actual protected route
        else:
            flash("Invalid email or password", "danger")
    return render_template("login.html", form=form)

@main.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.login"))

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/about')   
def about():
     return render_template('about.html')
 
@main.route('/products')   
def products():
     return render_template('products.html')
@main.route('/policy')   
def policy():
     return render_template('policy.html')

@main.route('/api/data')
def get_data():
    data={
        'name':'Flask Application',
        'version':'1.0.0'
    }
    return jsonify(data)
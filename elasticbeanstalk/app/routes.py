from flask import Blueprint, render_template, request
from datetime import date
from .models import User
from . import db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        user = User(first_name=first_name, last_name=last_name, dob=dob)
        db.session.add(user)
        db.session.commit()

        dob_date = date.fromisoformat(dob)
        today = date.today()
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
        return render_template('result.html', name=f"{first_name} {last_name}", age=age)
    return render_template('index.html')

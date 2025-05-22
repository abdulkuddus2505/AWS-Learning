from flask import Blueprint, render_template, request, redirect, url_for
from .models import Employee
from . import db

erp_bp = Blueprint("erp", __name__)

@erp_bp.route("/")
def index():
    employees = Employee.query.all()
    return render_template("index.html", employees=employees)

@erp_bp.route("/add", methods=["GET", "POST"])
def add_employee():
    if request.method == "POST":
        emp = Employee(
            name=request.form["name"],
            role=request.form["role"],
            department=request.form["department"]
        )
        db.session.add(emp)
        db.session.commit()
        return redirect(url_for("erp.index"))
    return render_template("add_employee.html")

@erp_bp.route("/delete/<int:emp_id>")
def delete_employee(emp_id):
    emp = Employee.query.get_or_404(emp_id)
    db.session.delete(emp)
    db.session.commit()
    return redirect(url_for("erp.index"))

@erp_bp.route("/edit/<int:emp_id>", methods=["GET", "POST"])
def edit_employee(emp_id):
    emp = Employee.query.get_or_404(emp_id)
    if request.method == "POST":
        emp.name = request.form["name"]
        emp.role = request.form["role"]
        emp.department = request.form["department"]
        db.session.commit()
        return redirect(url_for("erp.index"))
    return render_template("add_employee.html", employee=emp)

from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.deshi import Deshi
import repositories.deshi_repository as deshi_repository

deshis_blueprint = Blueprint("deshis", __name__)

@deshis_blueprint.route("/deshis")
def deshis():
    deshis = deshi_repository.select_all()
    return render_template("deshis/index.html", title = "Deshi", deshis = deshis)

from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.sensei import Sensei
import repositories.sensei_repository as sensei_repository

senseis_blueprint = Blueprint("senseis", __name__)

@senseis_blueprint.route("/senseis")
def senseis():
    senseis = sensei_repository.select_all()
    return render_template("senseis/index.html", title = "Sensei", senseis = senseis)

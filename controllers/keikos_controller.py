from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.keiko import Keiko
import repositories.keiko_repository as keiko_repository

keikos_blueprint = Blueprint("keikos", __name__)

@keikos_blueprint.route("/keikos")
def keikos():
    keikos = keiko_repository.select_all()
    return render_template("keikos/index.html", title = "Keiko", keikos = keikos)

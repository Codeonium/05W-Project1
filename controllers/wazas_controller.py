from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.waza import Waza
import repositories.waza_repository as waza_repository

wazas_blueprint = Blueprint("wazas", __name__)

@wazas_blueprint.route("/wazas")
def wazas():
    wazas = waza_repository.select_all()
    return render_template("wazas/index.html", title = "Waza", wazas = wazas)

@wazas_blueprint.route("/wazas/<id>")
def show(id):
    waza = waza_repository.select(id)
    senseis = waza_repository.senseis(waza)
    deshis = waza_repository.deshis(waza)
    return render_template("wazas/show.html", waza = waza, senseis = senseis, deshis = deshis)
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.waza import Waza

import repositories.waza_repository as waza_repository
import repositories.deshi_repository as deshi_repository
import repositories.sensei_repository as sensei_repository


wazas_blueprint = Blueprint("wazas", __name__)

@wazas_blueprint.route("/wazas")
def wazas():
    wazas = waza_repository.select_all()
    return render_template("wazas/index.html", title = "Waza", all_wazas = wazas)

@wazas_blueprint.route("/wazas/<id>", methods = ['GET'])
def show_waza(id):
    waza = waza_repository.select(id)
    sensei = waza_repository.senseis(waza)
    deshi = waza_repository.deshis(waza)
    return render_template("wazas/show.html", waza = waza, sensei = sensei, deshi = deshi)

@wazas_blueprint.route("/wazas/new", methods=['GET'])
def new_waza():
    deshis = deshi_repository.select_all()
    senseis = sensei_repository.select_all()
    return render_template("wazas/new.html", all_deshis = deshis, all_senseis = senseis)

@wazas_blueprint.route("/wazas",  methods=['POST'])
def create_waza():
    name    = request.form['name']
    waza = Waza(name)
    waza_repository.save(waza)
    return redirect('/wazas')

@wazas_blueprint.route("/wazas/<id>/edit", methods=['GET'])
def edit_waza(id):
    waza = waza_repository.select(id)
    deshis = deshi_repository.select_all()
    senseis = sensei_repository.select_all()
    return render_template('senseis/edit.html', all_deshis = deshis, all_senseis = senseis, waza = waza)

@wazas_blueprint.route("/wazas/<id>", methods=['POST'])
def update_waza(id):
    name    = request.form['name']
    waza  = waza_repository.select(request.form['waza_id'])
    waza = Waza(name, id)
    waza_repository.update(waza)
    return redirect('/wazas')

@wazas_blueprint.route("/wazas/<id>/delete", methods=['POST'])
def delete_waza(id):
    waza_repository.delete(id)
    return redirect('/wazas')

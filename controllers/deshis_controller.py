from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.deshi import Deshi
import repositories.deshi_repository as deshi_repository
import repositories.waza_repository as waza_repository

deshis_blueprint = Blueprint("deshis", __name__)

@deshis_blueprint.route("/deshis")
def deshis():
    deshis = deshi_repository.select_all()
    return render_template("deshis/index.html", title = "Deshi", deshis = deshis)


@deshis_blueprint.route("/deshis/new", methods=['GET'])
def new_deshi():
    wazas = waza_repository.select_all()
    return render_template("deshis/new.html", all_wazas = wazas)


@deshis_blueprint.route("/deshis",  methods=['POST'])
def create_deshi():
    name    = request.form['name']
    waza  = waza_repository.select(request.form['waza_id'])
    deshi = Deshi(name, waza)
    deshi_repository.save(deshi)
    return redirect('/deshis')



@deshis_blueprint.route("/deshis/<id>", methods=['GET'])
def show_deshi(id):
    deshi = deshi_repository.select(id)
    return render_template('deshis/show.html', deshi = deshi)


@deshis_blueprint.route("/deshis/<id>/edit", methods=['GET'])
def edit_deshi(id):
    deshi = deshi_repository.select(id)
    wazas = waza_repository.select_all()
    return render_template('deshis/edit.html', deshi = deshi, all_wazas = wazas)



@deshis_blueprint.route("/deshis/<id>", methods=['POST'])
def update_deshi(id):
    name    = request.form['name']
    waza  = waza_repository.select(request.form['waza_id'])
    deshi = Deshi(name, waza, id)
    print(deshi.waza.name())
    deshi_repository.update(deshi)
    return redirect('/deshis')



@deshis_blueprint.route("/deshis/<id>/delete", methods=['POST'])
def delete_deshi(id):
    deshi_repository.delete(id)
    return redirect('/deshis')

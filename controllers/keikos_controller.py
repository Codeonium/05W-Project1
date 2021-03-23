from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.keiko import Keiko

import repositories.deshi_repository as deshi_repository
import repositories.sensei_repository as sensei_repository
import repositories.waza_repository as waza_repository
import repositories.keiko_repository as keiko_repository

keikos_blueprint = Blueprint("keikos", __name__)

@keikos_blueprint.route("/keikos")
def keikos():
    keikos = keiko_repository.select_all()
    return render_template("keikos/index.html", title = "Keiko", keikos = keikos)

@keikos_blueprint.route("/keikos/new", methods=['GET'])
def new_keiko():
    senseis = sensei_repository.select_all()
    deshis = deshi_repository.select_all()
    return render_template("keikos/new.html", all_deshis = deshis, all_senseis = senseis)

@keikos_blueprint.route("/keikos",  methods=['POST'])
def create_keiko():
    sensei = sensei_repository.select(request.form['sensei_id'])
    time    = request.form['time']
    deshi = deshi_repository.select(request.form['deshi_id'])
    keiko = Keiko(sensei, time, deshi)
    keiko_repository.save(keiko)
    return redirect('/keikos')

@keikos_blueprint.route("/keikos/<id>", methods=['GET'])
def show_keiko(id):
    keiko = keiko_repository.select(id)
    return render_template('keikos/show.html', keiko = keiko)

@keikos_blueprint.route("/keikos/<id>/edit", methods=['GET'])
def edit_keiko(id):
    keiko = keiko_repository.select(id)
    senseis = sensei_repository.select_all()
    deshis = deshi_repository.select_all()
    return render_template('keikos/edit.html', keiko = keiko, all_senseis = senseis, all_deshis = deshis)

@keikos_blueprint.route("/keikos/<id>", methods=['POST'])
def update_keiko(id):
    sensei = sensei_repository.select(request.form['sensei_id'])
    time    = request.form['time']
    deshi = deshi_repository.select(request.form['deshi_id'])
    keiko = Keiko(sensei, time, deshi, id)
    print(keiko.sensei.name())
    keiko_repository.update(keiko)
    return redirect('/keikos')

@keikos_blueprint.route("/keikos/<id>/delete", methods=['POST'])
def delete_keiko(id):
    keiko_repository.delete(id)
    return redirect('/keikos')

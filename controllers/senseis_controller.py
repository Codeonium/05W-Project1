from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.sensei import Sensei
import repositories.sensei_repository as sensei_repository
import repositories.waza_repository as waza_repository

senseis_blueprint = Blueprint("senseis", __name__)

@senseis_blueprint.route("/senseis")
def senseis():
    senseis = sensei_repository.select_all()
    return render_template("senseis/index.html", title = "Sensei", senseis = senseis)


@senseis_blueprint.route("/senseis/new", methods=['GET'])
def new_sensei():
    wazas = waza_repository.select_all()
    return render_template("senseis/new.html", all_wazas = wazas)


@senseis_blueprint.route("/senseis",  methods=['POST'])
def create_sensei():
    name    = request.form['name']
    waza  = waza_repository.select(request.form['waza_id'])
    sensei = Sensei(name, waza)
    sensei_repository.save(sensei)
    return redirect('/senseis')



@senseis_blueprint.route("/senseis/<id>", methods=['GET'])
def show_sensei(id):
    sensei = sensei_repository.select(id)
    return render_template('senseis/show.html', sensei = sensei)


@senseis_blueprint.route("/senseis/<id>/edit", methods=['GET'])
def edit_sensei(id):
    sensei = sensei_repository.select(id)
    wazas = waza_repository.select_all()
    return render_template('senseis/edit.html', sensei = sensei, all_wazas = wazas)



@senseis_blueprint.route("/senseis/<id>", methods=['POST'])
def update_sensei(id):
    name    = request.form['name']
    waza  = waza_repository.select(request.form['waza_id'])
    sensei = Sensei(name, waza, id)
    print(sensei.waza.name())
    sensei_repository.update(sensei)
    return redirect('/senseis')



@senseis_blueprint.route("/senseis/<id>/delete", methods=['POST'])
def delete_sensei(id):
    sensei_repository.delete(id)
    return redirect('/senseis')

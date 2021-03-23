from db.run_sql import run_sql

from models.deshi import Deshi
from models.keiko import Keiko
from models.sensei import Sensei
import repositories.deshi_repository as deshi_repository
import repositories.sensei_repository as sensei_repository

def save (keiko):
    sql = "INSERT INTO keikos ( sensei_id, time, deshi_id) VALUES (%s, %s, %s) RETURNING id"
    values = [keiko.sensei.id, keiko.time, keiko.deshi.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    keiko.id = id


def select_all():
    keikos = []
    sql = "SELECT * FROM keikos"
    results = run_sql(sql)
    for result in results:
        deshi = deshi_repository.select(result["id"])
        sensei = sensei_repository.select(result["id"])
        keiko = Keiko(sensei, result["time"], deshi, result["id"])
        keikos.append(keiko)
    return keikos


def select(id):
    sql = "SELECT * FROM keikos WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    deshi = deshi_repository.select(result["id"])
    sensei = sensei_repository.select(result["id"])
    keiko = Keiko(sensei, result["time"], deshi, result["id"])
    return keiko


def delete_all():
    sql = "DELETE FROM keikos"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM keikos WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(keiko):
    sql = "UPDATE keikos SET (sensei_id, time, deshi_id) = (%s, %s, %s) WHERE id = %s"
    values = [keiko.sensei.id, keiko.time, keiko.deshi.id, keiko.id]
    run_sql(sql, values)


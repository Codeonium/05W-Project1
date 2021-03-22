from db.run_sql import run_sql

from models.waza import Waza
from models.sensei import Sensei
import repositories.waza_repository as waza_repository





def save(sensei):
    sql = "INSERT INTO senseis (name, level, waza_id) VALUES (%s, %s, %s) RETURNING id"
    values = [sensei.name, sensei.waza.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    sensei.id = id


def select_all():
    senseis = []
    sql = "SELECT * FROM senseis"
    results = run_sql(sql)
    for result in results:
        waza = waza_repository.select(result["waza_id"])
        sensei = Sensei(result["name"], waza, result["id"])
        senseis.append(sensei)
    return senseis


def select(id):
    sql = "SELECT * FROM senseis WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    waza = waza_repository.select(result["waza_id"])
    sensei = Sensei(result["name"], waza, result["id"])
    return sensei


def delete_all():
    sql = "DELETE FROM senseis"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM senseis WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(sensei):
    sql = "UPDATE senseis SET (name, level, waza_id) = (%s, %s, %s) WHERE id = %s"
    values = [sensei.name, sensei.waza.id, sensei.id]
    run_sql(sql, values)


def select_waza_learned(id):
    wazas = []
    sql = "SELECT wazas.* FROM wazas INNER JOIN keikos ON keikos.waza_id = wazas.id WHERE keikos.waza_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        waza = Waza(result["name"])
        wazas.append(waza)
    return wazas

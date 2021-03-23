from db.run_sql import run_sql

from models.waza import Waza
from models.sensei import Sensei
import repositories.waza_repository as waza_repository





def save(sensei):
    sql = "INSERT INTO senseis (name) VALUES (%s) RETURNING id"
    values = [sensei.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    sensei.id = id


def select_all():
    senseis = []
    sql = "SELECT * FROM senseis"
    results = run_sql(sql)
    for result in results:
        waza = waza_repository.select(result["id"])
        sensei = Sensei(result["name"], waza, result["id"])
        senseis.append(sensei)
    return senseis


def select(id):
    sql = "SELECT * FROM senseis WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    waza = waza_repository.select(result["id"])
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
    sql = "UPDATE senseis SET (name, waza_id) = (%s, %s) WHERE id = %s"
    values = [sensei.name, sensei.waza.id, sensei.id]
    run_sql(sql, values)


def wazas(sensei):
    wazas = []

    sql = "SELECT wazas.* FROM wazas INNER JOIN keikos ON keikos.sensei_id = sensei.id WHERE sensei_id = %s"
    values = [sensei.id]
    results = run_sql(sql, values)

    for row in results:
        waza = Waza(row['name'], row['id'] )
        wazas.append(waza)
    return wazas

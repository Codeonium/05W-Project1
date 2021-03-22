from db.run_sql import run_sql

from models.waza import Waza
from models.sensei import Sensei
from models.deshi import Deshi


def save(waza):
    sql = "INSERT INTO wazas (name) VALUES (%s) RETURNING *"
    values = [waza.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    waza.id = id
    return waza


def select_all():
    wazas = []

    sql = "SELECT * FROM wazas"
    results = run_sql(sql)

    for row in results:
        waza = Waza(row['name'], row['id'] )
        wazas.append(waza)
    return wazas


def select(id):
    waza = None
    sql = "SELECT * FROM wazas WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        waza = Waza(result['name'], result['id'] )
    return waza


def delete_all():
    sql = "DELETE  FROM wazas"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM wazas WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(waza):
    sql = "UPDATE wazas SET (name) = (%s) WHERE id = %s"
    values = [waza.name, waza.id]
    run_sql(sql, values)

def senseis(waza):
    senseis = []

    sql = "SELECT senseis.* FROM senseis INNER JOIN keikos ON keikos.waza_id = waza.id WHERE waza_id = %s"
    values = [waza.id]
    results = run_sql(sql, values)

    for row in results:
        sensei = Sensei(row['name'], row['waza_id'], row['id'] )
        senseis.append(sensei)
    return senseis

def deshis(waza):
    deshis = []

    sql = "SELECT deshis.* FROM deshis INNER JOIN keikos ON keikos.waza_id = waza.id WHERE waza_id = %s"
    values = [waza.id]
    results = run_sql(sql, values)

    for row in results:
        deshi = Deshi(row['name'], row['level'], row['waza_id'], row['id'] )
        deshis.append(deshi)
    return deshis

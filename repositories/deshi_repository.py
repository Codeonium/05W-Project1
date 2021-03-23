from db.run_sql import run_sql

from models.waza import Waza
from models.deshi import Deshi
import repositories.waza_repository as waza_repository



def save(deshi):
    sql = "INSERT INTO deshis (name) VALUES (%s) RETURNING id"
    values = [deshi.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    deshi.id = id


def select_all():
    deshis = []
    sql = "SELECT * FROM deshis"
    results = run_sql(sql)
    for row in results:
        waza = waza_repository.select(row["id"])
        deshi = Deshi(row["name"], row["level"], waza, row["id"])
        deshis.append(deshi)
    return deshis


def select(id):
    sql = "SELECT * FROM deshis WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    waza = waza_repository.select(result["id"])
    deshi = Deshi(result["name"], result["level"], waza, result["id"])
    return deshi


def delete_all():
    sql = "DELETE FROM deshis"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM deshis WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(deshi):
    sql = "UPDATE deshis SET (name, level, waza_id) = (%s, %s, %s) WHERE id = %s"
    values = [deshi.name, deshi.level, deshi.waza.id, deshi.id]
    run_sql(sql, values)


def select_waza_learned(id):
    wazas = []
    sql = "SELECT wazas.* FROM wazas INNER JOIN keikos ON keikos.waza_id = wazas.id WHERE keikos.waza_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        waza = Waza(row["name"])
        wazas.append(waza)
    return wazas
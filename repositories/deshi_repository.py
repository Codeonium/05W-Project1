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
        deshi = Deshi(row["name"], waza, row["id"])
        deshis.append(deshi)
    return deshis


def select(id):
    sql = "SELECT * FROM deshis WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    waza = waza_repository.select(result["id"])
    deshi = Deshi(result["name"], waza, result["id"])
    return deshi


def delete_all():
    sql = "DELETE FROM deshis"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM deshis WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(deshi):
    sql = "UPDATE deshis SET (name, waza_id) = (%s, %s) WHERE id = %s"
    values = [deshi.name, deshi.waza.id, deshi.id]
    run_sql(sql, values)


def wazas(deshi):
    wazas = []

    sql = "SELECT wazas.* FROM wazas INNER JOIN keikos ON keikos.deshi_id = deshi.id WHERE deshi_id = %s"
    values = [deshi.id]
    results = run_sql(sql, values)

    for row in results:
        waza = Waza(row['name'], row['id'] )
        wazas.append(waza)
    return wazas

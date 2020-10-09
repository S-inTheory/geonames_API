import json
import os
import sqlite3

from geonames_API.settings import BASE_DIR


def json_to_db():
    json_file = os.path.join(BASE_DIR, '../static', '../static/geonames.json')
    db_file = '../db.sqlite3'

    traffic = json.load(open(json_file))
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    id = 0

    for data in traffic:
        id += 1
        cursor.execute("Insert into gAPI_geoname values (?, ?, ?, ?, ?, ?, ?,"
                       " ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (
                           id, data['geonameid'], data['name'],
                           data['asciiname'], data['alternatenames'],
                           data['latitude'], data['longtitude'],
                           data['feature_class'], data['feature_code'],
                           data['country_code'], data['cc2'],
                           data['admin1_code'], data['admin2_code'],
                           data['admin3_code'], data['admin4_code'],
                           data['population'], data['elevation'],
                           data['dem'], data['timezone'],
                           data['modification_date'])
                       )
    connection.commit()


if __name__ == '__main__':
    json_to_db()

from flask import Flask, jsonify, abort
import mariadb

app = Flask(__name__)

# Database connection parameters
db_config = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "root",
    "database": "flight_sim"
}


def get_airport_info(icao_code):
    try:
        conn = mariadb.connect(**db_config)
        cursor = conn.cursor()

        query = "SELECT icao_code, name, location FROM Airport WHERE icao_code = ?"
        cursor.execute(query, (icao_code,))

        row = cursor.fetchone()

        cursor.close()
        conn.close()

        if row:
            return {"ICAO": row[0], "Name": row[1], "Location": row[2]}
        else:
            return None

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB: {e}")
        return None


@app.route('/Mod_13_2/<string:icao_code>', methods=['GET'])
def get_airport(icao_code):
    airport_info = get_airport_info(icao_code)

    if airport_info:
        return jsonify(airport_info)
    else:
        abort(404, description="Airport not found")


if __name__ == '__main__':
    app.run(debug=True)
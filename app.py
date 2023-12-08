# app.py
from flask import Flask, request, jsonify, make_response
from dbhelpers import run_statement, serialize_data
import json
from db_connector import create_connection

app = Flask(__name__)

animal_cols = ['id', 'name', 'species']

def get_db_cursor():
    conn = create_connection()
    return conn.cursor() if conn else None


@app.get('/api/animals')
def get_all_animals():
 try:
  result = run_statement('CALL get_all_animals()')
  print(result)
  print(result[0])
  formatted_animals = serialize_data(animal_cols, result)
  return make_response(jsonify(formatted_animals), 200)
 except Exception as error:
  return make_response(error, 200)


@app.get('/api/dogs')
def get_all_dogs():
    try:
        result = run_statement('CALL get_all_dogs()')
        print(result)
        print(result[0])
        formatted_dogs = serialize_data(animal_cols, result)
        return make_response(jsonify(formatted_dogs), 200)
    except Exception as error:
        return make_response(error, 200)

    # cursor = get_db_cursor()
    # if cursor:
    #     cursor.callproc('get_all_dogs')
    #     data = cursor.fetchall()
    #     cursor.close()
    #     return jsonify(data)
    # else:
    #     return jsonify({'error': 'Database connection error'})

@app.route('/api/cats', methods=['GET'])
def get_all_cats():
    try:
        result = run_statement('CALL get_all_cats()')
        print(result)
        print(result[0])
        formatted_cats = serialize_data(animal_cols, result)
        return make_response(jsonify(formatted_cats), 200)
    except Exception as error:
        return make_response(error, 200)

app.run(debug=True)

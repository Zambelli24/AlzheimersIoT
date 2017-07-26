from flask import Flask, request
from pymongo import MongoClient
from flask_pymongo import PyMongo
import time
import string
from db_wrapper import DatabaseWrapper
from helper_methods import HelperMethods
import json

app = Flask(__name__)

@app.route('/add_key', methods=['POST'])
def add_key():

	key = request.form['key']

	db = DatabaseWrapper()

	if HelperMethods.check_incorrect_key_format(key):
		raise Exception('The key is not in the specified format.')

	if db.check_key_is_enabled(key):
		return "The specified key has already been enabled"

	db.add_key(key)

	return "Key successfully enabled"

@app.route('/keys_list', methods=['GET'])
def view_keys_list():

	db = DatabaseWrapper()

	return str(db.get_keys())

@app.route('/add_data', methods=['POST'])
def add_data():

	key = request.form['key']
	time = request.form['time']
	data = request.form['data']

	db = DatabaseWrapper()

	if not db.check_key_is_enabled(key):
		raise Exception('The specified key does not exist')

	checked_time = HelperMethods.check_time(time)

	data = json.loads(data)

	db.post_new_data(key, data, checked_time)

	return "Data uploaded successfully"

@app.route('/view_data_since', methods=['GET'])
def view_data_since():

	key = request.form['key']
	time = request.form['time']

	db = DatabaseWrapper()

	if not db.check_key_is_enabled(key):
		raise Exception('The specified key does not exist')

	checked_time = HelperMethods.check_time(time)

	return str(db.get_data_since(key, checked_time))

@app.route('/view_most_recent_data', methods=['GET'])
def view_most_recent_data():

	key = request.form['key']

	db = DatabaseWrapper()

	if not db.check_key_is_enabled(key):
		raise Exception('The specified key does not exist')

	return str(db.get_most_recent_data(key))

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True, port=8080)

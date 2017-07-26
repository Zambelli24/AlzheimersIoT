from pymongo import MongoClient
from flask_pymongo import PyMongo
from datetime import datetime, timezone
import iso8601
import json

class DatabaseWrapper():

    def __init__(self):
        self.database = MongoClient('172.19.0.2', 27017)

    def clear_database(self):
        self.database.availablekeys.keyslist.delete_many({})
        self.database.recordeddata.data.delete_many({})

    def get_keys(self):
        db = self.database.availablekeys.keyslist
        return_list = []
        for key in db.find():
            return_list.append(str(key['name']))
        return return_list

    def check_key_is_enabled(self, key):
        db = self.database.availablekeys.keyslist
        for db_key in db.find():
            if key == str(db_key['name']):
                return True
        return False

    def add_key(self, key):
        db = self.database.availablekeys.keyslist
        db.insert_one({'name': key})

    def post_new_data(self, key, data, time):
        db = self.database.recordeddata.data
        db.insert_one({'key': key, 'time': time, 'data': data})

    def get_data_since(self, key, checked_time):
        db = self.database.recordeddata.data
        return_dict = {}
        unaware_current_time = datetime.now(timezone.utc)
        current_time = unaware_current_time.astimezone()
        for data_piece in db.find():
            if data_piece['key'] == key:
                data_time = iso8601.parse_date(str(data_piece['time']))
                if data_time > checked_time and data_time < current_time:
                    return_dict[str(data_piece['time'])] = json.dumps(data_piece['data'])
        return return_dict

    def get_most_recent_data(self, key):
        db = self.database.recordeddata.data
        return_value = {}
        for data_piece in db.find():
            if data_piece['key'] == key:
                data_time = iso8601.parse_date(str(data_piece['time']))
                if return_value == {} or data_time > time:
                    return_value.clear()
                    time = data_time
                    return_value[str(data_piece['time'])] = json.dumps(data_piece['data'])
        return return_value

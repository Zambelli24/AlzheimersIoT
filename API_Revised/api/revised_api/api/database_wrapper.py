from redis import Redis
import time

class InitializeDB():

    def __init__(self, database):
        self.database = database

class DatabaseWrapper():

    def __init__(self):
        self.database = Redis(host='localhost', port='6379')

    def get_keys(self):
        return self.database.lrange('keys', 0, -1)

    def check_key_is_enabled(self, key):
        for db_key in self.database.lrange('keys', 0, -1):
            if key == db_key.decode('UTF-8'):
                return True

    def add_key(self, key):
        self.database.lpush('keys', key)

    def check_enabled_key_in_list(self, key):
        for db_key in self.database.lrange('keys', 0, -1):
            if key == db_key:
                return key

    def post_new_data(self, key, data, time):
        self.database.zadd(key, data, time)

    def get_data_since(self, key, checked_time):
        return_dict = {}
        current_time = int(time.time())
        for data in self.database.zrange(key, 0, -1):
            data = data.decode('UTF-8')
            timestamp = self.database.zscore(key, data)
            if timestamp > checked_time and timestamp < current_time:
                return_dict[timestamp] = data
        return return_dict

    def get_most_recent_data(self, key):
        data = self.database.zrange(key, -2, -1)
        data = data[-1].decode('UTF-8')
        return_value = {}
        return_value[self.database.zscore(key, data)] = data
        return return_value

    def check_key_in_enabled_list(self, key):
        for db_key in self.database.lrange('keys', 0, -1):
            if key == db_key.decode('UTF-8'):
                return key
        raise Exception("The key requested was not found in the \
            database as an active key.")

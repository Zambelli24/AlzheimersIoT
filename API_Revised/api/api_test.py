import os
from revised_api.api.keys_list import KeysList
from revised_api.api.add_key import AddKey
from revised_api.api.add_data import AddData
from revised_api.api.view_data_since import ViewDataSince
from revised_api.api.view_most_recent_data import ViewMostRecentData
import unittest
import tempfile
import redis
import testing.redis
import json



class RevisedAPITestCase(unittest.TestCase):

    def setUp(self):
        self.redis = testing.redis.RedisServer()
        with self.redis as redis_server:
            fake_db = redis.Redis(**redis_server.dsn())

    def tearDown(self):
        self.redis.stop()

    def test_no_keys(self):
        self.setUp()
        no_keys = KeysList.get()
        self.assertFalse(no_keys)
        self.tearDown()

    def test_add_key(self):
        with self.redis as redis_server:
            fake_db = redis.Redis(**redis_server.dsn())
            one_key = AddKey.post('fitbit')
            assert 'Key successfully enabled' == one_key

            key_exists = KeysList.get()
            assert b'fitbit' in key_exists

    def test_add_bad_key(self):
        with self.redis as redis_server:
            fake_db = redis.Redis(**redis_server.dsn())
            self.assertRaises(Exception, AddKey.post, '_fitbit')

    def test_add_same_key_twice(self):
        with self.redis as redis_server:
            fake_db = redis.Redis(**redis_server.dsn())
            first_add = AddKey.post('fitbit')
            assert 'Key successfully enabled' == first_add
            key_exists = KeysList.get()
            assert b'fitbit' in key_exists

            second_add = AddKey.post('fitbit')
            assert 'The specified key has already been enabled' == second_add
            key_still_exists = KeysList.get()
            assert b'fitbit' in key_still_exists

    def test_add_multiple_keys(self):
        with self.redis as redis_server:
            fake_db = redis.Redis(**redis_server.dsn())
            first_add = AddKey.post('fitbit')
            assert 'Key successfully enabled' == first_add
            key_exists = KeysList.get()
            assert b'fitbit' in key_exists

            second_add = AddKey.post('apple_watch')
            assert 'Key successfully enabled' == second_add
            multiple_keys = KeysList.get()
            assert b'fitbit' in multiple_keys
            assert b'apple_watch' in multiple_keys

            third_add = AddKey.post('smart_phone')
            assert 'Key successfully enabled' == third_add
            multiple_keys = KeysList.get()
            assert b'fitbit' in multiple_keys
            assert b'apple_watch' in multiple_keys
            assert b'smart_phone' in multiple_keys

    def test_add_data_no_key(self):
        with self.redis as redis_server:
            fake_db = redis.Redis(**redis_server.dsn())
            self.assertRaises(Exception, AddData.post,
                'fitbit', '45', 'something')

    def test_add_data_good_key(self):
        with self.redis as redis_server:
            fake_db = redis.Redis(**redis_server.dsn())
            new_key = AddKey.post('fitbit')
            json_obj = json.dumps({'data': 'something'})
            new_data = AddData.post('fitbit', '45', json_obj)
            time_and_data = {}
            time_and_data[45.0] = json_obj
            assert 'Data uploaded successfully' == new_data

            view_last = ViewMostRecentData.get('fitbit')
            assert time_and_data == view_last

            view_all = ViewDataSince.get('fitbit', '0')
            assert time_and_data == view_all

    def test_add_multiple_data_points(self):
        with self.redis as redis_server:
            fake_db = redis.Redis(**redis_server.dsn())
            new_key = AddKey.post('fitbit')
            json_obj = json.dumps({'data': 'something'})
            new_data = AddData.post('fitbit', '45', json_obj)
            all_data = {}
            all_data[45.0] = json_obj
            assert 'Data uploaded successfully' == new_data

            json_obj2 = json.dumps({'data': 'something else'})
            all_data[50.0] = json_obj2
            more_data = AddData.post('fitbit', '50', json_obj2)
            view_all = ViewDataSince.get('fitbit', '0')
            assert all_data == view_all

            most_recent_data = {}
            most_recent_data[50.0] = json_obj2
            view_last = ViewMostRecentData.get('fitbit')
            assert most_recent_data == view_last

if __name__ == '__main__':
    unittest.main()
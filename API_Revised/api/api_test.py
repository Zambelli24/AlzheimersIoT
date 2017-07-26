from revised_api.api.keys_list import KeysList
from revised_api.api.add_key import AddKey
from revised_api.api.add_data import AddData
from revised_api.api.view_data_since import ViewDataSince
from revised_api.api.view_most_recent_data import ViewMostRecentData
from revised_api.api.database_wrapper import DatabaseWrapper
import unittest
import json

class RevisedAPITestCase(unittest.TestCase):

    def setUp(self):
        db = DatabaseWrapper()
        db.clear_database()

    def tearDown(self):
        db = DatabaseWrapper()
        db.clear_database()

    def test_no_keys(self):
        no_keys = KeysList.get(self)
        assert no_keys == []

    def test_add_key(self):
        one_key = AddKey.post('fitbit')
        assert 'Key successfully enabled' == one_key

        key_exists = KeysList.get(self)
        assert ['fitbit'] == key_exists

    def test_add_key_incorrect_format(self):
        self.assertRaises(Exception, AddKey.post, '_fitbit')
        self.assertRaises(Exception, AddKey.post, 'Fitbit')
        self.assertRaises(Exception, AddKey.post, '9fitbit')
        self.assertRaises(Exception, AddKey.post, 'fit$bit')

    def test_add_same_key_twice(self):
        first_add = AddKey.post('fitbit')
        assert 'Key successfully enabled' == first_add
        key_exists = KeysList.get(self)
        assert ['fitbit'] == key_exists

        second_add = AddKey.post('fitbit')
        assert 'The specified key has already been enabled' == second_add
        key_still_exists = KeysList.get(self)
        assert ['fitbit'] == key_still_exists

    def test_add_multiple_keys(self):
        first_add = AddKey.post('fitbit')
        assert 'Key successfully enabled' == first_add
        key_exists = KeysList.get(self)
        assert ['fitbit'] == key_exists

        second_add = AddKey.post('apple_watch')
        assert 'Key successfully enabled' == second_add
        multiple_keys = KeysList.get(self)
        assert 'fitbit' in multiple_keys
        assert 'apple_watch' in multiple_keys

        third_add = AddKey.post('smart_phone')
        assert 'Key successfully enabled' == third_add
        multiple_keys = KeysList.get(self)
        assert 'fitbit' in multiple_keys
        assert 'apple_watch' in multiple_keys
        assert 'smart_phone' in multiple_keys

    def test_add_and_get_data_no_key(self):
        self.assertRaises(Exception, AddData.post, 'fitbit', '2017', 'something')
        self.assertRaises(Exception, ViewDataSince.get, 'fitbit', '2017-07-05T06:37:55')
        self.assertRaises(Exception, ViewMostRecentData.get, 'fitbit')

    def test_add_data_good_key(self):
        new_key = AddKey.post('fitbit')
        json_obj = json.dumps({'data': 'something'})
        new_data = AddData.post('fitbit', '2017-07-05T06:37:55', json_obj)
        time_and_data = {}
        time_and_data['2017-07-05T06:37:55'] = json_obj
        assert 'Data uploaded successfully' == new_data

        view_last = ViewMostRecentData.get('fitbit')
        assert time_and_data == view_last

        view_all = ViewDataSince.get('fitbit', '2017-03-15T03')
        assert time_and_data == view_all

    def test_add_multiple_data_points(self):
        new_key = AddKey.post('fitbit')
        json_obj = json.dumps({'data': 'something'})
        new_data = AddData.post('fitbit', '2017-07-05T06:37:55', json_obj)
        all_data = {}
        all_data['2017-07-05T06:37:55'] = json_obj
        assert 'Data uploaded successfully' == new_data

        json_obj2 = json.dumps({'data': 'something else'})
        all_data['2017-07-05T10:37:55'] = json_obj2
        AddData.post('fitbit', '2017-07-05T10:37:55', json_obj2)
        view_all = ViewDataSince.get('fitbit', '2015-03-10T05')
        assert all_data == view_all

        most_recent_data = {}
        most_recent_data['2017-07-05T10:37:55'] = json_obj2
        view_last = ViewMostRecentData.get('fitbit')
        assert most_recent_data == view_last

    def test_get_data_returns_empty_list(self):
        new_key = AddKey.post('fitbit')
        no_data = ViewDataSince.get('fitbit', '2017-07-05T06:37:55')
        assert no_data == {}

        no_recent_data = ViewMostRecentData.get('fitbit')
        assert no_recent_data == {}

    def test_good_format_datetime(self):
        new_key = AddKey.post('fitbit')
        json_obj = json.dumps({'data': 'something'})
        AddData.post('fitbit', '2017-05-23T06:45:26', json_obj)
        AddData.post('fitbit', '2017-05-23T06:04', json_obj)

    def test_bad_format_datetime(self):
        new_key = AddKey.post('fitbit')
        json_obj = json.dumps({'data': 'something'})
        self.assertRaises(Exception, AddData.post, 'fitbit', '201-05-23T06:45:26', json_obj)
        self.assertRaises(Exception, AddData.post, 'fitbit', '2017-05-2306:45:26', json_obj)
        self.assertRaises(Exception, AddData.post, 'fitbit', '6000', json_obj)
        self.assertRaises(Exception, AddData.post, 'fitbit', '2017-10-20', json_obj)

    def test_add_with_future_time(self):
        new_key = AddKey.post('fitbit')
        json_obj = json.dumps({'data': 'something'})
        self.assertRaises(Exception, AddData.post, 'fitbit', '2019-08-12T08', json_obj)

    def test_add_non_json_object(self):
        new_key = AddKey.post('fitbit')
        self.assertRaises(Exception, AddData.post, 'fitbit', '2017-03-03T08:55:13', 'words')
        self.assertRaises(Exception, AddData.post, 'fitbit', '2017-03-03T08:55:13', {'words'})

    def test_add_empty_json_object(self):
        new_key = AddKey.post('fitbit')
        data = {}
        json_obj = json.dumps({})
        data['2017-05-14T08:54:12'] = json_obj
        AddData.post('fitbit', '2017-05-14T08:54:12', json_obj)
        view_last = ViewMostRecentData.get('fitbit')
        assert view_last == data

        view_all = ViewDataSince.get('fitbit', '2017-01-01T12')
        assert view_all == data


if __name__ == '__main__':
    unittest.main()
import unittest
import json
import requests
from db_wrapper import DatabaseWrapper
import ast

class RevisedAPITestCase(unittest.TestCase):

    def setUp(self):
        db = DatabaseWrapper()
        db.clear_database()

    def tearDown(self):
        db = DatabaseWrapper()
        db.clear_database()

    def test_no_keys(self):
        no_keys = requests.get('http://localhost:5000/keys_list')
        assert ast.literal_eval(no_keys.text) == []

    def test_add_key(self):
        one_key = requests.post('http://localhost:5000/add_key', data={'key': 'fitbit'})
        assert 'Key successfully enabled' == one_key.text

        key_exists = requests.get('http://localhost:5000/keys_list')
        assert ['fitbit'] == ast.literal_eval(key_exists.text)

    def test_add_key_incorrect_format(self):
        url = 'http://localhost:5000/add_key'
        data = {'key': '_fitbit'}
        r = requests.post(url=url, data=data)
        key_not_exists = requests.get('http://localhost:5000/keys_list')
        assert '_fitbit' not in key_not_exists.text

        data = {'key': 'Fitbit'}
        requests.post(url=url, data=data)
        key_not_exists = requests.get('http://localhost:5000/keys_list')
        assert 'Fitbit' not in key_not_exists.text

        data = {'key': '9fitbit'}
        requests.post(url=url, data=data)
        key_not_exists = requests.get('http://localhost:5000/keys_list')
        assert '9fitbit' not in key_not_exists.text

        data = {'key': 'fit$bit'}
        requests.post(url=url, data=data)
        key_not_exists = requests.get('http://localhost:5000/keys_list')
        assert 'fit$bit' not in key_not_exists.text

    def test_add_same_key_twice(self):
        key = {'key': 'fitbit'}
        requests.post('http://localhost:5000/add_key', data=key)
        key_exists = requests.get('http://localhost:5000/keys_list')
        assert ['fitbit'] == ast.literal_eval(key_exists.text)

        no_add = requests.post('http://localhost:5000/add_key', data=key)
        assert no_add.text == "The specified key has already been enabled"
        key_exists = requests.get('http://localhost:5000/keys_list')
        assert ['fitbit'] == ast.literal_eval(key_exists.text)

    def test_add_multiple_keys(self):
        key = {'key': 'fitbit'}
        requests.post('http://localhost:5000/add_key', data=key)
        key_exists = requests.get('http://localhost:5000/keys_list')
        assert 'fitbit' in ast.literal_eval(key_exists.text)

        key2 = {'key': 'smartwatch'}
        requests.post('http://localhost:5000/add_key', data=key2)
        key_exists = requests.get('http://localhost:5000/keys_list')
        assert 'fitbit' in ast.literal_eval(key_exists.text)
        assert 'smartwatch' in ast.literal_eval(key_exists.text)

        key3 = {'key': 'apple_watch'}
        requests.post('http://localhost:5000/add_key', data=key3)
        key_exists = requests.get('http://localhost:5000/keys_list')
        assert 'fitbit' in ast.literal_eval(key_exists.text)
        assert 'smartwatch' in ast.literal_eval(key_exists.text)
        assert 'apple_watch' in ast.literal_eval(key_exists.text)

    def test_add_and_get_data_no_key(self):
        data = {'key': 'fitbit', 'time': '2017-07-05T06:37:55', 'data': 'something'}
        response = requests.post('http://localhost:5000/add_data', data=data)
        assert response.status_code == 500

        data = {'key': 'fitbit', 'time': '2017-07-05T06:37:55'}
        response1 = requests.get('http://localhost:5000/view_data_since', data=data)
        assert response1.status_code == 500

        data = {'key': 'fitbit'}
        response3 = requests.get('http://localhost:5000/view_most_recent_data', data=data)
        assert response3.status_code == 500

    def test_add_data_good_key(self):
        requests.post('http://localhost:5000/add_key', data={'key': 'fitbit'})
        json_obj = json.dumps({'data': 'something'})
        data = {'key': 'fitbit', 'time': '2017-07-05T06:37:55', 'data': json_obj}
        new_data = requests.post('http://localhost:5000/add_data', data=data)
        time_and_data = {}
        time_and_data['2017-07-05 06:37:55'] = json_obj
        assert 'Data uploaded successfully' == new_data.text

        view_last = requests.get('http://localhost:5000/view_most_recent_data', data={'key':'fitbit'})
        assert time_and_data == ast.literal_eval(view_last.text)

        data = {'key': 'fitbit', 'time': '2017-03-15T03'}
        view_all = requests.get('http://localhost:5000/view_data_since', data=data)
        assert time_and_data == ast.literal_eval(view_all.text)

    def test_get_data_returns_empty_list(self):
        requests.post('http://localhost:5000/add_key', data={'key': 'fitbit'})
        data = {'key': 'fitbit', 'time': '2017-02-02T05'}
        no_data = requests.get('http://localhost:5000/view_data_since', data=data)
        assert ast.literal_eval(no_data.text) == {}

        no_recent_data = requests.get('http://localhost:5000/view_most_recent_data', data={'key': 'fitbit'})
        assert ast.literal_eval(no_data.text) == {}

    def test_good_format_datetime(self):
        requests.post('http://localhost:5000/add_key', data={'key': 'fitbit'})
        json_obj = json.dumps({'data': 'something'})
        data1 = {'key': 'fitbit', 'time': '2017-05-23T06:45:26', 'data': json_obj}
        add1 = requests.post('http://localhost:5000/add_data', data=data1)
        assert add1.status_code == 200

        data2 = {'key': 'fitbit', 'time': '2017-05-23T06:04', 'data': json_obj}
        add2 = requests.post('http://localhost:5000/add_data', data=data2)
        assert add2.status_code == 200

    def test_bad_format_datetime(self):
        requests.post('http://localhost:5000/add_key', data={'key': 'fitbit'})
        json_obj = json.dumps({'data': 'something'})
        data1 = {'key': 'fitbit', 'time': '2017', 'data': json_obj}
        add1 = requests.post('http://localhost:5000/add_data', data=data1)
        assert add1.status_code == 500

        data2 = {'key': 'fitbit', 'time': '2017-05-23T00', 'data': json_obj}
        add2 = requests.post('http://localhost:5000/add_data', data=data2)
        assert add2.status_code == 500

        data3 = {'key': 'fitbit', 'time': '600', 'data': json_obj}
        add3 = requests.post('http://localhost:5000/add_data', data=data3)
        assert add3.status_code == 500

    def test_add_with_future_time(self):
        requests.post('http://localhost:5000/add_key', data={'key': 'fitbit'})
        json_obj = json.dumps({'data': 'something'})
        data = {'key': 'fitbit', 'time': '2017', 'data': json_obj}

        bad_add = requests.post('http://localhost:5000/add_data', data=data)
        assert bad_add.status_code == 500

    def test_add_non_json_object(self):
        requests.post('http://localhost:5000/add_key', data={'key': 'fitbit'})
        data = {'key': 'fitbit', 'time': '2017-05-03T09', 'data': 'something'}

        bad_add = requests.post('http://localhost:5000/add_data', data=data)
        assert bad_add.status_code == 500

        data1 = {'key': 'fitbit', 'time': '2017-05-03T09', 'data': {'something'}}
        bad_add1 = requests.post('http://localhost:5000/add_data', data=data1)
        assert bad_add1.status_code == 500

    def test_add_empty_json_object(self):
        requests.post('http://localhost:5000/add_key', data={'key': 'fitbit'})
        json_obj = json.dumps({})
        data = {'key': 'fitbit', 'time': '2017-05-14T08:54:12', 'data': json_obj}


        comp_var = {}
        comp_var['2017-05-14 08:54:12'] = json_obj
        requests.post('http://localhost:5000/add_data', data=data)

        view_last = requests.get('http://localhost:5000/view_most_recent_data', data={'key': 'fitbit'})
        assert ast.literal_eval(view_last.text) == comp_var

        view_all = requests.get('http://localhost:5000/view_data_since', data={'key': 'fitbit', 'time': '2017-01-01T01'})
        assert ast.literal_eval(view_all.text) == comp_var

    def test_add_multiple_data_points(self):
        requests.post('http://localhost:5000/add_key', data={'key': 'fitbit'})
        json_obj = json.dumps({'data': 'something'})
        data = {'key': 'fitbit', 'time': '2017-07-05T06:37:55', 'data': json_obj}
        add_data = requests.post('http://localhost:5000/add_data', data=data)
        all_data = {}
        all_data['2017-07-05 06:37:55'] = json_obj
        assert 'Data uploaded successfully' == add_data.text

        json_obj2 = json.dumps({'data': 'something else'})
        all_data['2017-07-05 10:37:55'] = json_obj2
        data2 = {'key': 'fitbit', 'time': '2017-07-05T10:37:55', 'data': json_obj2}
        add_data2 = requests.post('http://localhost:5000/add_data', data=data2)
        assert 'Data uploaded successfully' == add_data2.text

        view_all_data = {'key': 'fitbit', 'time': '2015-03-10T05'}
        view_all = requests.get('http://localhost:5000/view_data_since', data=view_all_data)

        assert ast.literal_eval(view_all.text) == all_data

        most_recent_data = {}
        most_recent_data['2017-07-05 10:37:55'] = json_obj2
        view_last = requests.get('http://localhost:5000/view_most_recent_data', data={'key': 'fitbit'})
        assert most_recent_data == ast.literal_eval(view_last.text)


if __name__ == '__main__':
    unittest.main()
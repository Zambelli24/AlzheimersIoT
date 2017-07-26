import string
import iso8601
from datetime import datetime, timezone

class HelperMethods():

    def check_time(timestamp):

        datetime = iso8601.parse_date(timestamp)
        time = datetime.time()
        if str(time) == '00:00:00':
            raise Exception("The time was not in the correct form for a \
                timestamp in ISO 8601 format specific down to at least \
                the minutes.")
        unaware_current_time = datetime.now(timezone.utc)
        current_time = unaware_current_time.astimezone()
        if datetime > current_time:
            raise Exception('The time specified has not ocurred yet, \
                it is in the future.')
        return datetime

    def check_incorrect_key_format(key):
        if key[0] not in string.ascii_lowercase:
            return True
        for char in key:
            if char not in string.ascii_lowercase and char not in '1234567890_':
                return True
        return False
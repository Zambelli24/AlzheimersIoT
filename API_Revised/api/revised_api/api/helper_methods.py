import string

class HelperMethods():

    def check_time(timestamp):

        return timestamp
        #if timestamp in correct form:
            #return timestamp
        #else:
            #raise Exception("The time was not in the correct form for a \
            #	timestamp in ISO 8601 format.")

    def check_incorrect_key_format(key):
        if key[0] not in string.ascii_lowercase:
            return True
        for char in key:
            if char not in string.ascii_lowercase and char not in '1234567890_':
                return True
        return False
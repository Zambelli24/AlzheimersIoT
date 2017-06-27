FORMAT: 1A
HOST: url

# Data Collection API

The Data Collection API acts as a filter sitting in front of a database that contains information for others to view. 
This API allows data to be queried.

# Group Data

This group contains all the data to be queried that is stored in the database. Data is mapped according to a key and a timestamp. The data itself is in the form of a json object.

+ Attributes
    + key (string)
        
        Stream that the data came from. Each key may only contain letters, numbers and underscores. Each key must start
        with a letter, and all letters must be lowercase. Underscores should be used instead of spaces and numbers
        may also be included.
        
    + time (string)
    
        Time that the data was recorded. Time must be specified down to the minutes, and may be specified down to the 
        seconds if desired. Time must follow the [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) 
        formatting standard. 
        
    + data
        
        Data from the stream. A json object may contain any number of variables within it. An empty json object
        is allowed.

## Add Data by Key, Time, Data [/add_data{?key}{?time}{?data}]

+ Parameters
    + key (string)
        
        Stream that the data is coming from.
        
    + time (string)
    
        Time that the data was recorded.
        
    + data
        
        The actual data that is in the database.

### Add Data [POST]

Upload new data into the database. The key, timestamp, and data are parameters.
        
+ Request Valid Add

        + Paramters
            + key: ""
            + time: ""
            + data: ""
            
        + Headers
            Accept: text/plain

+ Response 200 (text/plain)

    Upload successful

    + Body
    
            "Data successfully added to the database."
            
+ Request Bad Data

        + Paramters
            + data: ""
    
+ Response 400 (text/plain)

    Invalid data format.
    
    + Body
    
            "The data being added was not in the form of a json object."
            
+ Request Bad Time

        + Parameters:
            + time: ""
    
+ Response 400 (text/plain)
    
    Invalid time format.
    
    + Body
    
            "The time was not in the correct form for a timestamp in ISO 8601 format."
            
+ Request Invalid Key

        + Parameters
            + key: ""
        
+ Response 400 (text/plain)

    Key not found.
    
    + Body
    
            "The key requested was not found in the database as an active key."

## View Data Since by Key, Time [/view_data_since{?key}{?time}]

+ Parameters
    + key (string)
        
        Stream that the data is coming from.
        
    + time (string)
    
        The data returned will be from the time specified to the present time.

### View Data Since [GET]

View data from a specific stream using a key and timestamp as parameters.

+ Request Valid Get

        + Parameters
            + key: ""
            + time: ""
        
+ Response 200 (application/json)

    + Header
    
            Data: successfully retrieved

    + Body
    ```
        {
            "data"
        }
    ```
    
+ Request No Data Since Time

        + Parameters
            + key: ""
            + time: ""

+ Response 200 (text/plain)

    There is no data since the timestamp specified.
    
    + Body
    
            "The request was successfully processed however there is no data since the requested time."
            
+ Request Bad Time

        + Parameters:
            + time: ""
        
+ Response 400 (text/plain)
    
    Invalid time format.
    
    + Body
    
            "The time was not in the correct form for a timestamp in ISO 8601 format."
            
+ Request Invalid Key

        + Parameters
            + key: ""

+ Response 400 (text/plain)

    Key not found.
    
    + Body
    
            "The key requested was not found in the database as an active key."
        
## View Most Recent Data by Key [/view_most_recent_data{?key}]

+ Parameters
    + key (string)
        
        Stream that the data is coming from.

### View Most Recent Data [GET]

Get the most recent piece of data in the databse using the key as a parameter.

+ Request Valid Get

        + Parameters
            + key: ""
            + time: ""
        
+ Response 200 (application/json)

    + Header
    
            Data: successfully retrieved

    + Body
    ```
        {
            "data"
        }
    ```

+ Request No Data

        + Parameters
            + key: ""

+ Response 200 (text/plain)

    There is no data for the specified key.
    
    + Body
    
            "The request was successfully processed however there is no data since the requested time."
            
+ Request Bad Time

        + Parameters:
            + time: ""

+ Request Invalid Key

        + Parameters
            + key: ""

+ Response 400 (text/plain)

    Key not found.
    
    + Body
    
            "The key requested was not found in the database as an active key."

# Group Keys

This group contains the keys for the compatible data streams with the system.

+ Attributes
    + key (string)
        
        Stream that the data came from. Each key may only contain letters, numbers and underscores. Each key must start
        with a letter, and all letters must be lowercase. Underscores should be used instead of spaces and numbers
        may also be included.

## Keys List [/keys_list]

### List All Enabled Keys [GET]

Returns all of the enabled devices as a list of strings. There are no parameters.

+ Request Valid Get
    
    + Headers
            
            Accept: text/plain

+ Response 200 (text/plain)

    The list of keys was successfully found.
    
    + Body
    
            "The list of all enabled keys"
            
+ Request No Keys (text/plain)

    + Headers
            
            Accept: text/plain
        
+ Response 200 (text/plain)

    The response was processed successfully but no keys are enabled.
    
    + Body
    
            "There are no keys currently enabled."
       
## Add Key by Key [/add_key/{?key}]

+ Parameters
    + key (string)
        
        Stream that is activated.

### Enable a Key [POST]

Initiate a connection between a stream and the system using the key as a parameter.
        
+ Request Valid Enable

        + Parameters
            + key: ""

+ Response 200 (text/plain)

    Key successfully enabled

    + Body
    
            "The specified key was successfully enabled."
            
+ Request Enabled Key (text/plain)

        + Parameters
            + key: ""
        
+ Response 200 (text/plain)

    Key has already been enabled.
    
    + Body
    
            "The specified key has already been enabled."

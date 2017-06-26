FORMAT: 1A

# AlzheimersIoT API

The AlzheimersIoT API acts as a filter sitting infront of a database that contains patient information for caretakers, and family to view the health state of a person who may have Alzheimers. This API allows communication between the patient and the caretakers.

# Patient Data

This group contains all the data for a specified patient that is stored in the database.

## Patient Data Collection [/data]

### Add Patient Data [POST]

Upload new data into the database without returning anything.

+ key (string) - Activated device that the data came from
+ time (string) - Time that the data was recorded
+ json object - Data from the activated device

### View Patient Data [GET]

View data from a specific device as a json format with the timestamp.

+ key (string) - Activated device you want the data from
+ time (string) - Time you want the data from i.e. all data within the past << 2 minutes, 10 minutes, 60 minutes, etc. >>

# Keys

This group contains the keys for the compatible devices with our system.

## Keys Collection [/keys]

### List All Enabled Keys [GET]

Returns all of the enabled devices as a list of strings.

### Enable a Keys [POST]

Initiate a connection between a new device and the system.

+ key (string) - The key for the device you want to initiate


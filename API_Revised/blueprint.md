FORMAT: 1A

# AlzheimersIoT API

The AlzheimersIoT API acts as a filter sitting infront of a database that contains patient information for caretakers, and family to view the health state of a person who may have Alzheimers. This API allows communication between the patient and the caretakers.

# Group Patient Data

This group contains all the data for a specified patient that is stored in the database.

## Patient Data Collection [/patient data]

### Add Patient Data [POST]

Upload new data into the database

+ key (string) - device that the data came from
+ time (int?) - time that the data was recorded
+ json object - the data

### View Patient Data [GET]

View data from a specific device.

+ key (string) - device you want the data from
+ time (int?) - time you want the data from

# Group Keys

This group contains the keys for the compatible devices with our system.

## Key Collection [/keys]

### List All Enabled Keys [GET]

This method has no parameters.

### Enable a Key [POST]

This method allows you to activate a key for a device compatible with the system.

+ key (string) - the key for the device you want to enable

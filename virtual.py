import blynklib
# import blynklib_mp as blynklib # micropython import

BLYNK_AUTH = '<YourAuthToken>' #insert your Auth Token here
# base lib init
blynk = blynklib.Blynk(BLYNK_AUTH)

@blynk.handle_event('read V22')
def read_virtual_pin_handler(pin):

    # your code goes here
    # ...
    # Example: get sensor value, perform calculations, etc
    sensor_data = '<YourSensorData>'
    critilcal_data_value = '<YourThresholdSensorValue>'

    # send value to Virtual Pin and store it in Blynk Cloud 
    blynk.virtual_write(pin, sensor_data)

    # you can define if needed any other pin
    # example: blynk.virtual_write(24, sensor_data)

    # you can perform actions if value reaches a threshold (e.g. some critical value)
    if sensor_data >= critilcal_data_value

        blynk.set_property(pin, 'color', '#FF0000') # set red color for the widget UI element 
        blynk.notify('Warning critical value') # send push notification to Blynk App 
        blynk.email(<youremail@email.com>, 'Email Subject', 'Email Body') # send email to specified address

# main loop that starts program and handles registered events
while True:
    blynk.run()
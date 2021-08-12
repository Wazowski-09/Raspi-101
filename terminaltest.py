import blynklib
import subprocess

# last command in example - just to show error handling
# for certain HW can be added specific commands. 'gpio readall' on PI3b for example
ALLOWED_COMMANDS_LIST = ['ls', 'lsusb', 'ip a', 'ip abc','i2c detect -y 1']

# cmsensor1
#BLYNK_AUTH = 'nD-SwPo3-WpMrvAbdksIFa4YnP14l9-A'

# cmsensor2
BLYNK_AUTH = 'JFDPBMufAg2aRnHmO5ITI9H29aUbZmA1'
blynk = blynklib.Blynk(BLYNK_AUTH)


@blynk.handle_event('write V11')
def write_handler(pin, values):
    header = ''
    result = ''
    delimiter = '{}\n'.format('=' * 30)
    if values and values[0] in ALLOWED_COMMANDS_LIST:
        cmd_params = values[0].split(' ')
        try:
            result = subprocess.check_output(cmd_params).decode('utf-8')
            header = '[output]\n'
        except subprocess.CalledProcessError as exe_err:
            header = '[error]\n'
            result = 'Return Code: {}\n'.format(exe_err.returncode)
        except Exception as g_err:
            print("Command caused '{}'".format(g_err))
    elif values and values[0] == 'help':
        header = '[help -> allowed commands]\n'
        result = '{}\n'.format('\n'.join(ALLOWED_COMMANDS_LIST))

    # communicate with terminal if help or some allowed command
    if result:
        output = '{}{}{}{}'.format(header, delimiter, result, delimiter)
        print(output)
        blynk.virtual_write(pin, output)
        blynk.virtual_write(pin, '\n')


###########################################################
# infinite loop that waits for event
###########################################################
while True:
    blynk.run()

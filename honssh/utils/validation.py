import re


def checkValidIP(prop, value):
    match = re.match('^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
                     value)
    if match:
        return True
    else:
        print '[VALIDATION] - [' + prop[0] + '][' + prop[1] + '] should be a valid IP address'
        return False

def checkValidPort(prop, value):
    if checkValidNumber(prop, value):
        if 1 <= int(value) <= 65535:
            return True
        else:
            print '[VALIDATION] - [' + prop[0] + '][' + prop[1] + '] should be between 1 and 65535'
            return False


def checkValidBool(prop, value):
    if value in ['true', 'false']:
        return True
    else:
        print '[VALIDATION] - [' + prop[0] + '][' + prop[1] + '] must be either true or false (case sensitive)'
        return False


def checkValidNumber(prop, value):
    try:
        int(value)
        return True
    except ValueError:
        print '[VALIDATION] - [' + prop[0] + '][' + prop[1] + '] should be number.'
        return False


def checkValidChance(prop, value):
    if checkValidNumber(prop, value):
        if 1 <= int(value):
            return True
        else:
            print '[VALIDATION] - [' + prop[0] + '][' + prop[1] + '] should be greater than 0'
            return False

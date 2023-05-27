from flask import request
import json


def driverRequired(fn):
    def innerfn(*args, **kwargs):

        data = args[0]
        if 'driverId' in data:
            print('driver authenticated succesfully')
        else:
            return 'cant find driver'
        return fn(*args, **kwargs)

    return innerfn

import requests
from model.runlogs import RunLogs
from flask import Blueprint, jsonify, request
from backpacker.firebase import get_backpacker_document, upload_backpacker_image, update_backpacker_document, \
    backpacker_login
from app.thor_tools import process_base64_image

drivers: Blueprint = Blueprint('driver', __name__, url_prefix='/driver')


@drivers.route('/login', methods=['POST'])
def driver_login():
    data = request.json
    print(data)
    email = data.get("email", None)
    password = data.get("password", None)
    status, res = backpacker_login(email, password)

    return jsonify(res), status


@drivers.route('/logout', methods=['POST'])
def driver_logout():
    return 'driver logged out'


@drivers.route('/signup', methods=['POST'])
def driver_signup():
    return 'driver signing up'


@drivers.route('/get_route_details', methods=['POST'])
def get_route_details():
    # TODO : this function require routeId and DriverId
    # route_id = "sampleRoute"
    route_id = request.json['routeId']
    res, status = get_backpacker_document("routes", route_id)

    return jsonify(res), status
    # return "got route details"


@drivers.route('/get_run_state', methods=['POST'])
def get_run_state():
    """
    require routeID and driverId for FirstTime
    #otherwise only require runLogId
    :return: run state dictonary
    """
    res = {}
    data = request.json
    runlog_id = data['runlogId']

    res["run_state"] = get_backpacker_document("runlogs", runlog_id)
    return jsonify(res)
    # return 'run_state_document'


@drivers.route('/upload', methods=['POST'])
def upload_image():
    """
    here server will recieve an image that we need to upload somewhere in datastore and add that url to runlogs along
    with userIds
    :return:
    """

    res = {}
    data = request.json
    img = process_base64_image(data.get('img', None))

    runlogId = "7bf26faf-834b-435f-810f-956a621b3e88"

    res['hulkstore'] = upload_backpacker_image(img)
    run_state = get_backpacker_document("runlogs", runlogId)
    run_state['completeList'].append(res['hulkstore']['uploaded image url '])
    res['update-logs'] = update_backpacker_document("runlogs", runlogId, run_state)

    return jsonify(res)
    # return 'you are updating run_state'

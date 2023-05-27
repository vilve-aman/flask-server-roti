from flask import Blueprint, request
from app.thor_tools import generate_backpacker_query, get_backpacker_locations, generate_direction_query, \
                            generate_runlog_id
from backpacker.firebase import set_backpacker_document
from backpacker.mapbox import get_backpacker_optimization, get_directions

admin: Blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/add_new_user', methods=['POST'])
def add_new_user():
    data = request.json
    print(data)
    location = {
        "name": data['name'],
        "coordinates": [data['long'], data['lat']],
    }

    res = set_backpacker_document(collId=data['collId'], docId=location['name'], doc=location)
    return res
    # return 'new user added'


@admin.route('/verify_driver')
def verify_driver():
    return 'driver verified'


@admin.route('/generate_maps', methods=['POST'])
def generate_maps():
    """
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    V1 - Plan
    -->     here we will first collect all the locations in the given cluster
    -->     generate a payload for backpacker/mapbox api
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    V2 - Plan
    -->     here we will fetch all documents in collection
    -->     generate a payload for backpacker/mapbox api
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    :return:
    """
    data = request.json
    locations = get_backpacker_locations(data['collId'])
    backpacker_payload = generate_backpacker_query(locations, 3)
    optimizations = get_backpacker_optimization(backpacker_payload)

    # ---------------------------------------------------------------------------------------------------------------------
    #       Postprocessing...
    # ---------------------------------------------------------------------------------------------------------------------

    acks = []
    routes = []
    itr = 0
    # print(locations, optimizations)
    for optimization in optimizations["routes"]:
        itr += 1
        direction_payload = generate_direction_query(optimization)
        directions = get_directions(direction_payload)
        runlogId = generate_runlog_id(f'R{itr}')
        route = {"optimization": optimization, "directions": directions, "runlogId": runlogId, "routeId": f'R{itr}'}
        ack = set_backpacker_document(collId='routes', docId=f'R{itr}', doc=route)

        routes.append(route)
        acks.append(ack)

    # return backpacker_payload
    # print(backpacker_payload)
    # return acks
    # return route_plan['routes']
    return {"routes": routes, "acknowledgements": acks}
    # return 'maps generated successfully'

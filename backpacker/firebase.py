import os
import json

import requests


def print_pretty(obj):
    pretty = json.dumps(obj, indent=4)
    print(pretty)


base_url = os.getenv("BACKPACKER_BASE_URL")


def get_backpacker_document(collId, docId) -> dict:
    url = f"{base_url}/starkbase/getdoc"
    payload = json.dumps({
        "collId": collId,
        "docId": docId
    })
    headers = {
        'Content-Type': 'application/json'
    }

    data = requests.post(url, data=payload, headers=headers)
    doc = data.json()
    print(doc)

    if data.status_code != 200:
        return doc, 404

    return doc['Document data'], 200


def set_backpacker_document(collId, docId, doc):
    url = f"{base_url}/starkbase/setdoc"
    payload = json.dumps({
        "collId": collId,
        "docId": docId,
        "obj": doc
    })
    headers = {
        'Content-Type': 'application/json'
    }

    data = requests.post(url, data=payload, headers=headers)
    doc = data.json()
    print(doc)

    if data.status_code != 200:
        return doc, 404

    return doc, 200


def update_backpacker_document(collId, docId, doc):
    url = f"{base_url}/starkbase/updatedoc"

    payload = json.dumps({
        "collId": collId,
        "docId": docId,
        "obj": doc
    })
    headers = {
        'Content-Type': 'application/json'
    }

    data = requests.post(url, data=payload, headers=headers)
    doc = data.json()

    print(doc)
    return doc


def upload_backpacker_image(image, token='validation-token'):
    url = f"{base_url}/hulkstore/upload"
    payload = {
        "token": token
    }
    data = requests.post(url, files={'my_image': image}, data=payload)
    doc = data.json()

    print(doc)
    return doc


def backpacker_login(email, password):
    url = f"{base_url}/auth/login"

    print(email, password)
    payload = json.dumps({
        "email": email,
        "password": password
    })
    headers = {
        'Content-Type': 'application/json'
    }

    data = requests.post(url, data=payload, headers=headers)
    doc = data.json()
    print(doc)

    if data.status_code != 200:
        return 500, doc

    return 200, doc

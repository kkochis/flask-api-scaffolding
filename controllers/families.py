# -*- coding: utf-8 -*-
from flask import jsonify
from application import app
from services import families


@app.route('/families', methods=['GET'])
def list_families():
    jsonapi = {
        'data': families.get_all()
    }
    return jsonify(jsonapi)

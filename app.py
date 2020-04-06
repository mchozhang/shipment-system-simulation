#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
flask app entrance, index page is the front-end to test the apis
"""

import os
from flask import Flask, render_template, jsonify, request
from flask_mongoengine import MongoEngine
from configparser import ConfigParser
from model.record import Record

# load db info from config file
basedir = os.path.dirname(os.path.abspath(__file__))
config = ConfigParser()
config.read(os.path.join(basedir, 'config.ini'))
db_url = config.get('db', "url")
db_name = config.get('db', 'name')

# app init
app = Flask(__name__, instance_relative_config=True)
app.config["MONGODB_SETTINGS"] = {
    'db': db_name,
    'host': db_url,
}

# db init
db = MongoEngine()
db.init_app(app)


@app.route('/', methods=['GET'])
def index():
    """
    render the index page
    :return: index page
    """
    records = []
    try:
        records = Record.objects()
        records = [record.to_json() for record in records]
    except Exception as e:
        print(e)

    return render_template("index.html", records=records)


@app.route('/record', methods=['GET'])
def search():
    """
    search the records by user id or product name
    :return:  a list containing all suitable records
    """
    result = {
        "status": "success",
    }
    try:
        # parse arguments from url
        user = request.args.get('user', "").strip()
        product = request.args.get('product', "").strip()

        # add filter to query
        if not user and not product:
            records = Record.objects()
        elif not user:
            records = Record.objects(product=product)
        elif not product:
            records = Record.objects(user=user)
        else:
            records = Record.objects(user=user, product=product)

        result["records"] = [record.to_json() for record in records]
    except Exception as e:
        result["status"] = "failed"
        result["err_msg"] = str(e)

    return jsonify(result)


@app.route('/record', methods=["POST"])
def insert_record():
    """
    user inserts a record
    :return: result of the post request
    """
    result = {
        "status": "success",
    }

    try:
        # parse form data
        json = request.json
        user = json["user"]
        product = json["product"]
        age = json.get("age", 0)
        latitude = json.get("latitude", 0.0)
        longitude = json.get("longitude", 0.0)
        hierarchy = json.get("hierarchy", "")
        hierarchy = [level.strip() for level in hierarchy.split(",")]

        # insert document
        record = Record(user=user, product=product, age=age, latitude=latitude, longitude=longitude,
                        hierarchy=hierarchy)
        record.save()

        result["record"] = record.to_json()
    except Exception as e:
        result["status"] = "failed"
        result["err_msg"] = str(e)

    return jsonify(result)


@app.route('/record', methods=["DELETE"])
def delete_record():
    """
    user removes a record
    :return: result of the delete request
    """
    result = {
        "status": "failed",
    }

    try:
        # parse arguments
        id = request.json["id"]

        # remove a document
        Record.objects.get(id=id).delete()
        result["status"] = "success"
    except Exception as e:
        result["status"] = "failed"
        result["err_msg"] = str(e)

    return jsonify(result)


@app.route('/delete-records', methods=["DELETE"])
def delete_multiple_records():
    """
    delete multiple records
    :return:
    """
    result = {
        "status": "success",
    }

    try:
        records = request.json["records"]

        # remove all selected records
        for id in records:
            Record.objects.get(id=id).delete()
    except Exception as e:
        result["status"] = "failed"
        result["err_msg"] = str(e)

    return jsonify(result)


if __name__ == '__main__':
    app.run()

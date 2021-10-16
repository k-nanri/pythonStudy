# -*- coding: utf-8 -*-
from flask import Flask, request, abort, json, jsonify
import peewee

db = peewee.SqliteDatabase("src/taskmanager/data.db")
api = Flask(__name__)

class Task(peewee.Model):
    id = peewee.IntegerField()
    title = peewee.TextField()
    created_at = peewee.TimeField()
    updated_at = peewee.TimeField()

    class Meta:
        database = db

@api.route("/task", methods=["POST"])
def create_task():
    task = request.get_json()
    print(task)


if __name__ == "__main__":
    api.run(host="0.0.0.0", port=3000)
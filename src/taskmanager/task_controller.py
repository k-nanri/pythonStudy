# -*- coding: utf-8 -*-
from flask import Flask, request, abort
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

@api.route("/task/<string:taskId>", methods=["GET"])
def get_task(taskId):
    try:
        task = Task.get(Task.id == taskId)
    except Task.DoesNotExist:
        abort(404)

    response = {
        "data": {
            
        }
    }

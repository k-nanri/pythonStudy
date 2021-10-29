# -*- coding: utf-8 -*-
from flask import Flask, request
from task_service import create_task2

app = Flask(__name__)


@app.route("/task", methods=["POST"])
def create_task():
    task = request.get_json()
    create_task2(task)
    return "OK", 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
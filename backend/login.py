import os

import bcrypt
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.getenv("MONGODB"))
db = client.cbdbms
parent_db = db.parent
child_db = db.child


def parent_login(username, password):
    try:
        parent = parent_db.find_one({"username": username})
        if bcrypt.checkpw(password.encode("utf-8"), parent["password"]):
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def child_login(username, password):
    try:
        child = child_db.find_one({"username": username})
        if bcrypt.checkpw(password.encode("utf-8"), child["password"]):
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

import os
from datetime import datetime
from random import randint

import bcrypt
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.getenv("MONGODB"))
db = client.cbdbms
parent_db = db.parent
child_db = db.child
transaction_db = db.transaction
transaction_request_db = db.transaction_request


def parent_transaction(username, password, amount):
    try:
        parent = parent_db.find_one({"username": username})
        if bcrypt.checkpw(password.encode("utf-8"), parent["password"]):
            transaction_db.create_index("transaction_id", unique=True)
            transaction_details = {
                "username": username,
                "transaction_id": randint(1, 1000000000000),
                "transactionAt": datetime.now(),
                "amount": amount,
                "type": "parent"
            }
            transaction_db.insert_one(transaction_details)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def child_transaction_request(username, password, amount, parentAccNo):
    try:
        child_details = child_db.find_one({"username": username})
        if bcrypt.checkpw(password.encode("utf-8"), child_details["password"]):
            parent_details = parent_db.find_one({"account_no": parentAccNo})
            child_transaction_update = {
                "$set": {"transaction_requests": parent_details["transaction_requests"].append({username: amount})}
            }
            parent_db.update_one({"account_no": parentAccNo}, child_transaction_update)

            child_transaction_update = {
                "$set": {"transaction_requests": child_details["transaction_requests"].append({username: amount})}
            }
            child_db.update_one({"account_no": parentAccNo}, child_transaction_update)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def child_transaction(username, amount, fromAcc, toAcc):
    try:
        child_details = child_db.find_one({"username": username, "account_number": fromAcc})
        balance_update = {"$set": {"balance": child_details["balance"] - amount}}
        child_db.update_one({"username": username, "account_number": fromAcc}, balance_update)

        transaction_db.create_index("transaction_id", unique=True)
        transaction_details = {
            "username": username,
            "transaction_id": randint(1, 1000000000000),
            "transactionAt": datetime.now(),
            "amount": amount,
            "from": fromAcc,
            "to": toAcc,
            "type": "child"
        }
        transaction_db.insert_one(transaction_details)

        child_details = child_db.find_one({"account_number": toAcc})
        balance_update = {"$set": {"balance": child_details["balance"] + amount}}
        child_db.update_one({"username": username, "account_number": fromAcc}, balance_update)
        return True
    except Exception as e:
        print(e)
        return False

import os
from datetime import datetime, date
from random import randint

import bcrypt
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

# connect to DB
client = MongoClient(os.getenv("MONGODB"))

# DB references
db = client.cbdbms
parent_db = db.parent
child_db = db.child
transaction_db = db.transaction
transaction_request_db = db.transaction_request

child_daily_limit = 100


# Parent to some Account transaction
def parent_transaction(username, password, amount, to_account_number, to_account_type):
    try:
        # Get Parent Details
        parent_details = parent_db.find_one({"username": username})

        # Check password and check account type of recipient
        if bcrypt.checkpw(password.encode("utf-8"), parent_details["password"]) and (
                to_account_type == "child" or to_account_type == "parent"):
            # update from account balance
            parent_details_update = {"$set", {"amount": parent_details["amount"] - amount}}
            parent_db.update_one({"username": username}, parent_details_update)

            # Update as Transaction
            transaction_db.create_index("transaction_id", unique=True)
            transaction_details = {
                "username": username,
                "from_account_number": parent_details["account_number"],
                "to_account_number": to_account_number,
                "transaction_id": randint(1, 1000000000000),
                "transactionAt": datetime.now(),
                "transaction_date": date.today(),
                "amount": amount,
                "to_type": to_account_type,
                "by_type": "parent",
                "transaction_type": "1to1"
            }
            transaction_db.insert_one(transaction_details)

            if to_account_type == "parent":
                # Get TO account Details
                to_parent_details = parent_db.find_one({"account_number": to_account_number})

                # Update TO account Balance
                to_parent_details_update = {"$set", {"amount": to_parent_details["amount"] + amount}}
                parent_db.update_one({"account_number": to_account_number}, to_parent_details_update)

            elif to_account_type == "child":
                # Get TO account Details
                to_child_details = child_db.find_one({"account_number": to_account_number})

                # Update TO account Balance
                to_child_details_update = {"$set", {"amount": to_child_details["amount"] + amount}}
                child_db.update_one({"account_number": to_account_number}, to_child_details_update)
            return True, "transaction success"
        else:
            return False, "password incorrect"
    except Exception as e:
        print(e)
        return False, e


# Deposit to parent account
def parent_deposit(account_number, amount):
    try:
        # Get Parent Details
        parent_details = parent_db.find_one({"account_number": account_number})

        # Update Parent Balance
        parent_details_update = {"$set", {"amount": parent_details["amount"] + amount}}
        parent_db.update_one({"account_number": account_number}, parent_details_update)

        # Update as Transaction
        transaction_db.create_index("transaction_id", unique=True)
        transaction_details = {
            "username": parent_details["username"],
            "transaction_id": randint(1, 1000000000000),
            "transactionAt": datetime.now(),
            "transaction_date": date.today(),
            "amount": amount,
            "by_type": "parent",
            "transaction_type": "deposit"
        }
        transaction_db.insert_one(transaction_details)
        return True, "transaction success"
    except Exception as e:
        print(e)
        return False, e


# Deposit to parent account
def child_deposit(account_number, amount):
    try:
        # Get Parent Details
        child_details = child_db.find_one({"account_number": account_number})

        # Update Parent Balance
        child_details_update = {"$set", {"amount": child_details["amount"] + amount}}
        child_db.update_one({"account_number": account_number}, child_details_update)

        # Update as Transaction
        transaction_db.create_index("transaction_id", unique=True)
        transaction_details = {
            "username": child_details["username"],
            "transaction_id": randint(1, 1000000000000),
            "transactionAt": datetime.now(),
            "transaction_date": date.today(),
            "amount": amount,
            "by_type": "child",
            "transaction_type": "deposit"
        }
        transaction_db.insert_one(transaction_details)
        return True, "transaction success"
    except Exception as e:
        print(e)
        return False, e


# Child transaction request
def child_transaction_request(username, password, amount, toAcc, parentAccNo):
    try:
        # Get child details
        child_details = child_db.find_one({"username": username})

        # check if password is correct
        if bcrypt.checkpw(password.encode("utf-8"), child_details["password"]):
            # check child's today's transactions
            child_today_transaction = transaction_db.find(
                {"from_account_number": child_details["account_number"], "transaction_date": date.today()}
            )
            amount_spent_today = 0
            for i in child_today_transaction:
                amount_spent_today += i["amount"]

                # if less than limit do transaction
                child_transaction_success = child_transaction(username, amount,
                                                              child_details["account_number"], toAcc, "auto")
                return child_transaction_success, "transaction success"
            else:
                # else make a transaction request
                transaction_request_db.create_index("transaction_request_id", unique=True)
                transaction_request = {
                    "child_username": username,
                    "child_account_number": child_details["account_number"],
                    "amount": amount,
                    "parentAccNo": parentAccNo,
                    "transaction_request_id": randint(1, 1000000000000),
                    "toAcc": toAcc
                }
                transaction_request_db.insert_one(transaction_request)
                return True, "transaction requested"
        else:
            return False, "password incorrect"
    except Exception as e:
        print(e)
        return False, "error"


# Child transaction
def child_transaction(username, amount, fromAcc, toAcc, approved_by):
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
            "from_account_number": fromAcc,
            "to_account_number": toAcc,
            "by_type": "child",
            "to_type": "child",
            "transaction_type": "1to1",
            "approved_by": approved_by
        }
        transaction_db.insert_one(transaction_details)

        child_details = child_db.find_one({"account_number": toAcc})
        balance_update = {"$set": {"balance": child_details["balance"] + amount}}
        child_db.update_one({"username": username, "account_number": fromAcc}, balance_update)
        return True, "transaction success"
    except Exception as e:
        print(e)
        return False, e


def transactions_by_child(username, account_number):
    try:
        child_details = child_db.find_one({"username": username, "account_number": account_number})
        child_sent = transaction_db.find(
            {"from_account_number": child_details["account_number"]}
        )

        child_received = transaction_db.find(
            {"to_account_number": child_details["account_number"]}
        )

        return True, child_sent, child_received

    except Exception as e:
        print(e)
        return False, e


def transactions_by_parent(username, account_number):
    try:
        parent_details = parent_db.find_one({"username": username, "account_number": account_number})
        parent_sent = transaction_db.find(
            {"from_account_number": parent_details["account_number"]}
        )

        parent_received = transaction_db.find(
            {"to_account_number": parent_details["account_number"]}
        )

        return True, parent_sent, parent_received

    except Exception as e:
        print(e)
        return False, e

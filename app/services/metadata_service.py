from app.config.database import call_data_collection


def get_metadata():
    cities = sorted(call_data_collection.distinct("city"))

    caller_numbers = sorted(
        call_data_collection.distinct("callerNumber")
    )

    receiver_numbers = sorted(
        call_data_collection.distinct("receiverNumber")
    )

    oldest_record = call_data_collection.find_one(
        {},
        {"callStartTime": 1, "_id": 0},
        sort=[("callStartTime", 1)]
    )

    newest_record = call_data_collection.find_one(
        {},
        {"callStartTime": 1, "_id": 0},
        sort=[("callStartTime", -1)]
    )

    return {
        "cities": cities,
        "callerNumbers": caller_numbers,
        "receiverNumbers": receiver_numbers,
        "minDate": oldest_record["callStartTime"],
        "maxDate": newest_record["callStartTime"],
    }

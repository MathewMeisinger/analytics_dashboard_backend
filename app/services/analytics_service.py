from app.config.database import call_data_collection
from app.services.filter_service import build_filter


def get_summary(
    city=None,
    caller_number=None,
    receiver_number=None,
    start_date=None,
    end_date=None,
):
    query = build_filter(
        city,
        caller_number,
        receiver_number,
        start_date,
        end_date,
    )

    pipeline = [
        {
            "$match": query
        },
        {
            "$group": {
                "_id": None,
                "totalCalls": {"$sum": 1},
                "successfulCalls": {"$sum": {"$cond": ["$callStatus", 1, 0]}},
                "totalCost": {"$sum": "$callCost"},
                "averageCost": {"$avg": "$callCost"},
                "averageDuration": {"$avg": "$callDuration"},
                "maxDuration": {"$max": "$callDuration"},
                "minDuration": {"$min": "$callDuration"},
                "totalDuration": {"$sum": "$callDuration"},
                "maxCost": {"$max": "$callCost"},
                "cities": {"$addToSet": "$city"}
            }
        }
    ]

    result = list(call_data_collection.aggregate(pipeline))

    if not result:
        return {
            "totalCalls": 0,
            "successfulCalls": 0,
            "totalCost": 0,
            "averageCost": 0,
            "averageDuration": 0,
            "maxDuration": 0,
            "minDuration": 0,
            "totalDuration": 0,
            "successRate": 0,
            "activeCities": 0,
            "maxCost": 0,
        }

    summary = result[0]

    return {
        "totalCalls": summary["totalCalls"],
        "successfulCalls": summary["successfulCalls"],
        "totalCost": round(summary["totalCost"], 2),
        "averageCost": round(summary["averageCost"], 2),
        "averageDuration": round(summary["averageDuration"], 2),
        "maxDuration": summary["maxDuration"],
        "minDuration": summary["minDuration"],
        "totalDuration": summary["totalDuration"],
        "successRate": round(
            (summary["successfulCalls"] / summary["totalCalls"]) * 100, 1,
        ),
        "activeCities": len(summary["cities"]),
        "maxCost": round(summary["maxCost"], 2),
    }


def get_call_type_distribution(
    city=None,
    caller_number=None,
    receiver_number=None,
    start_date=None,
    end_date=None,
):
    query = build_filter(
        city,
        caller_number,
        receiver_number,
        start_date,
        end_date,
    )

    pipeline = [
        {
            "$match": query
        },
        {
            "$group": {
                "_id": "$callDirection",
                "count": {"$sum": 1}
            }
        }
    ]

    results = list(
        call_data_collection.aggregate(pipeline)
    )

    distribution = []

    for result in results:
        distribution.append({
            "callType": (
                "Outgoing" if result["_id"] else "Incoming"
            ),
            "count": result["count"]
        })

    return distribution


def get_top_callers(
    city=None,
    caller_number=None,
    receiver_number=None,
    start_date=None,
    end_date=None,
    limit: int = 10,
):
    query = build_filter(
        city,
        caller_number,
        receiver_number,
        start_date,
        end_date,
    )

    pipeline = [
        {
            "$match": query
        },
        {
            "$group": {
                "_id": "$callerNumber",
                "totalCalls": {"$sum": 1}
            }
        },
        {
            "$sort": {"totalCalls": -1}
        },
        {
            "$limit": limit
        }
    ]

    results = list(
        call_data_collection.aggregate(pipeline)
    )

    top_callers = []

    for result in results:
        top_callers.append({
            "callerNumber": result["_id"],
            "totalCalls": result["totalCalls"]
        })

    return top_callers


def get_calls_by_city(
    city=None,
    caller_number=None,
    receiver_number=None,
    start_date=None,
    end_date=None,
):
    query = build_filter(
        city,
        caller_number,
        receiver_number,
        start_date,
        end_date,
    )

    pipeline = [
        {
            "$match": query
        },
        {
            "$group": {
                "_id": "$city",
                "totalCalls": {"$sum": 1}
            }
        },

        {
            "$sort": {"totalCalls": -1}
        }
    ]

    results = list(call_data_collection.aggregate(pipeline))

    return [
        {"city": result["_id"], "totalCalls": result["totalCalls"]}
        for result in results
    ]


def get_calls_by_hour(
    city=None,
    caller_number=None,
    receiver_number=None,
    start_date=None,
    end_date=None,
):
    query = build_filter(
        city,
        caller_number,
        receiver_number,
        start_date,
        end_date,
    )

    pipeline = [
        {
            "$match": query
        },
        {
            "$group": {
                "_id": {"$hour": "$callStartTime"},
                "totalCalls": {"$sum": 1}
                }
        },
        {
            "$sort": {"_id": 1}
        }
    ]

    results = list(call_data_collection.aggregate(pipeline))

    return [
        {"hour": result["_id"], "totalCalls": result["totalCalls"]}
        for result in results
        ]


def get_calls_by_day(
    city=None,
    caller_number=None,
    receiver_number=None,
    start_date=None,
    end_date=None,
):
    query = build_filter(
        city,
        caller_number,
        receiver_number,
        start_date,
        end_date,
    )

    pipeline = [
        {
            "$match": query
        },
        {
            "$group": {
                "_id": {"$dateToString": {
                        "format": "%Y-%m-%d",
                        "date": "$callStartTime"}},
                "totalCalls": {"$sum": 1}
            }
        },
        {
            "$sort": {"_id": 1}
        }
    ]

    results = list(call_data_collection.aggregate(pipeline))

    return [
        {"day": result["_id"], "totalCalls": result["totalCalls"]}
        for result in results
    ]


def get_cost_by_city(
    city=None,
    caller_number=None,
    receiver_number=None,
    start_date=None,
    end_date=None,
):
    query = build_filter(
        city,
        caller_number,
        receiver_number,
        start_date,
        end_date,
    )

    pipeline = [
        {
            "$match": query
        },
        {
            "$group": {
                "_id": "$city",
                "averageCost": {
                    "$avg": "$callCost"
                },
                "totalCost": {
                    "$sum": "$callCost"
                }
            }
        },
        {
            "$sort": {
                "averageCost": -1
            }
        }
    ]

    results = list(call_data_collection.aggregate(pipeline))

    return [
        {
            "city": result["_id"],
            "averageCost": round(result["averageCost"], 2),
            "totalCost": round(result["totalCost"], 2),
        }
        for result in results
    ]


def get_call_records(
    city=None,
    caller_number=None,
    receiver_number=None,
    start_date=None,
    end_date=None,
):
    query = build_filter(
        city,
        caller_number,
        receiver_number,
        start_date,
        end_date,
    )

    records = list(
        call_data_collection.find(
            query,
            {
                "_id": 0,
                "callerName": 1,
                "callerNumber": 1,
                "receiverNumber": 1,
                "city": 1,
                "callDuration": 1,
                "callCost": 1,
                "callStartTime": 1,
            },
        )
    )

    return records

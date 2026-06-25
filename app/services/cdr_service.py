import math
from app.config.database import call_data_collection


def get_paginated_cdrs(
    page: int,
    limit: int,
    city: str | None = None,
    caller_number: str | None = None,
    receiver_number: str | None = None,
    start_date=None,
    end_date=None,
    sort: str = "callStartTime",
    order: str = "desc"
):

    # Building the MongoDB query
    query = {}

    if city:
        query["city"] = city

    if caller_number:
        query["callerNumber"] = caller_number

    if receiver_number:
        query["receiverNumber"] = receiver_number

    if start_date or end_date:
        query["callStartTime"] = {}

        if start_date:
            query["callStartTime"]["$gte"] = start_date

        if end_date:
            query["callStartTime"]["$lte"] = end_date

    # Pagination
    skip = (page - 1) * limit

    # sorting
    sort_order = -1 if order.lower() == "desc" else 1

    # count filtered records
    total_records = call_data_collection.count_documents(query)
    total_pages = max(1, math.ceil(total_records / limit))

    # retrive the records
    records = list(
        call_data_collection
        .find(query, {"_id": 0})
        .sort(sort, sort_order)
        .skip(skip)
        .limit(limit)
    )

    return {
        "page": page,
        "limit": limit,
        "total_records": total_records,
        "total_pages": total_pages,
        "records": records,
    }

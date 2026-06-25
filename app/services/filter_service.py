from datetime import datetime


def build_filter(
    city=None,
    caller_number=None,
    receiver_number=None,
    start_date=None,
    end_date=None,
):

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
            query["callStartTime"]["$gte"] = datetime.combine(
                start_date,
                datetime.min.time(),
            )

        if end_date:
            query["callStartTime"]["$lte"] = datetime.combine(
                end_date,
                datetime.max.time(),
            )

    return query
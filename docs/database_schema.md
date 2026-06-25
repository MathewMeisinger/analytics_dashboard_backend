# Call Data Schema

| Field | Type | Description |
|---------|---------|---------------------------|
| id | integer | Unique call identifier |
| callerName | string | Caller's name |
| callerNumber | string | Originating number |
| receiverNumber | string | Receiving number |
| city | string | Call location |
| callDirection | boolean | True=Outgoing False=Incoming |
| callStatus | boolean | True=Successful False=Failed |
| callDuration | integer | Duration in seconds |
| callCost | float | Cost of call |
| callStartTime | datetime | Call start timestamp |
| callEndTime | datetime | Call end timestamp |
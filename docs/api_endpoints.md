# API Endpoints

## CDR

### GET /cdr

Returns paginated call records.

### Query Parameters

| Parameter | Type | Description |
|----------------|------------|-----------------------------|
| page | integer | Page number |
| limit | integer | Records per page |
| city | string | Filter by city |
| callerNumber | string | Filter by caller number |
| receiverNumber | string | Filter by receiver number |
| startDate | datetime | Start date |
| endDate | datetime | End date |
| sort | string | Sort field |
| order | asc/desc | Sort direction |

---

## Analytics

### GET /analytics/summary

Returns:

- Total Calls
- Total Duration
- Total Cost
- Average Cost

---

### GET /analytics/call-type-distribution

Returns:

- Incoming Calls
- Outgoing Calls

---

### GET /analytics/top-callers

Returns:

Top callers ordered by call volume.

---

## Metadata

### GET /metadata

Returns:

- Cities
- Caller Numbers
- Receiver Numbers

---

## Authentication (Phase 2)

### POST /auth/login

User login.

### POST /auth/signup

User registration (optional).

### GET /auth/me

Current authenticated user.
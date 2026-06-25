from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.routers.cdr import router as cdr_router
from app.routers.metadata import router as metadata_router
from app.exceptions import ResourceNotFoundException, DatabaseException
from app.routers.analytics import router as analytics_router
from app.routers import auth

app = FastAPI(
    title='PineVox Analytics API',
    description='Backend API for PineVox CDR Dashboard',
    version='1.0.0'
)

app.include_router(cdr_router)
app.include_router(metadata_router)
app.include_router(analytics_router)
app.include_router(auth.router)


@app.exception_handler(DatabaseException)
async def database_exception_handler(request: Request, exc: DatabaseException,):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": exc.message,
        },
    )

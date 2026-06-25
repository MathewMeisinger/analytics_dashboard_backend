import os

from dotenv import load_dotenv

load_dotenv()


# -----------------------------
# MongoDB
# -----------------------------
MONGO_URI = os.getenv("MONGO_URI")

DATABASE_NAME = os.getenv("DATABASE_NAME")

COLLECTION_NAME = os.getenv("COLLECTION_NAME")


# -----------------------------
# JWT
# -----------------------------
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

JWT_EXPIRE_MINUTES = int(
    os.getenv("JWT_EXPIRE_MINUTES", "30")
)

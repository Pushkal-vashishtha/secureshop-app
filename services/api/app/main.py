import logging
import os

import psycopg
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

logger = logging.getLogger("secureshop.api")
app = FastAPI(title="SecureShop API", version="0.1.0")


def conninfo() -> str:
    return psycopg.conninfo.make_conninfo(
        host=os.environ.get("DB_HOST", "localhost"),
        dbname=os.environ.get("DB_NAME", "secureshop"),
        user=os.environ.get("DB_USER", "app_user"),
        password=os.environ.get("DB_PASSWORD", ""),
        sslmode="require",
        connect_timeout=3,
    )


class ProductIn(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price_inr: float = Field(gt=0, lt=1_000_000)


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/products")
def list_products():
    try:
        with psycopg.connect(conninfo()) as conn:
            rows = conn.execute(
                "SELECT id, name, price_inr FROM shop.products ORDER BY id"
            ).fetchall()
    except psycopg.OperationalError as exc:
        logger.warning("database unavailable: %s", exc)
        raise HTTPException(status_code=503, detail="database unavailable")
    return [{"id": r[0], "name": r[1], "price_inr": float(r[2])} for r in rows]


@app.post("/products", status_code=201)
def add_product(product: ProductIn):
    try:
        with psycopg.connect(conninfo()) as conn:
            row = conn.execute(
                "INSERT INTO shop.products (name, price_inr) VALUES (%s, %s) RETURNING id",
                (product.name, product.price_inr),
            ).fetchone()
    except psycopg.OperationalError as exc:
        logger.warning("database unavailable: %s", exc)
        raise HTTPException(status_code=503, detail="database unavailable")
    return {"id": row[0], **product.model_dump()}

import os
import datetime
import json

from fastapi import FastAPI, Header, Request
from fastapi.responses import HTMLResponse

from redis import Redis

import uvicorn

app = FastAPI()

redis = Redis(
    host=os.getenv("REDIS_HOST", "redis"), port=int(os.getenv("REDIS_PORT", 6379))
)

redis.set("counter", 0)


@app.middleware("http")
async def log_visits(req: Request, call_next):
    res = await call_next(req)
    redis.lpush(
        "counter visits",
        json.dumps(
            {
                "User-Agent": req.headers.get("User-Agent"),
                "Date": str(datetime.datetime.utcnow()),
                "Path": req.url.path,
            }
        ),
    )
    return res


@app.get("/")
def get_counter():
    counter = int(redis.get("counter"))
    return counter


@app.get("/visits")
def get_visits():
    return [json.loads(i) for i in redis.lrange("counter visits", 0, -1)]


@app.get("/stat")
def get_counter():
    return redis.incr("counter")


@app.get("/about")
def hello():
    return HTMLResponse("<h3>Hello, ainur</h3>")


if __name__ == "__main__":
    uvicorn.run(app, port=int(os.getenv("PORT", 5000)))

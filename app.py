import time
import redis
import uvicorn
import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# cache = redis.Redis(host='redis', port=6379)
cache = redis.Redis(host=os.environ.get('REDISIP', 'redis'), port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # count = 0
    count = get_hit_count()
    print(count)
    return templates.TemplateResponse(
        request=request, name="home.html", context={"count": count}
    )

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=int(os.environ.get('PORT', 8000)), log_level="info")
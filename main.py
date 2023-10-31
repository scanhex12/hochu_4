from fastapi import FastAPI
import random
app = FastAPI()
url_db = {}
def generate_random_id():
    return ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", k=6))
@app.post("/create", response_model=dict)
def create_short_url(item: URLItem):
    short_id = generate_random_id()
    url_db[short_id] = item.url
    return {"id": short_id}
@app.get("/link/{id}", response_model=URLItem)
def get_original_url(id: str):
    original_url = url_db.get(id)
    if original_url is None:
        return {"url": "Not Found"}
    return {"url": original_url}

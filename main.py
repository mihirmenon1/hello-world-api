from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    """
    Create a root route that responds with a static message.
    """
    return {"message": "Hello, World!"}

@app.get("/hello/{name}")
def hello(name: str):
    """
    Create a route that responds with custom output taken from input.
    """
    return {"message": f"Hello, {name}!"}
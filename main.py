from fastapi import FastAPI
from routers import users, auth, content # Import the new content router

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(content.router) # Add the content router

@app.get("/")
def read_root():
    return {"message": "Welcome to the AiTuki Backend"}
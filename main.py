from fastapi import FastAPI
from routers import users, auth # Import the new auth router

app = FastAPI()

# Include both routers in your application
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AiTuki Backend"}
from fastapi import FastAPI
from routers import users # Import the users router

app = FastAPI()

# Include the user registration router in your main app.
# All endpoints from users.py will now be available under the main app.
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AiTuki Backend"}
    
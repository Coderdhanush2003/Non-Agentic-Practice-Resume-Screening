from fastapi import FastAPI
from routes.screening import router

app = FastAPI()
app.include_router(router)




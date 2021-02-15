from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(title='Project Signal Data Resources API', description='A collection of APIs for Project Signal')

@app.get('/')
def get_health():
    return { 'message': 'OK'}

lambda_handler = Mangum(app=app)


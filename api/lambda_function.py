from fastapi import FastAPI
from mangum import Mangum
from v1.routers import router

app = FastAPI(title='Project Signal Data Resources API',
              description='A collection of APIs for Project Signal',
              openapi_prefix='/dev')

app.include_router(router)


@app.get('/')
def get_health():
    return {'message': 'OK'}


lambda_handler = Mangum(app=app)

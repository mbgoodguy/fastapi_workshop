from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def root():
    a = {'message': 'Hello!'}
    return a

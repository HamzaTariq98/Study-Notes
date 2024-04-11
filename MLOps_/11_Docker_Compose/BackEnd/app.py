from fastapi import FastAPI
import uvicorn


app = FastAPI()

PORT = 5001

data = []


def fetch_data():
    with open('database.txt','r') as f:
        data = [int(line[:-1]) for line in f.readlines()]
    return data


@app.get('/')
def main():
    return {'Welcome':'Welcome to yr back end'}


@app.get('/add_num')
def add_num(num):
    with open('database.txt','a') as f:
        f.write(f'{num}\n')
    return {'data':fetch_data()}




@app.get('/fetch_data')
def fetch_numbers():
    return fetch_data()


if __name__ == '__main__':
    uvicorn.run(app,host = '0.0.0.0',port = PORT)
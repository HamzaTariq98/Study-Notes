from flask import Flask, render_template, url_for, request
import requests


port = 5000
app = Flask(__name__)



def add_number_to_db(number):
    requests.get(f'http://backend:5001/add_num?num={number}')
    print(f'\nadding {number} to db\n')




def call_database():
    response = requests.get('http://backend:5001/fetch_data')
    return response.json()



@app.route('/')
def main():
    data = call_database()
    return render_template('index.html',data=data)



@app.route('/add_value')
def add_value():
    number = None
    for num in range(10):
        num_ = request.args.get(f'_{num}')
        if num_:
            number = num_

    add_number_to_db(number)
    data = call_database()

    return render_template('index.html',data=data)



if __name__ == '__main__':
    app.run(debug=True,port=port)

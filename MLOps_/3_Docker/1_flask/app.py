from flask import Flask, request
import sklearn
import joblib
import os


model = joblib.load('model.pkl')
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Welcome to prediction model :D</p>"


@app.route("/predict")
def hello_world2():
    num = request.args.get('num')
    return {'pre':'hamza',
             'age':26,
             'predictions': model.predict([[int(num)]])}


if __name__ == "__main__":

    # model = LinearRegression()
    # X = np.array([[-1], [0], [1], [2]])
    # y = np.array([0, 1, 2, 3])
    # model.fit(X, y)
    # joblib.dump(model,'model.pkl')
    print(f"my model prediction of 2 is: {model.predict([[2]])}")
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True,host='0.0.0.0', port=port)

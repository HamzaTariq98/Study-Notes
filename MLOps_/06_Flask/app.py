from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/index')
def main_page(methods=['GET']):
    num = request.args.get('num')
    if num is None or num == "":
        result = ""
    else:
        num = int(num)**2
        result = f'Prediction value is :{num}' 
    return render_template('index.html',result=result)



if __name__ == '__main__':
    app.run(debug=True)
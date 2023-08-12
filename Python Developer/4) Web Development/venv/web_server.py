# 2 main frameworks for setting up a web server (flask and django)
# python anywhere to set up a free web link
from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)

# Define the folder where uploaded images will be stored
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/upload_files.html", methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        # Check if the post request has a file part
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']

        # If the user does not select a file, the browser might
        # submit an empty part without a filename
        if file.filename == '':
            return redirect(request.url)
        
        if file:
            # Securely save the uploaded file to the specified folder
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Here, you can process the uploaded image with your ImageAI model
            # and generate the corresponding result
            
            return redirect(url_for('hello_world'))  # Redirect back to the upload page

    return render_template('upload_files.html') 

@app.route("/")
def main_page():
    return render_template('index.html') 


@app.route("/process_email", methods=['POST'])
def process_email():
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    with open('data.txt','a') as file:
        file.write(f'\n{email},{subject},{message}')
        
    return 'message sent'


if __name__ == "__main__":
    app.run(debug=True)


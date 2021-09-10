from flask import Flask, redirect, url_for, render_template, flash
from flask.globals import request
from werkzeug.utils import secure_filename
import logging
from method import csv_to_json
import os

UPLOAD_FOLDER = '/unfinish_file'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template("Welcome_Page.html")

@app.route("/upload")
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return redirect(url_for('download_file',name = filename))
    return render_template("upload.html",methods=["GET", "POST"])

@app.route("/parse")
def parse():
    csv_to_json.parse_csv()
    return render_template("parse.html")

@app.route("/upload_result")
def result():
    return render_template("upload_result.html")

if __name__ == "__main__":
    app.run(debug=True)
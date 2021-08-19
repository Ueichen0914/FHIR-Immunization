from flask import Flask, redirect, request, render_template
import os
from werkzeug.utils import secure_filename
from method import csv_to_json

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("/Welcome_Page.html")


UPLOAD_FOLDER = "C:/Users/Tim/Desktop/FHIR immunization"
ALLOWED_EXTENSIONS = set(["csv"])


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS


@app.route("/upload-csv", methods=["GET", "POST"])
def upload_csv():
    return render_template("upload.html")
    if request.method == "POST":
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return redirect(url_for("uploaded_file", filename=filename))
            # csv = request.files["csv"]
            # print(csv)
            # return redirect(request.url)


if __name__ == "__main__":
    app.run(debug=True)

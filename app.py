from csv_upload import ALLOWED_EXTENSIONS, UPLOAD_FOLDER
from flask import Flask, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = ''
ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def patient(dic1):
    with open(
        "JSON_template\Patient_success_template.json", "r", encoding="utf-8"
    ) as patient_json:
        patient = json.load(patient_json)
    for key, value in dic1.items():
        if key == "姓名":
            patient["name"][0]["text"] = str(value)
        elif key == "身分證":
            patient["identifier"][0]["value"] = str(value)
        elif key == "性別":
            patient["gender"] = str(value)
        elif key == "生日":
            ivalue = int(value)
            if ivalue < 2000000:
                ivalue += 19110000
            svalue = str(ivalue)
            ssvalue = svalue[:4] + "-" + svalue[4:6] + "-" + svalue[6:8]
            patient["birthDate"] = ssvalue
        else:
            pass
    return patient

def parse_csv(file):
    file = "csv_example\FHIR resource.csv"
    with open(file) as f:
        text = csv.DictReader(f)
        for line in text:
            json_patient = json.dumps(
                patient(line), sort_keys=False, indent=4, ensure_ascii=False
            )
            print(json_patient)
            headers = {'Content-Type': 'application/json'}
            rp = requests.post(
                fhirbaseURL, headers=header, json=json_patient)
            print("Status code : ", rp.status_code)
            print("Print the entire Post Request : ")
            print(rp.text)

@app.route("/")
def home():
    return render_template("Welcome_Page.html")

@app.route("/upload")
def upload():
    return render_template("upload.html",methods=["GET", "POST"])

@app.route("/parse")
def parse():
    return render_template("parse.html")

@app.route("/upload_result")
def result():
    return render_template("upload_result.html")




if __name__ == "__main__":
    app.run(debug=True)
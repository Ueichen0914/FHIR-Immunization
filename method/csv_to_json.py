import csv
import json
import requests

header = {'Content-Type': 'application/json'}
fhirbaseURL = 'https://hapi.fhir.tw/fhir/Patient'


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

# def parse_csv(file):

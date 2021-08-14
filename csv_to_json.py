import csv
import json
import requests
from pprint import pprint


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


# def immunization(dic1):
#     with open(
#         "JSON_template\Immunization.json", "r", encoding="utf-8"
#     ) as Immunization_json:
#         immunization = json.load(Immunization)
#     for key, value in dic1.items():
#         if key == "姓名":
#             patient["name"][0]["text"] = value
#         elif key == "身分證":
#             patient["identifier"][0]["value"] = value
#         elif key == "性別":
#             patient["gender"] = value
#         elif key == "生日":
#             patient["birthDate"] = value
#         else:
#             pass
#     return immunization


file = "csv_example\FHIR resource.csv"
with open(file) as f:
    text = csv.DictReader(f)
    for line in text:
        json_patient = json.dumps(
            patient(line), sort_keys=False, indent=4, ensure_ascii=False
        )
        # json_immunization = json.dumps(
        #     immunization(line), sort_keys=True, indent=4, ensure_ascii=False
        # )
        print(json_patient)
        # print(json_immunization)
        rp = requests.post("https://hapi.fhir.tw/fhir/Patient", json=json_patient)
        print("Status code : ", rp.status_code)
        print("Print the entire Post Request : ")
        print(rp.json())
        # print(json.dump(rp.json(), indent=4, ensure_ascii=False))


# r = requests.post("https://hapi.fhir.tw/Immunization", json=json_patient)
# print(r.status_code)


# 輸出JSON物件
# json patient
# json immunitzation
# 物件內容
# "resourceType"
# "id"
# "status"
# "vaccineCode"
# "patient"
# "lotNumber"
# "site"
# "route"
# "doseQuantity"
# "protocolApplied"
# "performer"

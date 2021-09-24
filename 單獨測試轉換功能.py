import csv
import json
import requests

headers = {'Content-Type': 'application/json'}
fhirbaseURL = "https://hapi.fhir.tw/fhir"


def patient(dic):
    with open(
            "JSON_template\Patient_template.json", "r", encoding="utf-8") as patient_json:
        patient = json.load(patient_json)
    for key, value in dic.items():
        if key == "LV_UUID":
            # 加入id
            patient["id"] = str(value)
        elif key == "SEX":
            # 判斷性別
            if value == "1":
                info = "male"
            elif value == "2":
                info = "female"
            elif value == "3" | "4":
                info = "other"
            elif value == "9":
                info = "unknown"
            patient["gender"] = info
        elif key == "BIRTH_Y":
            # 判斷生日(民國)，放入svalue
            ivalue = int(value)
            if ivalue < 2000000:
                ivalue += 19110000
            svalue = str(ivalue)
            # 西元加入"-"放入ssvalue
            ssvalue = svalue[:4] + "-" + svalue[4:6] + "-" + svalue[6:8]
            patient["birthDate"] = ssvalue
        elif key == "RESID":
            # 加入地址
            patient["address"][0]["postalCode"] = str(value)
        elif key == "FU_DT":
            # 判斷生日(民國)，放入svalue
            ivalue = int(value)
            if ivalue < 2000000:
                ivalue += 19110000
            svalue = str(ivalue)
            # 西元加入"-"放入ssvalue
            ssvalue = svalue[:4] + "-" + svalue[4:6] + "-" + svalue[6:8]
            patient["deceasedDateTime"] = ssvalue
        # deceased boolean 和 datetime擇一
        # elif key == "VSTATUS":
        #     if value == "1":
        #         info = False
        #     else:
        #         info = True
        #     patient["deceasedBoolean"] = info
        else:
            pass
    return patient


file = "csv_example\FHIR_test.csv"
with open(file) as f:
    text = csv.DictReader(f)
    for line in text:
        json_patient = json.dumps(patient(line))
        for key, value in line.items():
            if key == "LV_UUID":
                fhirresourceURL = fhirbaseURL + "/Patient/" +str(value)
        r_patient = requests.put(
            fhirresourceURL, headers=headers, data=json_patient)
        print(r_patient.text)

import csv
import json
import requests
import datetime

headers = {'Content-Type': 'application/json'}
fhirbaseURL = "http://localhost:8070/fhir"


def patient(dic):
    with open(
            "/mnt/bgcdb/fhir/JSON_template/Patient_template.json", "r", encoding="utf-8") as patient_json:
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


def observation_height(dic):
    with open(
            "/mnt/bgcdb/fhir/JSON_template/Observation_Body_height.json", "r", encoding="utf-8") as height_json:
        height = json.load(height_json)
    for key, value in dic.items():
        if key == "HEIGHT":
            height["valueQuantity"]["value"] = float(value)
        elif key == "LV_UUID":
            height["subject"]["reference"] = "Patient/" + str(value)
        else:
            pass
    height["effectiveDateTime"] = str(datetime.date.today())
    return height


def observation_weight(dic):
    with open(
            "/mnt/bgcdb/fhir/JSON_template/Observation_Body_weight.json", "r", encoding="utf-8") as weight_json:
        weight = json.load(weight_json)
    for key, value in dic.items():
        if key == "WEIGHT":
            weight["valueQuantity"]["value"] = int(value)
        elif key == "LV_UUID":
            weight["subject"]["reference"] = "Patient/" + str(value)
        else:
            pass
    weight["effectiveDateTime"] = str(datetime.date.today())
    return weight


# 不太確定smoking要填哪個欄位
def observation_smoking(dic):
    with open(
            "/mnt/bgcdb/fhir/JSON_template/Smoking_Behavior.json", "r", encoding="utf-8") as smoke_json:
        smoke = json.load(smoke_json)
    for key, value in dic.items():
        if key == "SMOKING":
            smoke["code"]["coding"][0]["display"] = str(value)
        elif key == "LV_UUID":
            smoke["subject"]["reference"] = "Patient/" + str(value)
        else:
            pass
    smoke["effectiveDateTime"] = str(datetime.date.today())
    return smoke


# 為甚麼一下是放在code一下是放在display欄位??
def observation_betalnut(dic):
    with open(
            "/mnt/bgcdb/fhir/JSON_template/Betel_Nut_Chewing_Behavior.json", "r", encoding="utf-8") as betal_json:
        betal = json.load(betal_json)
    for key, value in dic.items():
        if key == "BTCHEW":
            betal["code"]["coding"][0]["code"] = str(value)
        elif key == "LV_UUID":
            betal["subject"]["reference"] = "Patient/" + str(value)
        else:
            pass
    betal["effectiveDateTime"] = str(datetime.date.today())
    return betal


def observation_drinking(dic):
    with open(
            "/mnt/bgcdb/fhir/JSON_template/Drinking_Behavior.json", "r", encoding="utf-8") as drinking_json:
        drinking = json.load(drinking_json)
    for key, value in dic.items():
        if key == "DRINKING":
            drinking["code"]["coding"][0]["display"] = str(value)
        elif key == "LV_UUID":
            drinking["subject"]["reference"] = "Patient/" + str(value)
        else:
            pass
    drinking["effectiveDateTime"] = str(datetime.date.today())
    return drinking


def observation_performance(dic):
    with open(
            "/mnt/bgcdb/fhir/JSON_template/PERFORMANCE.json", "r", encoding="utf-8") as performance_json:
        performance = json.load(performance_json)
    for key, value in dic.items():
        if key == "PERFORMANCE":
            performance["code"]["coding"][0]["display"] = str(value)
        elif key == "LV_UUID":
            performance["subject"]["reference"] = "Patient/" + str(value)
        else:
            pass
    performance["effectiveDateTime"] = str(datetime.date.today())
    return performance


def observation_SSF(dic, num):
    with open(
            "/mnt/bgcdb/fhir/JSON_template/SSF_template.json", "r", encoding="utf-8") as SSF_json:
        SSF = json.load(SSF_json)
    SSFNUM = "SSF" + num
    SSF["code"]["coding"][0]["code"] = SSFNUM
    for key, value in dic.items():
        if key == SSFNUM:
            SSF["code"]["coding"][0]["display"] = str(value)
        elif key == "LV_UUID":
            SSF["subject"]["reference"] = "Patient/" + str(value)
        else:
            pass
    SSF["effectiveDateTime"] = str(datetime.date.today())
    return SSF


# def observation_tumor(dic):
#     with open(
#             "JSON_template\tumor_size.json", "r", encoding="utf-8") as tumor_json:
#         tumor = json.load(tumor_json)
#     for key, value in dic.items():
#         if key == "TSIZE_C":
#             tumor["component"][0]["code"]["coding"][0]["display"] = str(value)
#         elif key == "LV_UUID":
#             tumor["subject"]["reference"] = "Patient/" + str(value)
#         else:
#             pass
#     tumor["effectiveDateTime"] = str(datetime.date.today())
#     return tumor


# def observation_lymph(dic):
#     with open(
#             "JSON_template\tumor_size.json", "r", encoding="utf-8") as lymph_json:
#         lymph = json.load(lymph_json)
#     for key, value in dic.items():
#         if key == "NEXAM":
#             lymph["component"][0]["valueQuantity"]["value"] = int(value)
#         elif key == "NPOSIT":
#             lymph["component"][1]["valueQuantity"]["value"] = int(value)
#         elif key == "LV_UUID":
#             lymph["subject"]["reference"] = "Patient/" + str(value)
#         else:
#             pass
#     lymph["effectiveDateTime"] = str(datetime.date.today())
#     return lymph


file = "/mnt/bgcdb/fhir/FHIR_test.csv"
with open(file) as f:
    text = csv.DictReader(f)
    for line in text:
        # Put Patient
        json_patient = json.dumps(patient(line))
        for key, value in line.items():
            if key == "LV_UUID":
                fhirresourceURL = fhirbaseURL + "/Patient/" + str(value)
        r_patient = requests.put(
            fhirresourceURL, headers=headers, data=json_patient)
        print(r_patient.text)
        # Post Height
        json_ob = json.dumps(observation_height(line))
        fhirresourceURL = fhirbaseURL + "/Observation"
        r_ob = requests.post(
            fhirresourceURL, headers=headers, data=json_ob)
        print(r_ob.text)
        # Post Weight
        json_ob = json.dumps(observation_weight(line))
        fhirresourceURL = fhirbaseURL + "/Observation"
        r_ob = requests.post(
            fhirresourceURL, headers=headers, data=json_ob)
        print(r_ob.text)
        # Post Smoking
        json_ob = json.dumps(observation_smoking(line))
        fhirresourceURL = fhirbaseURL + "/Observation"
        r_ob = requests.post(
            fhirresourceURL, headers=headers, data=json_ob)
        print(r_ob.text)
        # Post Betalnut
        json_ob = json.dumps(observation_betalnut(line))
        fhirresourceURL = fhirbaseURL + "/Observation"
        r_ob = requests.post(
            fhirresourceURL, headers=headers, data=json_ob)
        print(r_ob.text)
        # Post Drinking
        json_ob = json.dumps(observation_drinking(line))
        fhirresourceURL = fhirbaseURL + "/Observation"
        r_ob = requests.post(
            fhirresourceURL, headers=headers, data=json_ob)
        print(r_ob.text)
        # Post Performance
        json_ob = json.dumps(observation_performance(line))
        fhirresourceURL = fhirbaseURL + "/Observation"
        r_ob = requests.post(
            fhirresourceURL, headers=headers, data=json_ob)
        print(r_ob.text)
        # Post SSF
        for i in range(10):
            json_ob = json.dumps(observation_SSF(line, str(i+1)))
            fhirresourceURL = fhirbaseURL + "/Observation"
            r_ob = requests.post(
                fhirresourceURL, headers=headers, data=json_ob)
            print(r_ob.text)
        # Post Tumor size
        # json_ob = json.dumps(observation_tumor(line))
        # fhirresourceURL = fhirbaseURL + "/Observation"
        # r_ob = requests.post(
        #     fhirresourceURL, headers=headers, data=json_ob)
        # print(r_ob.text)
        # Post Lymph
        # json_ob = json.dumps(observation_lymph(line))
        # fhirresourceURL = fhirbaseURL + "/Observation"
        # r_ob = requests.post(
        #     fhirresourceURL, headers=headers, data=json_ob)
        # print(r_ob.text)

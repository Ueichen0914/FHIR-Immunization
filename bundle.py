import csv
import json
import requests
from datetime import datetime
import time

headers = {'Content-Type': 'application/json'}
fhirbaseURL = "https://hapi.fhir.tw/fhir"


def patient(dic):
    with open("Bundle_template\Bundle_Patient.json", "r", encoding="utf-8") as patient_json:
        patient_r = json.load(patient_json)
        patient = patient_r["resource"]
    for key, value in dic.items():
        if key == "LV_UUID":
            # 加入id
            patient["id"] = str(value)
            patient_r["request"]["url"] = fhirbaseURL + "/Patient/" + str(value)
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
            try:
                d_format = datetime.strptime(svalue, "%Y-%m-%d")
            except:
                continue
            patient["birthDate"] = d_format.strftime("%Y-%m-%d")
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
    return patient


def observation_height(dic):
    with open(
            "JSON_template\Observation_Body_height.json", "r", encoding="utf-8") as height_json:
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
            "JSON_template\Observation_Body_weight.json", "r", encoding="utf-8") as weight_json:
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


def observation_smoking(dic):
    with open(
            "JSON_template\Smoking_Behavior.json", "r", encoding="utf-8") as smoke_json:
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


def observation_betalnut(dic):
    with open(
            "JSON_template\Betel_Nut_Chewing_Behavior.json", "r", encoding="utf-8") as betal_json:
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
            "JSON_template\Drinking_Behavior.json", "r", encoding="utf-8") as drinking_json:
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
            "JSON_template\PERFORMANCE.json", "r", encoding="utf-8") as performance_json:
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
            "JSON_template\SSF_template.json", "r", encoding="utf-8") as SSF_json:
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


def observation_tumor(dic):
    with open(
            "JSON_template\Tumor_size.json", "r", encoding="utf-8") as tumor_json:
        tumor = json.load(tumor_json)
    for key, value in dic.items():
        if key == "TSIZE_C":
            tumor["component"][0]["code"]["coding"][0]["display"] = str(value)
        elif key == "LV_UUID":
            tumor["subject"]["reference"] = "Patient/" + str(value)
        else:
            pass
    tumor["effectiveDateTime"] = str(datetime.date.today())
    return tumor


def observation_lymph(dic):
    with open(
            "JSON_template\Lymph.json", "r", encoding="utf-8") as lymph_json:
        lymph = json.load(lymph_json)
    for key, value in dic.items():
        if key == "NEXAM":
            lymph["component"][0]["valueQuantity"]["value"] = int(value)
        elif key == "NPOSIT":
            lymph["component"][1]["valueQuantity"]["value"] = int(value)
        elif key == "LV_UUID":
            lymph["subject"]["reference"] = "Patient/" + str(value)
        else:
            pass
    lymph["effectiveDateTime"] = str(datetime.date.today())
    return lymph


file = "csv_example\FHIR_test.csv"

with open(file) as f:
    text = csv.DictReader(f)
    for line in text:
        with open(
                "Bundle_template\Bundle.json", "r", encoding="utf-8") as Bundle_json:
            bundle = json.load(Bundle_json)
        for key,value in line.items():
            patient(line)
            

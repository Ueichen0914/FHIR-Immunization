import csv
import json
import requests
from datetime import date

headers = {'Content-Type': 'application/json'}
fhirbaseURL = "https://hapi.fhir.tw/fhir"


def observation_height(key, value, ID, time, JSON):
    logic = False
    if key == "HEIGHT":
        JSON["resource"]["valueQuantity"]["value"] = float(value)
        logic = True
        print(JSON)
    else:
        pass
    JSON["resource"]["effectiveDateTime"] = time
    JSON["resource"]["id"] = ID
    JSON["request"]["url"] = "Observation/" + ID
    return JSON, logic


def observation_weight(key, value, ID, time, JSON):
    logic = False
    if key == "WEIGHT":
        JSON["resource"]["valueQuantity"]["value"] = int(value)
        logic = True
        print(JSON)
    else:
        pass
    JSON["resource"]["effectiveDateTime"] = time
    JSON["resource"]["id"] = ID
    JSON["request"]["url"] = "Observation/" + ID
    return JSON, logic


# def observation_smoking(key, value, ID, time, JSON):
#     if key == "SMOKING":
#         JSON["resource"]["code"]["coding"][0]["display"] = str(value)
#     else:
#         pass
#     smoke["effectiveDateTime"] = str(datetime.date.today())
#     return smoke


# def observation_betalnut(dic):
#     with open(
#             "JSON_template\Betel_Nut_Chewing_Behavior.json", "r", encoding="utf-8") as betal_json:
#         betal = json.load(betal_json)
#     for key, value in dic.items():
#         if key == "BTCHEW":
#             betal["code"]["coding"][0]["code"] = str(value)
#         elif key == "LV_UUID":
#             betal["subject"]["reference"] = "Patient/" + str(value)
#         else:
#             pass
#     betal["effectiveDateTime"] = str(datetime.date.today())
#     return betal


# def observation_drinking(dic):
#     with open(
#             "JSON_template\Drinking_Behavior.json", "r", encoding="utf-8") as drinking_json:
#         drinking = json.load(drinking_json)
#     for key, value in dic.items():
#         if key == "DRINKING":
#             drinking["code"]["coding"][0]["display"] = str(value)
#         elif key == "LV_UUID":
#             drinking["subject"]["reference"] = "Patient/" + str(value)
#         else:
#             pass
#     drinking["effectiveDateTime"] = str(datetime.date.today())
#     return drinking


# def observation_performance(dic):
#     with open(
#             "JSON_template\PERFORMANCE.json", "r", encoding="utf-8") as performance_json:
#         performance = json.load(performance_json)
#     for key, value in dic.items():
#         if key == "PERFORMANCE":
#             performance["code"]["coding"][0]["display"] = str(value)
#         elif key == "LV_UUID":
#             performance["subject"]["reference"] = "Patient/" + str(value)
#         else:
#             pass
#     performance["effectiveDateTime"] = str(datetime.date.today())
#     return performance


# def observation_SSF(dic, num):
#     with open(
#             "JSON_template\SSF_template.json", "r", encoding="utf-8") as SSF_json:
#         SSF = json.load(SSF_json)
#     SSFNUM = "SSF" + num
#     SSF["code"]["coding"][0]["code"] = SSFNUM
#     for key, value in dic.items():
#         if key == SSFNUM:
#             SSF["code"]["coding"][0]["display"] = str(value)
#         elif key == "LV_UUID":
#             SSF["subject"]["reference"] = "Patient/" + str(value)
#         else:
#             pass
#     SSF["effectiveDateTime"] = str(datetime.date.today())
#     return SSF


# def observation_tumor(dic):
#     with open(
#             "JSON_template\Tumor_size.json", "r", encoding="utf-8") as tumor_json:
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
#             "JSON_template\Lymph.json", "r", encoding="utf-8") as lymph_json:
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


def output(logic, json, bundle):
    if logic:
        bundle["entry"].append(json)
        print(bundle)
    return bundle


file = "csv_example\FHIR_test.csv"
with open(file) as f:
    text = csv.DictReader(f)
    time = str(date.today())
    for line in text:
        with open("Bundle_template\Bundle.json", "r", encoding="utf-8") as Bundle_json:
            bundle = json.load(Bundle_json)
        with open("Bundle_template\Bundle_Observation_Body_height.json", "r", encoding="utf-8") as height_json:
            height = json.load(height_json)
        with open("Bundle_template\Bundle_Observation_Body_weight.json", "r", encoding="utf-8") as weight_json:
            weight = json.load(weight_json)
        with open("Bundle_template\Bundle_Smoking_Behavior.json", "r", encoding="utf-8") as smoke_json:
            smoke = json.load(smoke_json)
        for key, value in line.items():
            if key == "LV_UUID":
                ID = str(value)
        for key, value in line.items():
            JSON, logic = observation_height(key, value, ID, time, height)
            bundle = output(logic, JSON, bundle)
            JSON, logic = observation_weight(key, value, ID, time, weight)
            bundle = output(logic, JSON, bundle)
        print(bundle)
        # json_bundle = json.dumps(bundle)
        # r_b = requests.post(
        #     fhirbaseURL, headers=headers, data=json_bundle)
        # print(r_b.text)

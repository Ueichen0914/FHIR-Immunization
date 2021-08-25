import requests
import json

headers = {'Content-Type': 'application/json'}
fhirbaseURL = 'https://hapi.fhir.tw/fhir/Patient'
patient_json = {
    "resourceType": "Patient",
    "meta": {
        "versionId": "7",
        "lastUpdated": "2021-07-13T20:45:28.026+08:00",
        "source": "#DGp1qyt6D3hgfIHY"
    },
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><div class=\"hapiHeaderText\">小明 <b>王 </b></div><table class=\"hapiPropertyTable\"><tbody><tr><td>Identifier</td><td>A123456789</td></tr><tr><td>Address</td><td><span>Van Egmondkade 23 </span><br/><span>Amsterdam </span><span>NLD </span></td></tr><tr><td>Date of birth</td><td><span>12 January 1773</span></td></tr></tbody></table></div>"
    },
    "identifier": [
        {
            "use": "usual",
            "system": "http://nema.org/examples/patients",
            "value": "F123456789"
        }
    ],
    "name": [
        {
            "use": "official",
            "text": "陳大名"
        }
    ],
    "telecom": [
        {
            "system": "phone",
            "value": "0648352638",
            "use": "mobile"
        },
        {
            "system": "email",
            "value": "p.heuvel@gmail.com",
            "use": "home"
        }
    ],
    "gender": "male",
    "birthDate": "1999-01-01",
    "address": [
        {
            "use": "home",
            "line": [
                "Van Egmondkade 23"
            ],
            "city": "Amsterdam",
            "postalCode": "1024 RJ",
            "country": "NLD"
        }
    ]
}

r = requests.post(fhirbaseURL, headers=headers, data=json.dumps(patient_json))
print("Status code : ", r.status_code)
print(r.text)

import requests
import json

def get_data_covid():
    global covid_reply
    response = requests.get('https://covid19.th-stat.com/api/open/today')
    if response:
        print('Request is successful.')
    else:
        print('Request returned an error.')

    data = response.text

    parsed = json.loads(data)

    print(json.dumps(parsed, indent=4))

    เพิ่มวันนี้ = parsed["NewConfirmed"]
    รักษาอยู่ในรพ = parsed["Hospitalized"]
    หายวันนี้ = parsed["NewRecovered"]
    รวมทั้งหมด = parsed["Confirmed"]
    หายทั้งหมด = parsed["Recovered"]
    ตายทั้งหมด = parsed["Deaths"]
    covid_reply = (f"เพิ่มวันนี้ = {เพิ่มวันนี้}\nรักษาอยู่ในรพ. = {รักษาอยู่ในรพ}\nหายวันนี้ = {หายวันนี้}\nรวมทั้งหมด = {รวมทั้งหมด}")
    return covid_reply

def get_update_date():
    global UpdateDate
    response = requests.get('https://covid19.th-stat.com/api/open/today')
    data = response.text
    parsed = json.loads(data)
    UpdateDate = parsed["UpdateDate"]
    return UpdateDate

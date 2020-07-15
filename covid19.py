
import requests
import json


def find(lst, key, value):
	for i, dic in enumerate(lst):
		if dic[key].lower() == value.lower():
			return i

def get_update_date(code):


	response = requests.get('https://api.covid19api.com/summary')

	if response:
		print('Request is successful.')
	else:
		print('Request returned an error.')

	data = response.text

	parsed = json.loads(data)

	parsed = parsed['Countries']

	data_country = find(parsed,'CountryCode',code)

	if data_country == None:
		return 'No data avaliable'
	else:
		parsed = parsed[data_country]
		UpdateDate = parsed["Date"]
		return UpdateDate

def get_data_wovid():
	response = requests.get('https://api.covid19api.com/summary')
	if response:
		print('Request is successful.')
	else:
		print('Request returned an error.')

	data = response.text

	parsed = json.loads(data)

	print(json.dumps(parsed, indent=4))

	parsed = parsed['Global']

	newtoday = parsed["NewConfirmed"]
	recoveredtoday = parsed["NewRecovered"]
	diedtoday = parsed['NewDeaths']
	allcase = parsed["TotalConfirmed"]
	recovered = parsed["TotalRecovered"]
	dead = parsed["TotalDeaths"]
	recovering = allcase-dead-recovered

	covid_reply = (f"New cases today = {newtoday}\nRecovered Today = {recoveredtoday}\nDied today  = {diedtoday}\nAll cases = {allcase}\nAll deaths = {dead}\nAll Recovered = {recovered}\nRecovering = {recovering}")
	return covid_reply

def get_data_covid(country):

	response = requests.get('https://api.covid19api.com/summary')

	if response:
		print('Request is successful.')
	else:
		print('Request returned an error.')

	data = response.text

	parsed = json.loads(data)

	parsed = parsed['Countries']

	data_country = find(parsed,'Country',country)
	if data_country == None:
		data_country = find(parsed,'CountryCode',country)


	if data_country == None:
		return 'No data avaliable for this country,correct syntax is [=covid thailand] , [=covid th] , [=covid  "united states of america"] , [=covid us]'

	else:
		parsed = parsed[data_country]
		newtoday = parsed["NewConfirmed"]
		recoveredtoday = parsed["NewRecovered"]
		diedtoday = parsed['NewDeaths']
		allcase = parsed["TotalConfirmed"]
		recovered = parsed["TotalRecovered"]
		dead = parsed["TotalDeaths"]
		recovering = allcase-dead-recovered

		covid_reply = (f"New cases today = {newtoday}\nRecovered Today = {recoveredtoday}\nDied today  = {diedtoday}\nAll cases = {allcase}\nAll deaths = {dead}\nAll recovered = {recovered}\nRecovering = {recovering}")

		return covid_reply

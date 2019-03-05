import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_state_gdps():
	# use creds to create a client to interact with the Google Drive API
	scope = ['https://www.googleapis.com/auth/drive.readonly']
	creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
	client = gspread.authorize(creds)

	# Find a workbook by name and open the first sheet
	# Make sure you use the right name here.
	sheet = client.open("State GDPs").sheet1

	# Extract and print all of the values
	state_gdp_array= sheet.get_all_values()

	state_gdp_dict = {}

	for i in range(2,len(state_gdp_array)):
		row = state_gdp_array[i]
		state_gdp_dict[row[0]] = int(row[1])
	
	return state_gdp_dict
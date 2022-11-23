import gspread 
from datetime import date
from bs4 import BeautifulSoup
from oauth2client.service_account import ServiceAccountCredentials
# test
try:
    try:
        print('Connecting to Google Drive')

        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name('BugCatcher-050529d2806d.json', scope)
        client = gspread.authorize(creds)
        sheet = client.open('Bug Catcher').sheet1
        data = sheet.get_all_records()
        date = date.today()

        print('Connection Established\n')

    except Exception as ex:
        print('An error occured while trying to connect to Google Drive')

    def theNet():
        os = input('Operating System:\n').title()
        language = input('Language:\n').title()
        application = input('Application:\n').title()
        errorNum= input('Error Number:\n')
        errMsg= input('Error Message:\n')
        cause= input('Cause:\n')
        solution= input('Solution:\n')
        codeSolution = input('Code Solution\n')
        tags= input('Tags (for searching):\n').title()

        print('Catching bug')

        values = [str(date), str(os), str(language), str(application), str(errorNum), str(errMsg), str(cause), str(solution), str(codeSolution), str(tags)]
        sheet.insert_row(values, 2)

        input('Bug has been captured!')

    theNet()

except Exception as ex:
    print(ex)

# ----------------------------- NOTES -----------------------------

# Further input standardisation required
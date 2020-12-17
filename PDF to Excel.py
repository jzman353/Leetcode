#Not sure why the package can't be used in pycharm but it works in IDLE

import pdftables_api
c = pdftables_api.Client('my_personal_API_code')

import os
os.chdir('/Users/jzalmano/Documents/') #FOLDER_PATH_GOES_HERE

#Change 'output' to be any name you want the excel spreadsheet to be named
#Change PDF_NAME_GOES_HERE to be whatever the name of the pdf is
c.xlsx('PDF_NAME_GOES_HERE.pdf', 'output')

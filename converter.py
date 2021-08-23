import pdftables_api
import glob,os
import requests
import sys

r = requests.get('https://pdftables.com/api/remaining?key=mlnolmd51ohn')
print(r.text+" page remaining...")

if int(r.text) == 0:
    print("oppa, sayonnara.. API limit reached!")
    exit()
else:
    c = pdftables_api.Client('mlnolmd51ohn')
    os.chdir("/home/robbi/Documents/workplace/python/PDFtable_API")
    for file in glob.glob("*.pdf"):
        print("Converting "+file+ " to excell")
        c.xlsx(file,file+".xlsx")
        print("Done!")

#replace c.xlsx with c.csv to convert to CSV
#replace c.xlsx with c.xml to convert to XML
#replace c.xlsx with c.html to convert to HTML

import pdftables_api
import glob,os
c = pdftables_api.Client('3hmaxz5atb7i')
os.chdir("/home/rnm/workplace/PDF-to-Excell")
for file in glob.glob("*.pdf"):
    print("Converting "+file+ " to excell")
    c.xlsx(file,file+".xlsx")
    print("Done!")

#replace c.xlsx with c.csv to convert to CSV
#replace c.xlsx with c.xml to convert to XML
#replace c.xlsx with c.html to convert to HTML

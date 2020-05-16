#ValImpAmount = round(float("{0:.2f}".format(float("131040.0"))),2)
#ValImpAmount = format(ValImpAmount, '.2f')
#print(ValImpAmount)
import hashlib
CUDE_string = "ND1"+"2019-06-21"+"09:15:23-05:00"+"12600.06"+"01"+"2394.01"+"04"+"0.00"+"03"+"0.00"+"14994.07"+"900508908"+"900108281"+"20191"+"2"
CUDE_string = "SETP099000003"+"2019-12-01"+"13:52:45-05:00"+"600000.00"+"01"+"0.00"+"04"+"0.00"+"03"+"0.00"+"600000.00"+"1112768143"+"PER20573858124"+"19891"+"2"
CUDE_sha384 = hashlib.sha384(str(CUDE_string).encode('utf-8')).hexdigest()
print (CUDE_sha384)

from lxml import etree
import json
from xml.dom import minidom
#/odoo_dian_v12/custom/addons/dian_efact/models/xml/XMLDian/res.country.state.csv      CodeList  
tree = etree.parse("/odoo_dian_v12/custom/addons/dian_efact/models/xml/XMLDian/Municipio-2.1.xml")
csv = open("/odoo_dian_v12/custom/addons/dian_efact/models/xml/XMLDian/res.country.state.csv","w") 

CodeList = tree.getroot()
for SimpleCodeList in CodeList.iter("SimpleCodeList"):
    for Row in SimpleCodeList.iter("Row"):
        for Value in Row.iter("Value"):
            ColumnRef = Value.get("ColumnRef")
            SimpleValue = Value.find("SimpleValue")
            if(str(ColumnRef) == "code"):                
                code = SimpleValue.text
            else:
                name = SimpleValue.text
            
        code = str('"')+str(code)+str('"')
        name = str('"')+str(name.encode('utf-8'))+str('"')
        country = str('"')+str("base.co")+str('"')
        line_break = str('\n')
        line = str(code) + str(",") + str(name) + str(",") + str(country) + str(line_break)
        csv.write(line)

csv.close()



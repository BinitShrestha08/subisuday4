

import re
import mysql.connector

# mydb= mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password= 'Binit@1234',
#     port= "3306",
#     database='mydatabase'
# )


####example


from api.models import OLT

def addLog(ts, hostname, phyint, serial):
    log = OLT(timestamp=ts, hostname=hostname, phyinterface=phyint,serialnumber=serial)
    log.save()




##### 3nampl end here

filename= 'huawei-olt.log'

regex= '^[0]+/+[0-7]+/+[0-15]'

# mycursor = mydb.cursor()

# mycursor.execute("CREATE table data1 (Timestamp VARCHAR(255), Hostname VARCHAR(225), PhyInterface VARCHAR(255), SerialNumber VARCHAR(255) )")

# mycursor.execute("ALTER TABLE data1 ADD CONSTRAINT PK_data PRIMARY KEY (Hostname, PhyInterface, SerialNumber)")


# def database(ts, hn, phyInt, sn):
#     if len(sn)== 16:
#         print('working')
#         output= ts + ' ' + hn +' ' + phyInt + ' ' + sn
#                 # print(output)
#         outfile = open('filtered.txt' , 'a')
#         outfile.write(output + '\n')

#         try:
#             insertstate= "INSERT INTO data1 (Timestamp, Hostname, PhyInterface, SerialNumber) VALUES (%s, %s, %s, %s)"
#             val= (ts, hn,phyInt, sn)
            
#             mycursor.execute(insertstate,val)
            
#         except :
#             print('duplicate values detected')

#             # print(mycursor.rowcount, "record inserted."
                
#     else:
#         print("Inavlid Serial number")




with open(filename) as fh:
    for line in fh:
        if 'discovered' in line:
            # print(line)

            description = list(line.strip().split(None, 40))
            # print(description)

            ts= description[0] + ' '+ description[1] + ' ' + description[2]
            # print('timestamp', ts)

            hn= description[3]
            # print('Hostname',hn)

            pi= description[24] + description[26] +description[28]
            phyI= pi.replace(',','/')
            phyInt= phyI[:-1] #splicing the last character
            # print('phy interface',phyInt)

            sno=  description[32]
            sn=sno.replace(',','')

            if (re.search(regex, phyInt)):
                print('all good')
                # database(ts, hn, phyInt, sn)
                # mydb.commit()
            else:
                print("failed")
                print(phyInt)

            
            # print('Serial Number',sn)

# deletestate= "DELETE FROM data1 WHERE SerialNumber = '4857544314DC1F09'"
# mycursor.execute(deletestate)
# mydb.commit()

# mycursor.execute("SELECT * FROM data1")
# myresult = mycursor.fetchall()
# for x in myresult:
#         print('* fromdata1', x)


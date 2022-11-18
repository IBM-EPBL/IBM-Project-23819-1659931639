import ibm_db

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=3883e7e4-18f5-4afe-be8c-fa31c41761d2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31498;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=xmx67961;PWD=SB1BQPsAgSmydQ0t",'','')
print(conn)
print("connection successful")

sql="SELECT * FROM USERS"
stmt = ibm_db.exec_immediate(conn,sql)
dictionary = ibm_db.fetch_assoc(stmt)
while dictionary!=False:
    print("FUll ROW: ",dictionary)
    dictionary=ibm_db.fetch_assoc(stmt)
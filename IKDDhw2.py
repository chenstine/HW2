import psycopg2
import pprint
import texttable
 
conn_str = "host='iservdb.cloudopenlab.org.tw' dbname='chenstine_db_5617' user='chenstine_user_5617' password='QU8H4upb'"
conn = psycopg2.connect(conn_str)

cursor = conn.cursor()

cursor.execute("SELECT text, user_name, user_id FROM ""hw2"" WHERE q = '123' ORDER BY user_id")

records = cursor.fetchall()

tab = texttable.Texttable()
tab.set_cols_width([20,10,20])
row = [records[0][0], records[0][1], records[0][2]]
tab.add_row(row)
s = tab.draw()
x = s.encode('utf8')
print x


#print "%10s %10s %10s" %(records[0][0], records[0][1], records[0][2])
#print "%10s" %(records[0][0])
pprint.pprint("~~~~~~~~~~~~~~~~~~~~~~~~~~")
pprint.pprint(records[0][0])
pprint.pprint("~~~~~~~~~~~~~~~~~~~~~~~~~~")
pprint.pprint(records[0][1])
pprint.pprint("~~~~~~~~~~~~~~~~~~~~~~~~~~")
pprint.pprint(records[0][2])
#!/usr/bin/python
#coding=utf-8
import sys
import psycopg2

def isHalf(ch):
	if ord(ch) > 0x3000:
		return False
	else:
		return True

conn_str = "host='iservdb.cloudopenlab.org.tw' dbname='chenstine_db_5617' user='chenstine_user_5617' password='QU8H4upb'"
conn = psycopg2.connect(conn_str)
conn.set_client_encoding('utf-8')
cursor = conn.cursor()
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE, cursor)

inputname = raw_input("input :")
cursor.execute("SELECT text, user_name, user_id FROM ""hw2"" WHERE q = (%s) ORDER BY user_id", [inputname])

records = cursor.fetchall()
i = 0
#print type(records[i][0])
print "output:"
print "+----------------------------------------+--------------------+-----------+"
while i < len(records):
	a = 0
	b = 0
	c = 0
	tf1 = True
	tf2 = True
	tf3 = True
	while tf1 or tf2 or tf3:
		print "|",
		j = 0
		while j != 39:
			if a < len(records[i][0]):
				if records[i][0][a] == '\n':
					print " ",
					a += 1
					j += 2
					continue
				if j == 38:
					print "",
					break
				if isHalf(records[i][0][a]):
					j -= 1
				print "\b%c" % records[i][0][a],
				a += 1
			else:
				if j == 38:
					j -= 1
					print "",
				else:
					print " ",
				tf1 = False
			j += 2
		j = 0
		print "|",
		while j != 19:
			if b < len(records[i][1]):
				if j == 18:
					print "",
					break
				if isHalf(records[i][1][b]):
					j -= 1
				print "\b%c" % records[i][1][b],
				b += 1
			else:
				if j == 18:
					j -= 1
					print "",
				else:
					print " ",
				tf2 = False
			j += 2
		j = 0
		print "|",
		while j < 10:
			if c < len(records[i][2]):
				print "\b%c" % records[i][2][c],
				c += 1
			else:
				print "",
				tf3 = False
			j += 1
		print "|"
	print "+----------------------------------------+--------------------+-----------+"
	i += 1

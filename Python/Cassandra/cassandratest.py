"""
iNeuron
"""

from cassandra.cluster import Cluster

cluster=Cluster()

session=cluster.connect('ineruon')
# session.execute("INSERT INTO python_test(id, first_name,last_name) VALUES (uuid(),'ratan','bajaj')")
rows=session.execute("SELECT * FROM emp")
for row in rows:
	print (row.emp_id ,row.emp_city)

print ("Done")
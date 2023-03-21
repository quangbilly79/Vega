from impala.dbapi import connect
from impala.util import as_pandas
import pandas as pd

conn = connect(host='vftsandbox-node02', port=21050)
# 21050 là Impala Deamon Frontend port
# vftsandbox-node02 là Impala Deamon Instance (Check Impala service => Instances trên Cloudera Manager)
# Miễn là Impala Deamon Instance là đc
cursor = conn.cursor()
cursor.execute('SELECT * FROM waka.testtable LIMIT 100')
description = cursor.description  # prints the result set's schema
# [('id', 'INT', None, None, None, None, None), ('name', 'STRING', None, None, None, None, None)]

df = as_pandas(cursor)
print(df)
#    id name
# 0   1    a
# 1   2    b

#results = cursor.fetchall()
#print(results)
# [(1, 'a'), (2, 'b')]

#df = pd.DataFrame(results, columns = [description[0][0], description[1][0]])
#print(df)
#    id name
# 0   1    a
# 1   2    b
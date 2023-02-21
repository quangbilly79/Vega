from impala.dbapi import connect
from impala.util import as_pandas
import pandas as pd

conn = connect(host='172.25.48.129', port=21050) # 21050 la Impala Deamon Frontend port
cursor = conn.cursor()
cursor.execute('SELECT * FROM vega_data.tmp LIMIT 100')
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
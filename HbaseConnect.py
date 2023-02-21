# from pyspark.sql import SparkSession
#
# app_name = "hbase"
# spark = (
#     SparkSession.builder.master("yarn")
#     .appName(app_name)
#     .config("spark.jars", "hbase-spark-1.2.0-cdh5.16.2.jar")
#     .getOrCreate()
# )
#
#
# dataSourceFormat = "org.apache.hadoop.hbase.spark"
#
# readCatalog = """{
#     "table":{"namespace":"namespace_dev", "name":"logs"},
#     "rowkey":"key",
#     "columns":{
#         "key":{"cf":"rowkey", "col":"key", "type":"string"},
#         "ARTICLE":{"cf":"atlas_data","col":"ARTICLE","type":"int"}
#     }
# }"""
#
# readDF = spark.read.options(catalog=readCatalog).format(dataSourceFormat).load()

# spark-shell --jars /home/vgdata/hbase-spark-1.0.1_spark-3.0.1_4.jar,/home/vgdata/hbase-spark-protocol-shaded-1.0.1_spark-3.0.1_4.jar
#--files /etc/hbase/conf/hbase-site.xml --conf spark.driver.extraClassPath=/etc/hbase/conf

import happybase

connection = happybase.Connection('172.25.48.129') # 172.25.48.129:9090 #HBase Thrift Server Port
table = connection.table('testTable')
for key, data in table.rows(['123', 'row_key2']):
    print(key, data)  # prints row key and data for each row
print('---')
# for key, data in table.scan(filter = "SingleColumnValueFilter('familyName1','col1',=,'substring:f1c1')"):
#     print(key, data)

rowAsDict = dict(table.rows(['123', 'row_key2']))
print(rowAsDict)
print(rowAsDict[b'123'])
# table.put(b'row-key', {b'family:qual1': b'value1',
#                        b'family:qual2': b'value2'})
#
# row = table.row(b'row-key')
# print(row[b'family:qual1'])  # prints 'value1'
#
# for key, data in table.rows([b'row-key-1', b'row-key-2']):
#     print(key, data)  # prints row key and data for each row
#
# for key, data in table.scan(row_prefix=b'row'):
#     print(key, data)  # prints 'value1' and 'value2'
#
# row = table.delete(b'row-key')

#scan 'testTable', {FILTER => "SingleColumnValueFilter('familyName1','col1',=,'substring:f1c1')"}
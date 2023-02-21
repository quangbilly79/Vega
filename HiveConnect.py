

from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import *
# warehouse_location points to the default location for managed databases and tables

# Tao Spark Session va cac lenh nhu bthg, sau do chuyen file py vao may ao?, va dung spark-submit
spark = SparkSession. \
    builder.getOrCreate()
df = spark.sql("select id from vega_data.tmp")
df1 = spark.sql("describe vega_data.tmp")
df.show()
df1.show()

# Tao. bang? trong hive datawarehouse tu` df trong Spark
# df.createOrReplaceTempView("mytempTable")
# spark.sql("create table newTmp as select * from mytempTable")

# Tao. bang tu file csv trong hdfs
# createHive = spark.sql("CREATE TABLE IF NOT EXISTS salesrecords( \
#         Region STRING, \
#         Country STRING, \
#         ItemType STRING, \
#         SalesChannel STRING, \
#         OrderPriority STRING, \
#         OrderID INT, \
#         UnitsSold INT, \
#         UnitPrice DECIMAL, \
#         UnitCost DECIMAL, \
#         TotalRevenue DECIMAL, \
#         TotalCost DECIMAL, \
#         TotalProfit DECIMAL) \
#     COMMENT 'Test load csv from hdfs cloudera' \
#     ROW FORMAT DELIMITED \
#     FIELDS TERMINATED BY ',' \
#     STORED AS TEXTFILE \
#     location '/user/hdfs/salesrecords.csv' \
#     tblproperties ('skip.header.line.count'='1')")

# Load data vao bang trong hive tu nguon` bat ki
# LOAD DATA INPATH '/user/vgdata/salesrecords.csv' INTO TABLE vegadata.salesrecords;



# spark-submit \
# --name "example_job" \
# --master yarn \
# --deploy-mode cluster \
# --jars "/home/vgdata/hive-warehouse-connector_2.11-1.0.0.7.2.15.0-147.jar"
# --conf spark.sql.hive.hiveserver2.jdbc.url="jdbc:hive2://localhost:10000" \
# --conf spark.datasource.hive.warehouse.load.staging.dir=/tmp \
# --conf spark.sql.extensions="com.hortonworks.spark.sql.rule.Extensions" \
# --conf spark.kryo.registrator=com.qubole.spark.hiveacid.util.HiveAcidKyroRegistrator \
# --conf spark.datasource.hive.warehouse.read.mode=DIRECT_READER_V1 \
# HiveConnect.py

#beeline -u jdbc:hive2://172.25.48.129:10000/vega_data -e "select * from tmp"
#beeline -u jdbc:hive2://172.25.48.129:10000/vega_data -f hivehql.hql
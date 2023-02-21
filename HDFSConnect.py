from pyspark import SparkContext, SparkConf
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession
import pyspark

# spark = (SparkSession
#                 .builder
#                 .appName('hdfs_test')
#                 .getOrCreate()
#                 )
# lines = spark.textFile("hdfs://172.25.48.129:8020/user/hdfs/test.txt")
# print(lines)

sc = SparkContext("local", "First App")
lines = sc.textFile(name="hdfs://172.25.48.129:8020/user/hdfs/test.txt")
print(lines)

#spark-shell --conf "spark.yarn.access.hadoopFileSystems=hdfs://192.168.140.160:8020/user/hdfs/test/salesrecords.csv"
#val df = sc.read.format("json").load("hdfs://192.168.140.160:8020/user/hdfs/test/salesrecords.csv")
# spark-submit --master yarn --deploy-mode cluster HDFSConnect.py
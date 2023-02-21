import pyspark
from pyspark.sql import *


spark = SparkSession \
    .builder \
    .appName('test') \
    .master('local[*]') \
    .config('spark.driver.extraClassPath', 'C:\SparkEverything\spark3_3_0\jars\mysql-connector-java-8.0.30') \
    .getOrCreate()

# IP 192.168.140.160 LabServer, Port 3306, Database dev, User dev, Pass Vega123312##, Table dev
localDF = spark.read \
    .format("jdbc") \
    .option("url","jdbc:mysql://192.168.140.1601:3306/dev") \
    .option("driver","com.mysql.cj.jdbc.Driver") \
    .option("dbtable","adf") \
    .option("user","dev") \
    .option("password","Vega123312##") \
    .load()

localDF.select("*").show()
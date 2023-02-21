from pyspark.sql import *


spark = (SparkSession
                .builder
                .appName('hdfs_test')
                .getOrCreate()
                )

dept = [("Finance",10),
        ("Marketing",20),
        ("Sales",30),
        ("IT",40)
      ]

deptColumns = ["dept_name","dept_id"]
deptDF = spark.createDataFrame(data=dept, schema = deptColumns)
deptDF.printSchema()
deptDF.show(truncate=False)

#lines = sc.textFile("hdfs://172.25.48.129:8020/user/hdfs/test.txt") #http://vftsandbox-namenode:9870/
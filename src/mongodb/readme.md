```shell
# verify pyspark version
# 3.3.1
pyspark --version
```

```shell
# init spark {app} ~ classpath
# jars location
file:/usr/local/lib/python3.9/site-packages/pyspark/jars/

# connector
# move to jars folder
https://www.mongodb.com/products/spark-connector
https://github.com/mongodb/mongo-spark
https://mvnrepository.com/artifact/org.mongodb.spark/mongo-spark-connector

# copy files
# /Users/luanmorenomaciel/GitHub/series-spark/src/mongodb/jars
cp * /usr/local/lib/python3.9/site-packages/pyspark/jars/
```
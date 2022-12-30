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
https://mvnrepository.com/artifact/net.snowflake/snowflake-jdbc/3.13.26
https://mvnrepository.com/artifact/net.snowflake/spark-snowflake_2.13/2.11.1-spark_3.3

# copy files
# /Users/luanmorenomaciel/GitHub/series-spark/src/snowflake/jars
cp * /usr/local/lib/python3.9/site-packages/pyspark/jars/
 ls | grep snowflake 
```
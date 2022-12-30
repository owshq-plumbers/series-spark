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
https://cloud.google.com/dataproc/docs/concepts/connectors/cloud-storage#clusters
https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-hadoop3-latest.jar

# copy files
# /Users/luanmorenomaciel/GitHub/series-spark/src/gcs/jars
cp gcs-connector-hadoop3-latest.jar /usr/local/lib/python3.9/site-packages/pyspark/jars/
ls | grep gcs
```
# https://spark.apache.org/docs/latest/submitting-applications.html

```shell
spark-submit --help
```

```shell
--deploy-mode
# cluster = driver runs on one of worker nodes
# [client | default] = driver runs locally where you are submitting app ~ not used for production

--master
# yarn = cluster resources
# mesos = mesos://host:port
# standalone = spark://host:port
# kubernetes = k8s://host:port
# local = local
```

```shell
option | description
--driver-memory	| memory to be used by the spark driver
--driver-cores | cpu cores to be used by the spark driver
--num-executors	| the total number of executors to use
--executor-memory | amount of memory to use for the executor process
--executor-cores | number of cpu cores to use for the executor process
--total-executor-cores | the total number of executor cores to use
```

```shell
# scala
./bin/spark-submit \
--master yarn \
--deploy-mode cluster \
--conf "spark.sql.shuffle.partitions=20000" \
--jars "dependency1.jar,dependency2.jar"
--class com.sparkbyexamples.WordCountExample \
spark-by-examples.jar 

# pyspark
./bin/spark-submit \
   --master yarn \
   --deploy-mode cluster \
   wordByExample.py
```

```shell
spark-submit \
    /Users/luanmorenomaciel/GitHub/series-spark/src/first_app.py
```
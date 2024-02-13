# Azure HDInsight - Apache Spark

[user-assigned managed identity](https://docs.microsoft.com/en-us/azure/hdinsight/hdinsight-hadoop-use-data-lake-storage-gen2-portal)  
[storage optimization](https://docs.microsoft.com/en-us/azure/hdinsight/spark/optimize-data-storage)  
[processing optimization](https://docs.microsoft.com/en-us/azure/hdinsight/spark/optimize-data-processing)  
[submit spark job](https://docs.microsoft.com/en-us/azure/hdinsight/spark/spark-best-practices)

> * deployment option = arm templates & terraform
> * resource group = owshq_eastus2
> * name = owshq-apache-spark
> * region = eastus2
> * cluster type = spark
> * version = spark 3.0 [hdi 4.0]
> * login = luanmoreno
> * pwd = Qq11ww22!!@@
> * ssh user = sshuser
> * primary storage = adls2
> * storage account = owshqblobstg
> * filesystem = owshq-spark-storage
> * identity = uami-owshq-spark [storage blob data owner]
> * worker node = 8 cores with 64 gb of ram [2]
> * total cost per hour = [2.62 USD] 
> * time to provision = [~ 15 min]

### log & access hdinsight cluster
```sh
# ssh into driver node
sudo ssh sshuser@owshq-apache-spark-ssh.azurehdinsight.net

# list files inside of storage
# azure data lake gen 2 storage
# using abfs protocol
sudo hdfs dfs -ls /
sudo hdfs dfs -ls abfs://bs-stg-files@owshqblobstg.dfs.core.windows.net/

# 5.5 gb of users file
# 600 mb of business file
# 220 gb of reviews file
sudo hdfs dfs -ls abfs://bs-stg-files@owshqblobstg.dfs.core.windows.net/users
sudo hdfs dfs -ls abfs://bs-stg-files@owshqblobstg.dfs.core.windows.net/business
sudo hdfs dfs -ls abfs://bs-stg-files@owshqblobstg.dfs.core.windows.net/reviews

# point to spark app file [.py]
# execute spark-submit ~ /home/sshuser
export PYTHONIOENCODING=utf8
sudo $SPARK_HOME/bin/spark-submit --master yarn abfs://bs-stg-files@owshqblobstg.dfs.core.windows.net/app/cluster.py

# monitoring cluster with [ambari]
https://owshq-apache-spark.azurehdinsight.net

# [spark history server] for spark job monitoring
https://owshq-apache-spark.azurehdinsight.net/sparkhistory/

# zeppelin for [notebook] experience
https://owshq-apache-spark.azurehdinsight.net/zeppelin/
```

### total time spent
```sh
# time taken to process
39 minutes
```
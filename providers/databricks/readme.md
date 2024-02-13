# Azure Databricks - Apache Spark

[schedule spark jobs](https://docs.databricks.com/jobs.html)  

## configuring databricks cli for storage access

```sh
# install databricks-cli
pip install databricks-cli

# create secret
databricks configure --token

# configure url - blade url
# generate token from portal = dapi4ecab28a87b418f5134e21e614d438f4-2
https://adb-2090585310411504.4.azuredatabricks.net

# get clusters
# get ls
databricks clusters list

# create scope
# get key from blob storage
# key = lmKoi0C1eXYJ/10fOqh+4im0CT8wyw/MWbUqmNooiH6yH2mmNS1HtiZNMXDUvCEc0TRtC/3i2eat+AStq3oURg==
# :wq on vim
databricks secrets create-scope --scope az-blob-storage-owshqblobstg
databricks secrets list-scopes
databricks secrets put --scope az-blob-storage-owshqblobstg --key key-owshqblobstg
databricks secrets list --scope az-blob-storage-owshqblobstg

# list fs
databricks fs ls
databricks fs ls dbfs:/mnt
databricks fs ls dbfs:/mnt/bs-stg-files/reviews
```

## verify job execution

```sh
# job = dbr-job-batch-etl-yelp-dev
# action = run 
# successfully started run of job "dbr-job-batch-etl-yelp-py"

# completed runs ~ view details
# view spark ui ~ history server
```

## files to be processed

```sh
# files for processing
business = ~ 138mb (3)
user = ~ 2.32gb (2)
reviews = ~ 4.39 (22)
```

## schedule job for processing

```sh
> * deployment option = arm templates & terraform
> * option = create job
> * name = dbr-job-batch-etl-yelp-py
> * schedule type = manual
> * type = python
> * job location = [dbfs:/mnt/bs-stg-files/app/databricks/cluster.py]
> * configure new job cluster
> * cluster = 3 workers: standard_ds3_v2 ~ 8.2 (includes apache spark 3.1.1 & scala 2.12)
> * max concurrent runs = 1

```

## total time spent

```sh
# time taken to process
39m 16s
```
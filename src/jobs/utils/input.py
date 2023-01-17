def read_parquet_files(spark, filename):
    """
    load data from json file format.

    :param spark: spark session object.
    :param filename: location of the file.
    :return: spark dataFrame.
    """

    df = spark.read.parquet(filename)
    return df
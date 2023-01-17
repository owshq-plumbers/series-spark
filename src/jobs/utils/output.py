def write_into_parquet(df, mode, location):

    df.write.format("parquet").mode(mode).save(location)

    return None
import pandas

def summarise(csv):
    df = pandas.read_csv(csv, iterator=True, chunksize=2000)
    partial_desc = df.describe()

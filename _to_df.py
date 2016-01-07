import sys, os, time
import pandas as pandas

from helpers import get_file

def to_df(input_file_path, separator=";", index=False):
    input_file = get_file(input_file_path)
    s = time.time()

    df = pandas.read_csv(input_file, sep=separator, engine='c', decimal=',', encoding='utf-8')

    print (time.time() - s) / 60.0, "minutes to read."

    return df



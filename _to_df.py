import sys, os, time
import pandas as pd

file_path = os.path.dirname(os.path.realpath(__file__))
utils_path = os.path.abspath(os.path.join(file_path, ".."))
sys.path.insert(0, utils_path)
from helpers import get_file

def to_df(input_file_path, index=False):
    input_file = get_file(input_file_path)
    s = time.time()

    df = pd.read_csv(input_file, sep=";", engine='c', decimal=',')

    print (time.time() - s) / 60.0, "minutes to read."

    return df

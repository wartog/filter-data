import sys
from _to_df import to_df

if len(sys.argv) < 2:
    sys.exit("Usage: print.py csv_file.csv")

df = to_df(sys.argv[1])

print df.head()

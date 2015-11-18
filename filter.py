import sys
from _to_df import to_df

if len(sys.argv) < 2:
    sys.exit("Usage: filter.py csv_file.csv new_csv_file.csv")

df = to_df(sys.argv[1])
df = df[(df.Municipality_ID == 310620)]

df.to_csv(open('./fout.csv', 'wb+'), sep=";", index=True, float_format="%.2f")

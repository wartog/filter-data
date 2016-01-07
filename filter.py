import sys, os, click
from _to_df import to_df


'''
USAGE EXAMPLE:
python filter.py data/BH_2011.csv data/2011
'''

@click.command()
@click.argument('file_path', type=click.Path(exists=True), required=True)
@click.argument('output_path', type=click.Path(), required=True)
def main(file_path, output_path):

    # This should create the folder if it's not there yet
    if not os.path.exists(output_path): os.makedirs(output_path)

    # Reading the csv, getting a dataframe from pd.read_csv
    data_frame = to_df(sys.argv[1])

    # Filtering data, where Municipality_ID column = 310620
    data_frame = data_frame[(data_frame.Month == 1)]

    # Write output
    new_file_path = os.path.abspath(os.path.join(output_path, "fout.csv"))
    data_frame.to_csv(open(new_file_path, 'wb+'), sep=";", index=False, float_format="%.3f")

if __name__ == "__main__":
    main()



import sys, os, click, MySQLdb
from _to_df import to_df


'''
USAGE EXAMPLE:
python df_to_sql.py data/2015/fout.csv tabela_test
'''

@click.command()
@click.argument('file_path', type=click.Path(exists=True), required=True)
@click.argument('table', required=True)
def main(file_path, table):

    # This should create the folder if it's not there yet
    if not os.path.exists(file_path): os.makedirs(file_path)

    # Reading the csv, getting a dataframe from pd.read_csv
    data_frame = to_df(sys.argv[1])



    ''' Connect to DB '''
    connection = MySQLdb.connect(host=os.environ["DB_HOST"], user=os.environ["DB_USER"], passwd=os.environ["DB_PW"], db=os.environ["DB_NAME"])
    data_frame.to_sql(table, connection, flavor='mysql',  if_exists='replace', index=False, chunksize=650000)


if __name__ == "__main__":
    main()



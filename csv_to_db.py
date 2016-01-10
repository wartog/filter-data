import click
import os

'''
USAGE:
python csv_to_db.py -file_path=data/2015/fout.csv -table_name=tabela_test
'''

@click.command()
@click.option('-file_path', type=click.Path(exists=True), prompt=True, help='Csv input file.')
@click.option('-table_name', prompt=True, help='Name of table in database eg test.')
def main(file_path, table_name):
    print "importing", file_path, "into", table_name

    # Only possible with local-infile=1 in my.conf
    cmd = '''mysql --local-infile $DB_NAME -e "LOAD DATA LOCAL INFILE '%s' INTO TABLE %s FIELDS TERMINATED BY ';' LINES TERMINATED BY '\\n' IGNORE 1 LINES; "''' % (file_path, table_name)
    print cmd
    os.system(cmd)

if __name__ == '__main__':
    main()

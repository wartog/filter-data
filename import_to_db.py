# db_importer.py

import click
import os

'''
USAGE:
python import_to_db.py file_path=data/file.csv table_name=test
'''

@click.command()
@click.option('file_path', default='.', type=click.Path(exists=True), prompt=False, help='Csv input file.')
@click.option('table_name',prompt=True, help='Name of table in database eg test.')
def main(file_path, table_name):
    print "importing", f, "into", table_name
    header = handle.readline().strip()
    fields = header.split('\t')
    fields_null = ["{0} = nullif(@v{0},'')".format(fi) for fi in fields]
    # print "fields", fields

    fields = ["@v{}".format(x) for x in fields]

    fields = ",".join(fields)
    fields_null = ",".join(fields_null)

    cmd = '''mysql -u$DB_USER $DB_NAME -e "LOAD DATA LOCAL INFILE '%s' INTO TABLE %s FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n' IGNORE 1 LINES (%s) SET %s;" ''' % (f, table_name, fields, fields_null)
    print cmd
    os.system(cmd)

if __name__ == '__main__':
    main()

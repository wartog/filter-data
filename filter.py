import sys, os, click
from _to_df import to_df


@click.command()
@click.argument('file_path', type=click.Path(exists=True), required=True)
@click.argument('output_path', type=click.Path(), required=True)
def main(file_path, output_path):

    if not os.path.exists(output_path): os.makedirs(output_path)

    df = to_df(sys.argv[1])
    df = df[(df.Municipality_ID == 310620)]


    import pdb; pdb.set_trace()
    new_file_path = os.path.abspath(os.path.join(output_path, "fout.csv"))
    print new_file_path

    df.to_csv(open(new_file_path, 'wb+'), sep=";", index=True, float_format="%.3f")

if __name__ == "__main__":
    main()



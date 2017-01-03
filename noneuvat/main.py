import os
import argparse

from . report import NonEUVATReport


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-y', '--year', type=int, help='Four digit year', required=True)
    parser.add_argument(
        '-q', '--quarter', type=int, help='Quarter of year', required=True)
    parser.add_argument(
        '-o', '--output', type=str, help='Output directory', required=True)
    args = parser.parse_args()
    print('Saving to {}'.format(args.output))
    report = NonEUVATReport(args.year, args.quarter)
    non_EU_vat_table = report.report
    save_name = report.get_save_name() + '.ods'
    if args.output.strip() == '.':
        output_path = os.path.getcwd()
    else:
        output_path = args.output
    output_path = os.path.join(output_path, save_name)
    non_EU_vat_table.write_ods(output_path)

if __name__ == "__main__":
    main()

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
        '-o', '--output', type=str, help='Output directory',
        default=os.getcwd())
    args = parser.parse_args()
    report = NonEUVATReport(args.year, args.quarter)
    non_EU_vat_table = report.report
    save_name = report.get_save_name(extension='ods')
    if args.output.strip() == '.':
        output_path = os.getcwd()
    else:
        output_path = args.output
    report = NonEUVATReport(args.year, args.quarter)
    non_EU_vat_table = report.report
    save_name = report.get_save_name() + '.ods'
    output_path = os.path.join(output_path, save_name)
    print('Saving to {}'.format(output_path))
    non_EU_vat_table.write_ods(output_path)

if __name__ == "__main__":
    main()

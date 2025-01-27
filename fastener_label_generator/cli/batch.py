import csv
import os
import sys
from fastener_label_generator import FastenerLabelGenerator


def main():
    args = sys.argv[1:]
    if len(args) != 4:
        print("Usage: %s filename.pdf template_name style_name csv_file" % os.path.basename(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    # parse command line - ideally we should use click or a similar library
    filename, template_name, style_name, csv_path = args

    # load records from CSV
    records = []
    with open(csv_path, newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            records.append(row)

    # generate and write label file
    pdf_content = FastenerLabelGenerator.generate_pdf(template_name, style_name, records)
    open(filename, "wb").write(pdf_content)


if __name__ == "__main__":
    main()

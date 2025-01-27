import os
import sys
from fastener_label_generator import FastenerLabelGenerator


def main():
    args = sys.argv[1:]
    if len(args) < 3:
        print("Usage: %s filename.pdf template_name style_name field=value ..." % os.path.basename(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    # parse command line - ideally we should use click or a similar library
    filename, template_name, style_name, *field_args = args
    # pre-fill the field list - useful for testing
    fields = dict(size="M56x986",
                  screw_img="ISO7380_A.svg",
                  drive_img="H.svg",
                  drive_name_and_size="PH2",
                  id="202131231",
                  material="Stal nierdzewna A2",
                  coating="Czerniona",
                  strength_class="Klasa 12.8",
                  norms="ISO7810")
    # unpack fields from command line
    for field_arg in field_args:
        key, _, value = field_arg.partition("=")
        fields[key] = value

    # generate and write label file
    pdf_content = FastenerLabelGenerator.generate_pdf(template_name, style_name, [fields])
    open(filename, "wb").write(pdf_content)


if __name__ == "__main__":
    main()

from blabel import LabelWriter

label_writer = LabelWriter(
    "item_template.html", default_stylesheets=("style.css",)
)
records = [
    dict(thread="M3", length="30", screw_img="Fasteners_ISO7045.svg", bit_img="PH.png", bit_name = "PH2")
]

label_writer.write_labels(records, target="labels.pdf", base_url=".")

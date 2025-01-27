from blabel import LabelWriter

label_writer = LabelWriter(
    "item_template.html", default_stylesheets=("style.css",)
)
records = [
    dict(thread="M56", length="986", screw_img="ISO7380_A.svg", drive_img="H.svg", drive_name_and_size = "PH2", id="202131231", material="Stal nierdzewna A2", coating="Czerniona", strength_class="Klasa 12.8", norms="ISO7810")
]
label_writer.write_labels(records, target="labels.pdf", base_url=".")

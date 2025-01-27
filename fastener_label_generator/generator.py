import blabel
import importlib.resources
from importlib.abc import Traversable
import weasyprint


class FastenerLabelGenerator(object):

    assets: Traversable = importlib.resources.files("fastener_label_generator").joinpath("assets")

    @classmethod
    def generate_pdf(cls, template_name: str, stylesheet_name: str, fields: dict) -> bytes:

        # load template + style from disk
        template = cls.assets.joinpath("templates").joinpath(template_name + ".html").read_text()
        stylesheet = cls.assets.joinpath("styles").joinpath(stylesheet_name + ".css").read_text()

        # construct a writer object
        label_writer = blabel.LabelWriter(
            item_template=template,
            default_stylesheets=(weasyprint.CSS(string=stylesheet),)
        )

        # FIXME: construct template data
        record = dict(thread="M56", length="986", screw_img="ISO7380_A.svg", drive_img="H.svg", drive_name_and_size = "PH2", id="202131231", material="Stal nierdzewna A2", coating="Czerniona", strength_class="Klasa 12.8", norms="ISO7810")
        record.update(fields)

        # generate label
        with importlib.resources.as_file(cls.assets) as assets:
            return label_writer.write_labels([record], base_url=str(assets))

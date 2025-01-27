import blabel
import importlib.resources
from importlib.abc import Traversable
import weasyprint


class FastenerLabelGenerator(object):

    assets: Traversable = importlib.resources.files("fastener_label_generator").joinpath("assets")

    @classmethod
    def generate_pdf(cls, template_name: str, stylesheet_name: str, records: list[dict]) -> bytes:

        # load template + style from disk
        template = cls.assets.joinpath("templates").joinpath(template_name + ".html").read_text()
        stylesheet = cls.assets.joinpath("styles").joinpath(stylesheet_name + ".css").read_text()

        # construct a writer object
        label_writer = blabel.LabelWriter(
            item_template=template,
            default_stylesheets=(weasyprint.CSS(string=stylesheet),)
        )

        # generate label
        with importlib.resources.as_file(cls.assets) as assets:
            return label_writer.write_labels(records, base_url=str(assets))

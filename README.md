# fastener_label_generator

Label generator for fasteners stored in the [Hackerspace Wrocław](https://www.hswro.org/) workshop.

Based on:

- [blabel](https://github.com/Edinburgh-Genome-Foundry/blabel) for image generation 
- [FreeCAD Fasteners Workbench](https://github.com/shaise/FreeCAD_FastenersWB/) for fasteners icons
- [Wikipedia](https://de.wikipedia.org/wiki/Liste_der_Schraubenkopfantriebe) for screwdriver bits icons 

## Installation

Install like any standard Python utility. `pipx` is recommended for automatic management of venvs:

```
apt install python3-pipx
pipx install https://github.com/HackerspaceWroclaw/fastener_label_generator
```

## Command line usage

```shell
# Usage: fastener-label-generator filename.pdf template_name style_name field=value ...

fastener-label-generator label.pdf screw hswro thread=M3 bit=PH2
```

## Library usage

```python
from fastener_label_generator import FastenerLabelGenerator

pdf_content = FastenerLabelGenerator.generate_pdf("screw", "hswro", {"thread": "M3"})
open("label.pdf", "wb").write(pdf_content)
```

## Development

Install the library in Editable mode:

```shell
git clone https://github.com/HackerspaceWroclaw/fastener_label_generator ~/fastener_label_generator
python -m venv ~/flg-env
source ~/flg-env/bin/activate
pip install -e ~/fastener_label_generator
```

and hack away.

# fastener_label_generator

Label generator for fasteners stored in the [Hackerspace Wrocław](https://www.hswro.org/) workshop.

Based on:

- [blabel](https://github.com/Edinburgh-Genome-Foundry/blabel) for image generation 
- [FreeCAD Fasteners Workbench](https://github.com/shaise/FreeCAD_FastenersWB/) for fasteners icons
- [Wikipedia](https://de.wikipedia.org/wiki/Liste_der_Schraubenkopfantriebe) for screwdriver bits icons 

## Installation

## Command line usage

Install like any standard Python utility. `pipx` is recommended for automatic management of venvs:

```shell
sudo apt install python3-pipx
pipx install https://github.com/HackerspaceWroclaw/fastener_label_generator

# Usage: fastener-label-generator filename.pdf template_name style_name field=value ...
fastener-label-generator label.pdf fastener-label-generator test.pdf martyna martyna description="Śruba z łbem sześciokątnym" thread="M3" length="12" standard="DIN 933" material="ocynk" bolt_image="din933.png"
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

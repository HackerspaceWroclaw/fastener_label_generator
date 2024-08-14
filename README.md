# fastener_label_generator
Label generator for fasteners stored in Hackerspace Wrocław workshop
Based on:
- blabel for image generation - https://github.com/Edinburgh-Genome-Foundry/blabel
- FreeCAD Fasteners Workbench for fasteners icons - https://github.com/shaise/FreeCAD_FastenersWB/
- Wikipedia for screwdriver bits icons - https://de.wikipedia.org/wiki/Liste_der_Schraubenkopfantriebe 

## Installation

You need to install python3 and blabel library via PIP

For Ubuntu/Debian:
```
sudo apt install python3
pip3 install blabel
```

## Usage

Edit records to your needs e.g.:
```
dict(thread="M3", length="30", screw_img="Fasteners_ISO7045.svg", bit_img="PH.png", bit_name = "PH2")
```

Run with python3:
```
python3 fastener_label_generator.py
```

Labels will be generated to `labels.pdf` file.

# introducing: pix

## Overview

`pix` is a Python script that allows you to convert any image into pixel art. It offers the flexibility to use predefined color palettes or create your own for the output image.

## Features

- **Image to Pixel Art Conversion**: Convert any image into a pixel art version.
- **Customizable Palettes**: Use predefined color palettes or create your own.

## Installation

To install `pix`, you can clone the repository and install the required packages.

```bash
git clone https://github.com/FIEF-nohell/pix.git
cd pix
pip install -r requirements.txt
```

## Usage

To convert an image into pixel art, run the following command:

```bash
python pix.py input.jpg 5 dawn
```

Select an input image that is located in the root directory of the repository. The number following the image name specifies the pixel density of the output image, effectively serving as its resolution. A value of 1 indicates high pixel density, while a value of 20 suggests lower density.

Caution: Lower pixel density values result in longer rendering times. You may need to experiment with this setting to achieve the desired output.

The final argument is the color palette. You can browse available options in the palettes folder.



## Palettes

### Predefined Palettes By Me

- **Dawn**: A palette that looks very monochromatic.
- **Full**: A color palette with 270 colors.
  
### Lospec Palettes

All other palettes are sourced from [Lospec](https://lospec.com). You can download more palettes from their website. Simply select one and download the HEX file, then place it in the palettes folder


## Acknowledgments

Special thanks to [Lospec](https://lospec.com) for providing a wide range of color palettes.

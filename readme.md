# Introducing: pix!

## Overview

`pix` is a Python/HTML tool that allows you to convert any image into pixel art. It offers the flexibility to use predefined color palettes or create your own for the output image.

## Features

- **Image to Pixel Art Conversion**: Convert any image into a pixel art version.
- **Customizable Palettes**: Use predefined color palettes or create your own.

## Installation

To install `pix`, you can clone the repository and install the required packages.

```bash
git clone https://github.com/FIEF-nohell/pix.git
cd pix/API
pip install -r requirements.txt
```

## Starting

It is very simple to run this tool. First open the `startAPI.bat` and after that is running open `startGUI.bat`. 
When both are running the webserver should be open at `localhost:6969/index.html` 

[![grafik.png](https://i.postimg.cc/GpzMMDGX/grafik.png)](https://postimg.cc/VSrBvd7t)


## Usage

Select any input image that you want to modify. The number resolution of the output image defines it pixel density. A value of 1 indicates high pixel density, while a value of 20 suggests lower density.

Caution: Lower pixel density values result in longer rendering times. You may need to experiment with this setting to achieve the desired output.

The final argument is the color palette. You can browse available options or add your own in the `API/palettes` folder.


## Examples

Original image left, dawn palette in the middle and nyx on the right.

### Resolution 4
[![grafik.png](https://i.postimg.cc/qRPzNyT1/grafik.png)](https://postimg.cc/WF72KDtZ)

### Resolution 8
[![grafik.png](https://i.postimg.cc/bvbvKdbb/grafik.png)](https://postimg.cc/wtqHNqwT)

### Resolution 12
[![grafik.png](https://i.postimg.cc/5yjWWkGG/grafik.png)](https://postimg.cc/kRrpxw7F)

### Resolution 18
[![grafik.png](https://i.postimg.cc/fTmDz1kn/grafik.png)](https://postimg.cc/4mfrwLzB)

## Palettes

### Predefined Palettes By Me

- **Dawn**: A palette that looks very monochromatic.
- **Full**: A color palette with 270 colors.
  
### Lospec Palettes

All other palettes are sourced from [Lospec](https://lospec.com). You can download more palettes from their website. Simply select one and download the HEX file, then place it in the palettes folder


## Acknowledgments

Special thanks to [Lospec](https://lospec.com) for providing a wide range of color palettes.

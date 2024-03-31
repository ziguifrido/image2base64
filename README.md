![GitHub](https://img.shields.io/github/license/ziguifrido/image2base64)
![GitHub top language](https://img.shields.io/github/languages/top/ziguifrido/image2base64)
![GitHub last commit](https://img.shields.io/github/last-commit/ziguifrido/image2base64)

# Image2Base64

#### A simple converter between Images and Base64, written in Python.

Convert images to base64 and base64 to images.

## Prerequisites

- [Python 3.x](https://www.python.org/) installed.

## Usage

### Image &rarr; Base64

#### Parameters

- **--input**: Image path;
- **--output**: Base64 path;
- **--output-type**: Output type (1- clipboard, 2- file);

```
$ python image2base64.py --input image.png --output base64.txt --output_type 2
```

### Base64 &rarr; Image

#### Parameters

- **--input**: Base64 path;
- **--output**: Image path;

```
$ python base64_to_image.py --input base64.txt --output image.png
```

## Licence

This projet uses the [MIT license](LICENSE.md).

## Author

Marcos Oliveira

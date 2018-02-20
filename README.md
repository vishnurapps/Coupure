# Coupure
A cross platform snipping tool

Steps to follow in Arch Linux
## Install tesseract
```
sudo pacman -S tesseract
```
## Install tesseract-data-eng
```
sudo pacman -S tesseract-data-eng
```
## Testing tesseract
```
[vishnu@stampede Desktop]$ tesseract -v
tesseract 3.05.01
 leptonica-1.74.4
  libgif 5.1.4 : libjpeg 8d (libjpeg-turbo 1.5.1) : libpng 1.6.34 : libtiff 4.0.8 : zlib 1.2.11 : libwebp 0.6.0

[vishnu@stampede Desktop]$ tesseract example_01.png stdout
Warning. Invalid resolution 0 dpi. Using 70 instead.
Testing Tesseract OCR
```
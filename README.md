pyVhdl2Sch
==========
pyVhdl2Sch is a documentation generator tool. It takes VHDL files (.vhd) as entry and generates a pdf/svg/ps/png schematic for each input file.

pyVhdl2Sch is based on Python and is a rewrite of the QT/Latex based Vhdl2Sch.

How to use
======
type:

    ./pyV2S.py myVhdlfile.vhd

pyVhdl2Sch parses your file, find the entity and creates the corespondant schematic with Cairo.

The result is a pdf with a very narrow bounding box so you can import it in a latex document (for example) easily.

Full usage
==========

  * -v : verbose mode

  * -fgcolor : define contour color (based on https://github.com/vaab/colour)
    * example -fgred or -fg#caf or -fg#cafe42
  
  * -bgcolor : replace the transparent background by a colored one
  * -ftformat : specify the output format
    * -ftpdf --> pdf
    * -ftpng --> png
    * -ftsvg --> psvg
    * -ftps  --> ps
  * -winteger : specify the width of png file
    * -w1000 --> width of png = 1000px
  

Supported OS
============
- Linux
- Windows seven
- MacOs

Requirements
============
- python
- jura font installed (or change font in pdfdrawer.py)
- cairocffi
- coulour


Install
===========
Debian like
-----------
    git clone git@github.com:LaurentCabaret/pyVhdl2Sch.git

in order to install all the dependencies

	sudo sh reqs/linux.sh
	sudo sh reqs/update_pip_packages

Windows
-------
 * install win32 python (2.7.X)
 * install gtk and add it to your path http://www.gtk.org/download/win32.php
 * install cffi dll by downloading and executing cffi‑0.8.6.win32‑py2.7.exe on http://www.lfd.uci.edu/~gohlke/pythonlibs/#cffi
 * install pip if needed
 * in PowerShell (or cmd) 
     python -m pip install pylint pep8>=1.3.3 pytest-pep8 cairocffi colour
 
OSX
---
 * Install XQuartz from https://xquartz.macosforge.org/landing/
 * `brew install cairo`
 * `brew install pkg-config libffi`
 * `export PKG_CONFIG_PATH=/usr/local/Cellar/libffi/3.0.13/lib/pkgconfig/`
 * `pip install -r reqs/requirements.txt`
 * `python pyVhdl.py yourfile.vhd`
 
How to help
===========

What could be very cool to implement (help required)
------------------------------------
  * Auto finding of component usage and global schematic (with sub files) generation
  * Multiple schematic theme (using keywords to select look and feel)
  * 'png' production for 'word document' including 
  * A clean way to install it (a package ?)

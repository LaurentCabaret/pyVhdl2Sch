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
  

Supported OS
============
- Linux
- Not yet tested on windows
- Not yet tested on MacOs

Requirements
============
- python
- jura font installed (or change font in pdfdrawer.py)
- cairocffi
- coulour


Install
-------
    git clone git@github.com:LaurentCabaret/pyVhdl2Sch.git

in order to install all the dependencies

	sh linux.sh
	sh reqs/update_pip_packages

How to help
===========

What could be very cool to implement (help required)
------------------------------------
  * Auto finding of component usage and global schematic (with sub files) generation
  * Multiple schematic theme (using keywords to select look and feel)
  * 'png' production for 'word document' including 
  * A clean way to install it (a package ?)

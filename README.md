pyVhdl2Sch
==========
pyVhdl2Sch is a documentation generator tool. It takes VHDL files (.vhd) as entry and generates a pdf schematic for each input file.

pyVhdl2Sch is based on Python and is a rewrite of the QT/Latex based Vhdl2Sch.

How to use
======
type:
  ./pyV2S.py myVhdlfile.vhd

pyVhdl2Sch parses your file, find the entity and creates the corespondant schematic with Cairo.

The result is a pdf with a very narrow bounding box so you can import it in a latex document easily.

Supported OS
============
- Linux
- Not yet tested on windows
- Not yet tested on MacOs

Requirements
============
- python
- jura font installed 

Install
-------
  git clone ...

How to help
===========

What could be very cool to implement (help required)
------------------------------------
  * Auto finding of component usage and global schematic (with sub files) generation
  * Multiple schematic theme (using keywords to select look and feel)
  * 'png' production for 'word document' including 
  * A clean way to install it (a package ?)

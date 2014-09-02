---
layout: page
title: About
permalink: /about/
---

pyVhdl2Sch is a Python-based documentation generator tool. It takes VHDL files (.vhd) as entry and generates a pdf/svg/ps/png schematic for each input file.

{% highlight vhdl %}
Entity InputGate is
  Port ( Clk            : in  STD_LOGIC;
         PxClk          : in  STD_LOGIC;
         PxVal          : in  STD_LOGIC;
         a: in std_logic_vector (5 downto 0);
         b : in std_logic_vector(5 downto 0);
         c: in std_logic_vector(5 downto 0);
         d : in std_logic_vector (5 downto 0);
         PxValOut       : out  STD_LOGIC;
         Lig        : out  std_logic_vector (wSize-1 downto 0);
         Lig32         : out  std_logic_vector (wSize-1 downto 3);
         Col            : out  std_logic_vector (1 to 8);
         StatusInner    : out  std_logic;
         daInOut!@g  : inout   std_logic_vector (134 downto 7);
         FirstPass  : out   std_logic := '0');
end InputGate;
{% endhighlight %}
![output]({{ site.url }}/images/InputGate.png)

How to use
==========

{% highlight bash %}
./pyV2S.py -v -ftpng -w1000 -fgblack
{% endhighlight %}

pyVhdl2Sch parses your file, your options, find the entity and creates the corespondant schematic with Cairo.

The result is a pdf or (png, svg, ps) with a very narrow bounding box so you can import it in a latex document (for example) easily.

Full usage
==========
  * -v : verbose mode
  * -fgcolor : define contour color (based on https://github.com/vaab/colour)
		example -fgred or -fg#caf or -fg#cafe42
  * -bgcolor : replace the transparent background by a colored one
  * -ftformat : specify the output format
    * -ftpdf --> pdf
    * -ftpng --> png
    * -ftsvg --> psvg
    * -ftps --> ps
  * -winteger : specify the width of png file
  * -w1000 --> width of png = 1000px

More
====

Check out the [pyVhdl2Sch docs][pyVhdl2Sch] for more info on how to get the most out of Jekyll. File all bugs/feature requests at [pyVhdl2Sch's GitHub repo][pyVhdl2Sch-gh].

[pyVhdl2Sch-gh]: https://github.com/LaurentCabaret/pyVhdl2Sch
[pyVhdl2Sch]:    https://github.com/LaurentCabaret/pyVhdl2Sch/blob/master/README.md
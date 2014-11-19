library ieee;
use ieee.std_logic_1164.all;

package a_pkg is

function x_res (to_resolve: std_logic_vector) return std_ulogic;

end a_pkg;

package body a_pkg is

function x_res (to_resolve: std_logic_vector) return std_ulogic is
variable r: std_ulogic;
begin
r := 'Z';
for i in to_resolve'range loop
r := r or to_resolve(i);
end loop;
return r;
end function x_res;

end a_pkg;

library ieee;
use ieee.std_logic_1164.all;
use work.a_pkg.all;

entity foo is
port (
signal a_signal: in std_logic;
signal b: in std_logic;
signal c: in std_logic;
signal p: out x_res std_logic
);
end foo;

architecture fum of foo is

begin
p <= a;
p <= b;
p <= c;
end architecture;
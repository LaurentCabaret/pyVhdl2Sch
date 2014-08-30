-- Module Name:    InputGate - Behavioral 
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
USE ieee.std_logic_unsigned.ALL;


Entity test5 is pOrt (
    a : in std_logic_vector(0 to 7);
    d : out std_logic_vector(0 to Wsize-1);
    e : out std_logic_Vector(0 to aAbB - 1);
    f : in unsigned(0 to aAbB - 1);
    g : in unsignEd (0 to aAbB - 1);
    h : in Unsigned ( 0 to aAbB - 1 );
    b : in Std_logic_Vector(0 to 3);
    c : out std_Logic  );
end test;

architecture Behavioral of test is
  
  
begin
  c <= a and b;    
end Behavioral;


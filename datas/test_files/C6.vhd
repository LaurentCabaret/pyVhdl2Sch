-- Module Name:    InputGate - Behavioral 
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
USE ieee.std_logic_unsigned.ALL;


entity
test6
  is 
    port  --port
    ( --(
a
: --;;;
in 
std_logic_vector
(   
width
-
1
downto
0
  );
    b : in std_logic;
    c : out std_logic
  )

  ;
end
test6;

architecture Behavioral of test is
  
  
begin
  c <= a and b;    
end Behavioral;


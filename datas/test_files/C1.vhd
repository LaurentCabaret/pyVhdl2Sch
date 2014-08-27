-- Module Name:    InputGate - Behavioral 
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
USE ieee.std_logic_unsigned.ALL;


entIty Component_one is
  Port ( Clk            : in  STD_LOGIC;
         A : in STD_LOGIC;
         B : in STD_LOGIC;
         S : out STD_LOGIC
         );
end Component_one;

architecture Behavioral of Component_one is
  
  
begin
  S <= A and B;    
end Behavioral;


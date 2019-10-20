-- Module Name:    InputGate - Behavioral 
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
USE ieee.std_logic_unsigned.ALL;


entity test2 is port 
  (
    a : in std_logic;
    b : in std_logic;
    c : out std_logic
  );
end entity;

architecture Behavioral of test is
  
  
begin
  c <= a and b;    
end Behavioral;


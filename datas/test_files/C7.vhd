library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity ShiftRegister is
    Port ( CLK : in STD_LOGIC;
        Output : out STD_LOGIC_VECTOR); -- missing `(7 downto 0)` here
end entity;

architecture Behavioral of ShiftRegister is

signal Q : STD_LOGIC_VECTOR (7 downto 0) := "10011000";

begin

Output <= Q;

    process (CLK)
    begin
        if (CLK'event and CLK = '1') then
            Q(7 downto 0) <= Q(6 downto 0) & Q(7);
        end if;
    end process;

end Behavioral;
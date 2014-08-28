-- Module Name:    InputGate - Behavioral 
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
USE ieee.std_logic_unsigned.ALL;


entIty InputGate is
  Generic (
    wSize     :integer  := 9;
    hSize     :integer  := 9;
    imgWidth  : integer := 512;         -- Largeur de l'image
    imgHeight : integer := 512);        -- Hauteur de l'image    
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

architecture Behavioral of InputGate is
  CONSTANT LargeurBits : integer :=wSize;
  CONSTANT HauteurBits : integer :=hSize;
  COMPONENT AccessManager IS

    generic (
      hBusSize : integer range 0 to 11;
      vBusSize : integer range 0 to 11;
      imgWidth : integer range 0 to 1920;
      imgHeight : integer range 0 to 1080
      );

    port (        
      C_Add             : in    std_logic_vector (hBusSize-1 downto 0);
      L_Add             : in    std_logic_vector (vBusSize-1 downto 0);
      StatusInner       : out   std_logic;
      UpLeftCorner      : out   std_logic;   
      FirstLine         : out   std_logic;
      FirstRow         : out   std_logic;
      LastRow          : out   std_logic;
      LastPixel        : out   std_logic
      );

  END COMPONENT;

  signal CleanPxClk : std_logic :='0';
  SIGNAL C_Add :  std_logic_vector (LargeurBits-1 downto 0) := (others=>'0');
  SIGNAL L_Add :  std_logic_vector (HauteurBits-1 downto 0) := (others=>'0');
  SIGNAL SigLastRow :  std_logic := '0';
  SIGNAL SigLastPixel :  std_logic := '0';
  SIGNAL fPass :  std_logic := '1';
  
  
begin
  AM1: AccessManager GENERIC MAP(
    hBusSize => LargeurBits,
    vBusSize => HauteurBits,
    imgWidth => imgWidth,
    imgHeight => imgHeight
    )
    PORT MAP(
      C_Add         => C_Add,
      L_Add         => L_Add,
      StatusInner     => StatusInner,
      UpLeftCorner    => UpLeftCorner,
      FirstLine       => FirstLine,           
      FirstRow      => FirstRow,
      LastRow         => SigLastRow ,
      LastPixel     => SigLastPixel
      );


  PxClkEventManager: process(Clk)
    variable flag : std_logic := '1';
  begin 
    if Clk'Event and Clk='1' then 
      if (PxClk = '1' and flag = '0') then CleanPxClk <='1';
                                           flag:='1';
      elsif PxClk = '0' then flag:='0'; 
                             CleanPxClk <='0';
      elsif PxClk = '1' and flag = '1' then CleanPxClk <='0';
                                            flag:='1';
      end if;
    end if;
  end process;

  FirstPass <= fPass;
  PixelCounter: process(Clk)
   variable flag : std_logic := '1';
  variable flagPass : std_logic := '0';
   begin
    if Clk'Event and Clk='1' then 
      if CleanPxClk = '1' then 
        if SigLastRow='1' then C_Add <= (others=>'0');
                               if SigLastPixel ='1' then L_Add <=  (others=>'0');
                                      if flagPass = '0' then fPass <= '0';
                                                      flagPass := '1';
                                      else fPass <= '1';
                                          flagPass := '0';
                                      end if;
                               else L_Add <= L_Add + 1;
                               end if;
        else C_Add <= C_Add + 1;                        
        end if;
      end if;
    end if;
  end process;

  Col <= C_Add;
  Lig <= L_Add;
  LastRow <= SigLastRow;
  LastPixel <= SigLastPixel;

  PxValOut <= PxVal; 
end Behavioral;


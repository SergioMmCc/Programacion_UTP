-- Code your design here
library IEEE;
use IEEE.std_logic_1164.all;

entity xorsop is
  port ( A : in std_logic;
         B : in std_logic;
         S : out std_logic
       );
end entity;

Architecture arq_xorsop of xorsop is
--declaro componentes y/o señales
  Begin
  S <= ((not A) and B) or (A and (not B));

end architecture;

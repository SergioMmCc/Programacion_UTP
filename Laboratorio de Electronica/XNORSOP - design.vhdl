-- Code your design here
library IEEE;
use IEEE.std_logic_1164.all;

entity xnorsop is
  port ( A : in std_logic;
         B : in std_logic;
         S : out std_logic
       );
end entity;

Architecture arq_xnorsop of xnorsop is
  Begin
  S <= (A and B) or ((not A) and (not B));

end architecture;

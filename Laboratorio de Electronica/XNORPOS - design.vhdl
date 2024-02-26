-- Code your design here
library IEEE;
use IEEE.std_logic_1164.all;

entity xnorpos is
  port ( A : in std_logic;
         B : in std_logic;
         S : out std_logic
       );
end entity;

Architecture arq_xnorpos of xnorpos is
  Begin
S <= (A or (not B)) and ((not A) or B);

end architecture;

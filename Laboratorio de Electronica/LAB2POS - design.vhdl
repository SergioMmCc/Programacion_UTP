-- Code your design here
library IEEE;
use IEEE.std_logic_1164.all;

entity lab2pos is
  port ( A : in std_logic;
         B : in std_logic;
         C : in std_logic;
         Cout : out std_logic;
         S : out std_logic
       );
end entity;

Architecture arq_lab2pos of lab2pos is
  Begin
  Cout <= (A or B or C) and (A or B or (not C)) and (A or (not B) or C) and ((not A) or B or C); 
  S <= (A or B or C) and (A or (not B) or (not C)) and ((not A) or (not B) or C);

end architecture;

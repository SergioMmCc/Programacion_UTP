-- Code your design here
library IEEE;
use IEEE.std_logic_1164.all;

entity lab2sop is
  port ( A : in std_logic;
         B : in std_logic;
         C : in std_logic;
         Cout : out std_logic;
         S : out std_logic
       );
end entity;

Architecture arq_lab2sop of lab2sop is
  Begin
  Cout <= ((not A) and B and C) or (A and (not B) and C) or (A and B and (not C)) or (A and B and C); 
  S <= ((not A) and (not B) and C) or ((not A) and B and (not C)) or (A and (not B) and (not C)) or (A and (not B) and C) or (A and B and C);

end architecture;

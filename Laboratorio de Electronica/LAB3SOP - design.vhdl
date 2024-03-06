-- Code your design here
library IEEE;
use IEEE.std_logic_1164.all;

entity lab3sop is
  port ( A : in std_logic;
         B : in std_logic;
         C : in std_logic;
         D : in std_logic;
         S : out std_logic
       );
end entity;

Architecture arq_lab3sop of lab3sop is
  Begin
  
  signal S1, S2, S3, S4, S5, S65, S7, S8 : std_logic;
  
  S1 <= (not A) and B and C and D;
  S2 <= A and (not B) and (not C) and D;
  S3 <= A and (not B) and C and (not D);
  S4 <= A and (not B) and C and D;
  S5 <= A and B and (not C) and (not D);
  S6 <= A and B and (not C) and D;
  S7 <= A and B and C and (not D);
  S8 <= A and B and C and D; 
  
  S <= S1 or S2 or S3 or S4 or S5 or S6 or S7 or S8;

end architecture;

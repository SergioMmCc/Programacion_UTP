-- Code your design here
library IEEE;
use IEEE.std_logic_1164.all;

entity lab3pos is
  port ( A : in std_logic;
         B : in std_logic;
         C : in std_logic;
         D : in std_logic;
         S : out std_logic
       );
end entity;

Architecture arq_lab3pos of lab3pos is
  signal S1, S2, S3, S4, S5, S6, S7, S8 : std_logic;
  Begin
  
  S1 <= A or B or C or D;
  S2 <= A or B or C or (not D);
  S3 <= A or B or (not C) or D;
  S4 <= A or B or (not C) or (not D);
  S5 <= A or (not B) or C or D;
  S6 <= A or (not B) or C or (not D);
  S7 <= A or (not B) or (not C) or D;
  S8 <= (not A) or B or C or D; 
  
  S <= S1 and S2 and S3 and S4 and S5 and S6 and S7 and S8;

end architecture;

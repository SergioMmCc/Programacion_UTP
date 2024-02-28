-- Code your testbench here
library IEEE;
use IEEE.std_logic_1164.all;

entity TB_LAB2SOP is

end entity;

architecture arq_TB_LAB2SOP of TB_LAB2SOP is
  component lab2sop
    port ( A : in std_logic;
           B : in std_logic;
           C : in std_logic;
           Cout : out std_logic;
           S : out std_logic
          );
  end component;

  signal X, Y, Z : std_logic;

  Begin

  UUT : lab2sop
  port map ( A => X,
             B => Y,
             C => Z
            );

  Process
    begin
      X <= '0';
      Y <= '0';
      Z <= '0';
      wait for 10 ns;

      X <= '0';
      Y <= '0';
      Z <= '1';
      wait for 10 ns;

      X <= '0';
      Y <= '1';
      Z <= '0';
      wait for 10 ns;

      X <= '0';
      Y <= '1';
      Z <= '1';
      wait for 10 ns;
      
      X <= '1';
      Y <= '0';
      Z <= '0';
      wait for 10 ns;
      
      X <= '1';
      Y <= '0';
      Z <= '1';
      wait for 10 ns;
      
      X <= '1';
      Y <= '1';
      Z <= '0';
      wait for 10 ns;
      
      X <= '1';
      Y <= '1';
      Z <= '1';
      wait for 10 ns;

  end process;
end architecture;

-- Code your testbench here
library IEEE;
use IEEE.std_logic_1164.all;

entity TB_LAB3SOP is

end entity;

architecture arq_TB_LAB3SOP of TB_LAB3SOP is
  component lab3sop
    port ( A : in std_logic;
           B : in std_logic;
           C : in std_logic;
           D : in std_logic;
           S : out std_logic
          );
  end component;

  signal W, X, Y, Z : std_logic;

  Begin

  UUT : lab3sop
  port map ( A => W,
             B => X,
             C => Y,
             D => Z
            );

  Process
    begin
      W <= '0';
      X <= '0';
      Y <= '0';
      Z <= '0';
      wait for 10 ns;
	  
      W <= '0';
      X <= '0';
      Y <= '0';
      Z <= '1';
      wait for 10 ns;

      W <= '0';
      X <= '0';
      Y <= '1';
      Z <= '0';
      wait for 10 ns;

      W <= '0';
      X <= '0';
      Y <= '1';
      Z <= '1';
      wait for 10 ns;
      
      W <= '0';
      X <= '1';
      Y <= '0';
      Z <= '0';
      wait for 10 ns;
      
      W <= '0';
      X <= '1';
      Y <= '0';
      Z <= '1';
      wait for 10 ns;
      
      W <= '0';
      X <= '1';
      Y <= '1';
      Z <= '0';
      wait for 10 ns;
      
      W <= '0';
      X <= '1';
      Y <= '1';
      Z <= '1';
      wait for 10 ns;
      
      
      
      W <= '1';
      X <= '0';
      Y <= '0';
      Z <= '0';
      wait for 10 ns;

      W <= '1';
      X <= '0';
      Y <= '0';
      Z <= '1';
      wait for 10 ns;

      W <= '1';
      X <= '0';
      Y <= '1';
      Z <= '0';
      wait for 10 ns;

      W <= '1';
      X <= '0';
      Y <= '1';
      Z <= '1';
      wait for 10 ns;
      
      W <= '1';
      X <= '1';
      Y <= '0';
      Z <= '0';
      wait for 10 ns;
      
      W <= '1';
      X <= '1';
      Y <= '0';
      Z <= '1';
      wait for 10 ns;
      
      W <= '1';
      X <= '1';
      Y <= '1';
      Z <= '0';
      wait for 10 ns;
      
      W <= '1';
      X <= '1';
      Y <= '1';
      Z <= '1';
      wait for 10 ns;

  end process;
end architecture;

-- Code your testbench here
library IEEE;
use IEEE.std_logic_1164.all;

entity TB_XORSOP is
-- Aquí estarían los puertos
end entity;

architecture arq_TB_XORSOP of TB_XORSOP is
-- declaración de componentes y/o señales
  component xorsop
    port ( A : in std_logic;
           B : in std_logic;
           S : out std_logic
          );
  end component;

  signal X, Y : std_logic;

  Begin

  UUT : xorsop
  port map ( A => X,
             B => Y
            );

  Process
    begin
      X <= '0';
      Y <= '0';
      wait for 10 ns;

      X <= '0';
      Y <= '1';
      wait for 10 ns;

      X <= '1';
      Y <= '0';
      wait for 10 ns;

      X <= '1';
      Y <= '1';
      wait for 10 ns;

  end process;
end architecture;

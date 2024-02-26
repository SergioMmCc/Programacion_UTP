-- Code your testbench here
library IEEE;
use IEEE.std_logic_1164.all;

entity TB_XNORPOS is

end entity;

architecture arq_TB_XNORPOS of TB_XNORPOS is
  component xnorpos
    port ( A : in std_logic;
           B : in std_logic;
           S : out std_logic
          );
  end component;

  signal X, Y : std_logic;

  Begin

  UUT : xnorpos
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

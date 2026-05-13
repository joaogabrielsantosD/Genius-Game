-- WARNING: Do NOT edit the input and output ports in this file in a text
-- editor if you plan to continue editing the block that represents it in
-- the Block Editor! File corruption is VERY likely to occur.

-- Authors: João Donato, Matheus Sousa.

FUNCTION sevenseg (clock, value[4..0])
	RETURNS (seg[7..0], dig[3..0]);
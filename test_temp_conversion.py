from temp_conversion import fahr_to_celsius
from temp_conversion import fahr_to_kelvin

def test_fahr_cels_abs_zero_input():
	assert fahr_to_celsius(-460) == -273

def test_fahr_kelvin_abs_zero_input():
	assert fahr_to_kelvin(-460) == 0.0
	
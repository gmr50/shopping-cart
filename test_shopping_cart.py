from shopping_cart_revisited import to_usd, human_friendly_timestamp, find_product, calculate_total_price

def test_to_usd():

	test_passed = False
	input = 10000
	result = to_usd(input)

	if(result[0] == '$'):
		test_passed = True


	assert test_passed == True

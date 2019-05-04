from shopping_cart_revisited import to_usd, human_friendly_timestamp, find_product, calculate_total_price

def test_to_usd():

	test_passed = False
	input = 10000
	result = to_usd(input)



	if(result[0] == '$' and result[3] == ',' and result[-1] == '0' and result[-2] == '0'):
		test_passed = True


	assert test_passed == True

	#reset for next test
	#testing now with trailing decimals
	test_passed = False

	result = to_usd(10.99999999)

	if(result == "$11.00"):
		test_passed = True

	assert test_passed == True

	#reset for next test
	#testing with fewer decimals

	test_passed = False
	result = to_usd(1.1)
	if(result == "$1.10"):
		test_passed = True

	assert test_passed == True





def test_human_friendly_time():

	test_passed = False
	now = human_friendly_timestamp("now")
	today = human_friendly_timestamp("today")


	if(now[2] == ':' and today[2] == '/' and today[5] == '/'):
		test_passed = True

	assert test_passed == True



def test_find_product():
	products = [{"id":1, "name": "test1", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
	{"id":2, "name": "Test2", "department": "beverages", "aisle": "tea", "price": 2.49},
	{"id":3, "name": "Test 3", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},]


	result = find_product("test1", products)
	assert result["price"] == 3.50


	#tests case sensitivity
	result = find_product("TEST2", products)
	assert result["aisle"] == "tea"


	#tests number lookup
	result = find_product(3, products)
	assert result["name"] == "Test 3"

	#error handling is done outside of the find_product function


def test_calculate_total_price():
	prices_list = [10,11,12]

	results_list = calculate_total_price(prices_list)

	assert results_list[0] == "$33.00"
	assert results_list[1] == "$1.98"
	assert results_list[2] == "$34.98"










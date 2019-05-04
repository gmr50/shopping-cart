import datetime


def to_usd(input):


	result = "${0:.2f}".format(input)

	return result


def human_friendly_timestamp(time_type):

	if(time_type == "now"):
		now = datetime.datetime.now().time().strftime('%I:%M %p')
		return now

	elif(time_type == "today"):
		today = datetime.date.today().strftime('%m/%d/%y')
		return today
	else:
		return "Did not pass time_type string"


def find_product(input_select, products):


	#converts to int if applicable
	try:
		input_select = int(input_select)
	except ValueError:
		input_select = str(input_select)


	if(type(input_select)==int):


		matching_product = [pr for pr in products if pr["id"] == int(input_select)]
		#takes and selects the first line of the list given by the list comprehension
		#if theres a match, in this scenario, it will be the first


		#throws error if the product is not found, caught outside of this function
		selected_product = matching_product[0]
		return selected_product

	else:
		matching_product = [pr for pr in products if pr["name"].lower() == input_select.lower()]
		#takes and selects the first line of the list given by the list comprehension
		#if theres a match, in this scenario, it will be the first

		#throws an error if product is not found, caught outside the function
		selected_product = matching_product[0]
		return selected_product


def calculate_total_price(prices_list):

	total_price = 0.00
	calculations_list = []

	for x in prices_list:
		total_price = total_price + x 

	#times dc tax rate
	tax = total_price * .06
	final_price = tax + total_price
	tax = to_usd(tax)
	final_price = to_usd(final_price)
	subtotal = to_usd(total_price)

	calculations_list.append(subtotal)
	calculations_list.append(tax)
	calculations_list.append(final_price)

	return calculations_list








if __name__ == "__main__":
    print("main")

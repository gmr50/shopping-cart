#this is where the shopping_Cart code will go 

# shopping_cart.py

import datetime 

#look in course notes for how to use
#modules/datetime

products = [
	{"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
	{"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
	{"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
	{"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
	{"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
	{"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
	{"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
	{"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
	{"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
	{"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
	{"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
	{"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
	{"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
	{"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
	{"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
	{"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
	{"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
	{"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
	{"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
	{"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# TODO: write some Python code here to produce the desired functionality...


#print(products)


print("************".center(300))
print("***************************************************".center(300))
print("Hello!!! Welcome to Graham's groceries 'n goodies".center(300))
print("***************************************************".center(300))
print("************".center(300))

print("Here's our menu!")

print("------------------------------------------------------------------")

def name_sort(product_list):
	return product_list["name"]

sorted_products = sorted(products,key=name_sort)


for pr in sorted_products:
	price_product = "${0:.2f}".format(pr["price"])
	print("+ " + pr["name"] + " (" + str(price_product) + ") " + "[ID: " + str(pr["id"]) +  "]")

print("------------------------------------------------------------------")


loop_bool = True
item_count = 0 
prices_list = []
names_list = []

# an infinite loop! you can press control+c to cancel the program if/when it gets stuck...
while loop_bool == True:
	# capturing user input and storing in a variable
	user_input = input("Please input a product identifier, or 'DONE' if there are no more items: ")
	# demonstrating ability to recognize what the input was, although you might also want to check its datatype


	if user_input != ("DONE") and user_input != ("done"):
		
		try:

			print("YOUR INPUT WAS: " + str(user_input))


		

		#in order to reference a product by its id, need to do filtering 
		#or do a list comprehension *************

		#using list comprehension to look up item
			matching_product = [pr for pr in products if pr["id"] == int(user_input)]
		#this list comprehension returns a list, could be all the products or just one item

		#takes and selects the first line of the list given by the list comprehension
		#if theres a match, in this scenario, it will be the first

			if not matching_product:
				print("That's not on the menu! pick again!")
			else:
				selected_product = matching_product[0]



				product_price = 0
				product_price = selected_product["price"]
				product_name = selected_product["name"]
				prices_list.append(product_price)
				names_list.append(product_name) 



				#increments item count 
				item_count += 1

			print("***********")

		except ValueError:
			print("Invalid entry! Try again.")
	
	else:
		loop_bool = False
		if item_count == 0:

			print("You didn't buy anything! Thanks for coming though.")
		else: 

			########################
			# receipt printing
			print("generating receipt....")
			print("------------------------------------------------------------------")
			print("Graham's Groceries 'n Goodies".center(300))
			print("847-846-9452".center(300))
			print("Find us on the web at https://github.com/gmr50/shopping-cart !! ".center(300))
			print("------------------------------------------------------------------")
			#printing date and time w formatting
			today  = datetime.date.today().strftime('%m/%d/%y')
			now = datetime.datetime.now().time().strftime('%I:%M')
			print("Purchase Date: " + str(today))
			print("Purchase Time: " + str(now))

			print("------------------------------------------------------------------")

			total_price = 0.00
			
			for x, y in zip(prices_list, names_list):
				

				price_format = "${0:.2f}".format(x)
				print(" + " + str(y) + " , " + str(price_format))
				total_price = total_price + x 

			#times dc tax rate
			tax = total_price * .06
			final_price = tax + total_price
			total_price_format = "${0:.2f}".format(total_price)
			final_tax_format = "${0:.2f}".format(tax)
			final_price_format = "${0:.2f}".format(final_price)

			print("------------------------------------------------------------------")

			print("Subtotal: " + str(total_price_format))
			print("Tax: " + str(final_tax_format))
			print("Total Price: " + str(final_price_format))

			print("------------------------------------------------------------------")

			print("Thanks for shopping!")
			print("Come back and get some goodies from Graham soon")
			print("------------------------------------------------------------------")

			#printing receipt section
			receipt_input = input("Would you like a receipt? Press 'Y' or 'y' for yes, otherwise press any key: ")

			if(receipt_input == "Y" or receipt_input == "y"):
				print("You selected yes!")

				today2  = datetime.date.today().strftime('%y-%m-%d-')
				now2 = datetime.datetime.now().time().strftime('%H-%M-%s%f')

				file_name = "receipts/" + str(today2) + str(now2) + ".txt"
				print("The receipt file's name is: " + file_name)
				print("Please come again!!")

				with open(file_name, "w") as file:
					file.write("------------------------------------------------------------------")
					file.write("\n")
					file.write("Graham's Groceries 'n Goodies".center(300))
					file.write("\n")
					file.write("847-846-9452".center(300))
					file.write("\n")
					file.write("Find us on the web at https://github.com/gmr50/shopping-cart !! ".center(300))
					file.write("\n")
					file.write("------------------------------------------------------------------")
					file.write("\n")
					file.write("Purchase Date: " + str(today))
					file.write("\n")
					file.write("Purchase Time: " + str(now))
					file.write("\n")
					file.write("------------------------------------------------------------------")
					file.write("\n")
					for x, y in zip(prices_list, names_list):
						price_format = "${0:.2f}".format(x)
						file.write(" + " + str(y) + " , " + str(price_format))
						file.write("\n")

					file.write("------------------------------------------------------------------")
					file.write("\n")
					file.write("Subtotal: " + str(total_price_format))
					file.write("\n")
					file.write("Tax: " + str(final_tax_format))
					file.write("\n")
					file.write("Total Price: " + str(final_price_format))
					file.write("\n")
					file.write("------------------------------------------------------------------")
					file.write("\n")
					file.write("Thanks for shopping!")
					file.write("\n")
					file.write("Come back and get some goodies from Graham soon")
					file.write("\n")
					file.write("------------------------------------------------------------------")

			else:
				print("No receipt. See you soon!")




   # price = product["price"]
   # assuming there was a single dictionary item named product 


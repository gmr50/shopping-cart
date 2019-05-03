
# shopping_cart.py

import datetime 
import csv


from shopping_cart_revisited import to_usd


def name_sort(product_list):
	return product_list["name"]




csv_file_path = "products.csv"


#declare empty list
products = [] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

with open(csv_file_path, "r") as csv_file:
		reader = csv.DictReader(csv_file)
		for row in reader:
			d = {"id": int(row["id"]), "name": row["name"], "price": float(row["price"])}			
			products.append(d) 
			#print(type(d), d["name"], d["price"])





print("************")
print("***************************************************")
print("Hello!!! Welcome to Graham's groceries 'n goodies")
print("***************************************************")
print("************")

print("Here's our menu!")

print("------------------------------------------------------------------")



sorted_products = sorted(products,key=name_sort)


for pr in sorted_products:
	price_product = to_usd(pr["price"])
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
				

				price_format = to_usd(x)
				print(" + " + str(y) + " , " + str(price_format))
				total_price = total_price + x 

			#times dc tax rate
			tax = total_price * .06
			final_price = tax + total_price
			tax = to_usd(tax)
			final_price = to_usd(final_price)
			subtotal = to_usd(total_price)

			print("------------------------------------------------------------------")

			print("Subtotal: " + subtotal)
			print("Tax: " + tax)
			print("Total Price: " + final_price)

			print("------------------------------------------------------------------")

			print("Thanks for shopping!")
			print("Come back and get some goodies from Graham soon")
			print("------------------------------------------------------------------")
			###################################

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

						price_format = to_usd(x)
						file.write(" + " + str(y) + " , " + price_format)
						file.write("\n")

					file.write("------------------------------------------------------------------")
					file.write("\n")
					file.write("Subtotal: " + subtotal)
					file.write("\n")
					file.write("Tax: " + tax)
					file.write("\n")
					file.write("Total Price: " + final_price)
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


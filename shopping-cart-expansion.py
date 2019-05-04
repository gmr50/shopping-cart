
# shopping_cart.py

import datetime 
import csv


from shopping_cart_revisited import to_usd, human_friendly_timestamp, find_product, calculate_total_price


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



now = human_friendly_timestamp("now")
print("Now: " + now)
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


			selected_product = find_product(user_input,products)
		

			product_price = 0
			product_price = selected_product["price"]
			product_name = selected_product["name"]
			prices_list.append(product_price)
			names_list.append(product_name) 



			#increments item count 
			item_count += 1

			print("***********")

		except:
			#catches error from find_product function
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
			today  = human_friendly_timestamp("today")
			now = human_friendly_timestamp("now")
			print("Purchase Date: " + today)
			print("Purchase Time: " + now)

			print("------------------------------------------------------------------")


			
			for x, y in zip(prices_list, names_list):
				

				price_format = to_usd(x)
				print(" + " + str(y) + " , " + str(price_format))



			calculations_list = calculate_total_price(prices_list)

			print("------------------------------------------------------------------")

			print("Subtotal: " + str(calculations_list[0]))
			print("Tax: " + str(calculations_list[1]))
			print("Total Price: " + str(calculations_list[2]))

			print("------------------------------------------------------------------")

			print("Thanks for shopping!")
			print("Come back and get some goodies from Graham soon")
			print("------------------------------------------------------------------")
			###################################

			#printing receipt section
			receipt_input = input("Would you like a receipt? Press 'Y' or 'y' for yes, otherwise press any key: ")

			if(receipt_input == "Y" or receipt_input == "y"):
				print("You selected yes!")

				#this datetime invocation kept for receipt writing purposes
				today2  = datetime.date.today().strftime('%d-%m-%y-')
				now2 = human_friendly_timestamp("now")

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


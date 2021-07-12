item_add="yes"
while item_add =="yes" :
				item_name=str(input("Enter item name here : "))
				item_rate=float(input("Enter item rate here : "))
				item_essential=str(input("Is it essential product ? (yes/no) : "))
				item_imported=str(input("Is it imported product ? (yes/no)  : "))
				final_tax=0
				total=0
				if item_essential =="yes" and item_imported =="no":
					final_price=item_rate
					tax =0
					print("Final price :" + "{:.2f}".format(final_price))

				elif item_essential == "no"  and item_imported =="yes":
					import_tax=((item_rate/100)*5)
					basic_tax=((item_rate/100)*10)
					tax =import_tax+basic_tax
					final_price=item_rate+import_tax+basic_tax
					print("Final price :" + "{:.2f}".format(final_price))

				elif item_essential == "no"  and item_imported =="no":
					basic_tax=((item_rate/100)*10)
					final_price=item_rate+basic_tax
					tax =basic_tax
					print("Final price :" + "{:.2f}".format(final_price))

				elif item_essential == "yes"  and item_imported =="yes":
					import_tax=((item_rate/100)*5)
					final_price=item_rate+import_tax
					tax =import_tax
					print("Final price :" + "{:.2f}".format(final_price))
				final_tax=final_tax+tax
				total=total+final_price
				item_add=input("Do you want to add new item ? (yes/no) : ")
		
print 	("Tax	: " + "{:.2f}".format(final_tax))
print	("Total	: " + "{:.2f}".format(total))
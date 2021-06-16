# Exercise 1
# ------------
# Takes Input
# Stores input into a list
# user can add or delete items
# user can see current shopping list
# loops until user 'quits'
# after quitting bring out all items in cart
def shopping_cart():
	print("""
	
	____________________\n
	WELCOME TO THE SHOP!
	____________________\n""")
	
	cart = []
	sum_ = 0
	checkout = {}
	stocklist = { # Dictionary of available items
		1:{
			"name": "graphic t-shirt",
			"qty": 5,
			"price": "1"
		},
		2:{
			"name": "jeans",
			"qty": 5,
			"price": "1"
		},
		3:{
			"name": "hat",
			"qty": 5,
			"price": "1"
		},
		4:{
			"name": "blazer",
			"qty": 5,
			"price": "1"
		},
		5:{
			"name": "boots",
			"qty": 5,
			"price": "1"
		},
		6:{
			"name": "shoes",
			"qty": 5,
			"price": "1"
		},
	}
  # Initial instructions for the user
	instructions = print("""
	Type 'shop' to see the options.
	Type 'view' to see your cart.
	Type 'del' to remove the last item you added fromm the cart.
	Type 'checkout' to purchase your items.""")
	active = True
	while active: # Starts shopping loop
		choice = input("\nWhat would you like to do? 'shop', 'view', 'del', 'checkout': ") # Takes input for options
		
		if choice == 'shop': # Shows user availible items
			for i in stocklist.values():
				print(i['name'])
			add = input("\ntype the name of the item to add it: ") # Allows user to add item to cart
			for i in stocklist.values():
				if add == i["name"]:
					cart.append(i["name"])
					print("\n-- * You added " + i["name"] + " * --\n")
					
			
		elif choice == 'view': # User can view cart
			print("\nItem(s) in cart -- "+str(cart)+" --")
		elif choice == 'del': # User can del most recent addition to the cart
			cart.pop()
		else: # User can checkout and end loop/ program
			if choice == 'checkout':
				active = False
				print("\n-- Thanks for shopping with us! --")
				print("Item(s) you purchased --"+str(cart)+"--\n")

shopping_cart()
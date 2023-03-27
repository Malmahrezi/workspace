    CS50 Web Programming with Python and JavaScript 
    
    
    This is a Django App for ordering from Chipotle Mexican Grill online 


	This project contains to main folders:
		○ burrito:
			§ setting.py: contains Django setting for burrito project.
			§ urls.py: contains burrito configuration urls.
			§ wsgi.py: WSGI config for burrito project.
		○ orders:
			§ static
				□ orders
					® main.js : contains all codes responsible for disabling all check boxes for toppings, also when burrito order is clicked, counting checkboxes, checking number of toppings 
					® style.css : a CSS file that contains all style functions and colors and the design of my project.
			§ templates
				□ orders
					® base.html: the layout of the main page.
					® confirm.html : after choosing from the menu, this page pop up to confirm the order.
					® index.html : this html file contains the shopping cart page.
					® login.html : the login page that asks the user to provide their username and passwords.
					® register.html : the page that provide a form to be filled in order to create an account for the new users.
					® staff.html
			§ admin.py
			§ apps.py
			§ models.py : this python file that contains all the models for the orders.
			§ tests.py
			§ urls.py : this file contains all paths the app needs to operate. 
			§ views.py : the file contains all functions our website needs 
		○ manage.py
		○ README.md
		
    

		Distinctiveness and Complexity: 
I do believe that my project satisfies the distinctiveness and complexity requirements because it does what the restaurants needs entirely. The app allows both customer and seller to have the maximum freedom to choose whatever they want to add and delete from both bills and menu. Also, the app allows the seller to rearrange the prices whenever needed. The page that contains the list of all orders details, explain to the customer in details what they are about to confirm in the order, and how the total price they will play. Moreover, the seller has the ability to confirm the final order details.
    
    Chipotle Mexican Grill restaurant website that I have created for both owner of the restaurant and customer. The owner can use Django Admin Page to create more Chipotle menu options and toppings. Also, they can decide how many toppings the customer can have and whether it is big or small. Also, the Owner have the authority to confirm whatever order the customer made by approving pending orders. Also, the owner has the full control of prices of all listings in the menu. Each time the owner decides to create new listing in his menu, The admin page is a very simple straight forward page that allow users to add whatever they want in term of the type of the food they want to add, the amount of the mo0ney they want to put for each new listing and also whether if it is big or small listing option. Moreover, the page allows the admin of to change or delete any selection has been made previously in a very practical and precise way. 
    
    For customer, they can pick whatever they want from the menu and decide to add any toppings they want from the toppings list, they also have ability to decide how many toppings they want, and if it is small or big, with different prices. Moreover, the customer can decide what subs they want to add to their order, with the ability to decide what size they want.
    
There is also, a shopping cart page that contain orders list of all customer’s choices from the menu, the list adds down and option the customer picks and adds to the total the full amount due, each option appears on the Shopping Cart has its price next to it.
   
When the customer clicks “Place Order” button that appear on the bottom of the Shopping Cart menu, another page opens up where you can press “Confirm Order” there you confirm you orders as a customer, and wait to the Admin user “Owner” to approve the transaction. After pressing the “Confirm Order” button, a red sign appears and it says “pending” where you as a customer just wait to the Admin to confirm your orders.

    My project has one JS page where I have written functions deals with check boxes for toppings and also whenever a burrito order is clicked, also whenever a box unclicked if a customer wanted to change a topping. Another helper function that counts checked boxes. Another function that passes the checkbox name to the function.

    I have also created a CSS style page that deals with all color, appearance and font of may project website. For the pages on my website, I have wrote six html pages to cover all my website page’s needs (base.html, confirm.html, index.html-login.html-register.html-staff.html.


    An admin page where I have my models registered that contains (BurritoBowl – ChipotleBurritoWrap - Toppings-Subs) and a model page in my order app that consist all the model I have created to make sure that my website run perfectly. Also, a urls.py page that contains all paths needed to be taken so the movement between all pages in my website preform perfectly.

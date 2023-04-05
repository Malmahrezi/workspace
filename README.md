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

I do believe that my project satisfies the distinctiveness and complexity requirements because it does satisfy what a successful restaurant need.. The app allows both customers and seller to have the maximum freedom to choose whatever they want to add and delete from both bills and menu whereas not all restaurants websites have that much flexibility in the website. Also, the app allows the seller to rearrange the prices whenever needed. The page that contains the list of all orders details, explain to the customer deeply what they are about to confirm in their order, and how much they will pay. Moreover, the seller has the ability to confirm the final order after reviewing the entire list in details easily, which what I have focused to prepare during building the website. I have spent long time reviewing other’s restaurant websites to figure out what they are missing to provide to both of their customers and restaurant owner in term of authorities and specifications that are available for the customer. Which gave me a clear diagram of what kind of website I should program, and what specifications I am supposed to implement in the website. The most important factor to focus on was, how to program a website that will guarantee best experience for the customer which will lead to best financial benefit for the seller.
    
Chipotle Mexican Grill restaurant website that I have created for both owner of the restaurant and their customer. The owner can use Django Admin Page to create more Chipotle menu options and toppings. Also, they can decide how many toppings the customer can have and whether it is big or small. Also, the Owner have the authority to confirm whatever order the customer made by approving pending orders. moreover, the owner has the full control of prices of all listings in the menu. Each time the owners decides to create new listing in their menu, The admin page is a very simple processes page  that allow users to add whatever they want in term of the type of the food they want, the amount of the money they want to bill the customer for each new listing and also whether if it is big or small listing option. Moreover, the page allows the admin of to change or delete any selection has been made previously in a very practical and precise way. These specifications I created to make sure that both sides get the best experience possible making and dealing the orders in the website. The website is very practical and fun to use, also It is very simple for the owner to manage and fix whatever they decide to fix, especially in term of adding more options for their menu or updating their prices.
    
For customer, they can pick whatever they want from the menu and decide to add any toppings they want from the toppings list, they also have ability to decide how many toppings they want, and if it is small or big, with different prices. Moreover, the customer can decide what subs they want to add to their order, with the ability to decide what size they want. The customer experience using the website is going to be fun and effective. They first need to register in the website in the registration page, then they will be redirected to the menu page where they will be able to pick from the menu whatever they want from the main courses and whether they want add any toppings, drink etc. Whenever they click in any option they want, immediately in the top corner on the same page, a bill popup with what they have added to their basket including the price of each item. Moreover, the customer can delete and add from the basket which give them more flexibility shopping using the website. 
    
There is also, a shopping cart page that contain order’s list of all customer’s choices from the menu, the list adds up all options the customer picks and adds everything to the total amount due, each option appears on the Shopping Cart has its price next to it. When the customer clicks “Place Order” “button that appear on the bottom of the Shopping Cart menu”, another page opens up where you can press “Confirm Order”,  there you confirm your orders as a customer, and wait to the Admin user “Owner” to approve the transaction. After pressing “Confirm Order” button, a red sign appears and it says “pending” where you as a customer just wait to the Admin to confirm your orders.

My project has one JS page where I have written the functions deals with check boxes for toppings and also whenever a burrito order is clicked, also whenever a box unclicked if a customer wanted to change a topping. Another helper function that counts checked boxes. Moreover, there is another function that passes the checkbox name to the function.

I have also created a CSS style page that deals with all color, appearances and fonts of my project’s website. For the pages on my website, I have wrote six html pages to cover all my website page’s needs (base.html, confirm.html, index.html-login.html-register.html-staff.html.


An admin page where I have my models registered that contains (BurritoBowl – ChipotleBurritoWrap - Toppings-Subs) and a model page in my order app that consist all the model I have created to make sure that my website run perfectly. Also, a urls.py page that contains all paths needed to be taken so the movement between all pages in my website performs perfectly.

At the end, I hope the website I have built will satisfy both customers and business owners, as we all know, a perfect website a developer build comes as a result of hard working and a good programming code. However, the most important to know before building any website is to ask yourself as a developer, what are my client’s needs, who are their customers, their preferences, and what are the keys inside the website code that are open to improve as business owners maybe decide to grow. That is because what is the best is to improve the website that you already have instead of developing a new one.

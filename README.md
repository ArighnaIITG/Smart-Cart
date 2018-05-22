# Smart-Cart
An e-commerce shopping cart website, created using Django, and Bootstrap.

## Technology this app uses:

  1. Python 2.7.2
  2. Django 1.8.1
  3. SQLite 3 (Database, you can use MySQL or PostGreSQL)
  
Please make sure these versions are installed and in use, before following the installation instructions given below.
  
## Installation

  1. Clone this repository.
  2. Navigate to the root directory of this repo and run `python manage.py syncdb`. You will be prompted to create a superuser login for the admin page. Create one, or you can directly create superuser using `python manage.py createsuperuser`.
  3. Run `python manage.py runserver`. This will launch your server at `localhost:8000`.
  4. If you further make changes to your models in the cloned repo, run the following commands to commit those changes :-
        a) `python manage.py makemigrations`
        b) `python manage.py migrate`
        
 Enjoy the application..!!
 
 # Wishlist
 
 Some features I would like to implement in the future:

    Checkout
        select address
        saves order to database, searchable by user and by merchant
    Shopping cart improvements:
        edit cart
        persist cart using cart table in db
    More user features:
        Edit email, change password, etc
        view past orders
        view saved carts
    Admin features:
        admins can search for customers, orders
        admins can edit the products on sale
        admins can choose the name of their store, and get a subdomain for it
        
 Please feel free to contribute...!!

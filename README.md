Hotel Search App in Django
This is a simple Hotel Search application built using Django for the backend, Vue.js for front-end interactivity, and Bootstrap for styling. Users can search and sort hotels based on price (ascending or descending) and filter hotels within a specified price range.

Features
Dynamic sorting by hotel price (Ascending or Descending).
Price filtering based on user input.
Uses Vue.js for front-end interactivity.
Django for the backend to handle requests and manage data.
JSON response for hotel data to dynamically update the UI.
Project Structure
arduino

hotel_search/
│
├── home/
│   ├── migrations/
│   ├── templates/
│   │   └── home.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── hotel_search/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
Installation
1. Clone the Repository
bash
git clone https://github.com/your-username/hotel_search.git
cd hotel_search
2. Set Up Virtual Environment
bash
# Install virtualenv if you haven't
pip install virtualenv

# Create virtual environment
virtualenv env

# Activate virtual environment
# For Windows
.\env\Scripts\activate

# For macOS/Linux
source env/bin/activate
3. Install Dependencies
bash
pip install -r requirements.txt
If you don't have a requirements.txt file, manually install Django:

bash
pip install django
4. Set Up Database
bash
python manage.py makemigrations
python manage.py migrate
5. Create Superuser
bash
python manage.py createsuperuser
Follow the prompts to create an admin user for the Django admin panel.

6. Run the Development Server
bash
python manage.py runserver
Open a browser and visit http://127.0.0.1:8000 to view the app.

Usage
Access the home page at http://127.0.0.1:8000/.
Sort hotels by price (Ascending/Descending) or filter by price range.
To add hotel data, visit the Django admin panel at http://127.0.0.1:8000/admin/ and create new hotel records.
Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

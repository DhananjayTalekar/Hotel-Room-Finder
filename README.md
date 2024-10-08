Hotel Search App in Django
Project Overview
The Hotel Search App is a web application built using Django, Vue.js, and Bootstrap that allows users to search for hotels and sort them based on price. The application provides a user-friendly interface for filtering and sorting hotels in ascending or descending order by price, offering a seamless browsing experience.

Users can interact with the app to view hotel listings, sort them by price, and filter by a specific price range, making it easy to find suitable accommodation based on their budget.

Features
Hotel Listings: Display a dynamic list of hotels, including their name, price, and description.
Sorting Functionality: Sort hotels in ascending or descending order based on price.
Price Filtering: Filter hotels by price range to find hotels that fit the user's budget.
Vue.js for Interactivity: Integrated Vue.js for dynamic UI updates, allowing users to instantly sort and filter results without page reloads.
Bootstrap for Styling: Utilized Bootstrap for a responsive and modern user interface.
Django Admin Integration: Use the Django admin panel to easily add, edit, and delete hotel entries.
Tech Stack
Backend: Django
Frontend: HTML, Vue.js, Bootstrap
Database: SQLite (default Django database)
Styling: Bootstrap
Project Structure
arduino
Copy code
hotel_search/
├── home/
│   ├── migrations/
│   ├── templates/
│   │   └── home.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── hotel_search/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── db.sqlite3
Installation and Setup
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/hotel_search_app.git
Navigate to the project directory:

bash
Copy code
cd hotel_search_app
Create and activate a virtual environment:

bash
Copy code
virtualenv env
source env/bin/activate  # On Windows, use: .\env\Scripts\activate
Install the project dependencies:

bash
Copy code
pip install -r requirements.txt
Run the following commands to set up the database:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create a superuser to access the Django admin panel:

bash
Copy code
python manage.py createsuperuser
Run the development server:

bash
Copy code
python manage.py runserver
Access the app by visiting http://127.0.0.1:8000/ and the admin panel at http://127.0.0.1:8000/admin/.

Usage
Admin Panel: Add, edit, or delete hotel data using Django’s admin interface.
Hotel Search: Users can view the list of hotels, sort by price (ascending/descending), and filter hotels by price range.
Future Enhancements
Add search functionality for hotels based on location.
Implement user authentication for personalized experiences.
Enable rating and reviews for each hotel.
Connect the app to a more scalable database, such as PostgreSQL.
Contributing
Feel free to fork the project, create a pull request, or open an issue for suggestions and improvements.

How to run the app :

1. Launch the database server
2. change your directory ../interface/demo
3. python manage.py runserver

Files that you have to look up :

1. views.py : Functionality for retrieving the query and giving responses mostly done here in this file
2. templates/chat_view.html and home.html : Html pages, nothing special. Design mostly done here.
3. urls.py : used to map web requests to the appropriate view functions or class-based views
4. forms.py : to handle input query
5. models.py : to handle database for chat history

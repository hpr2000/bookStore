# bookStore
Flask Bookstore Web Application with Neo4j
This is a simple Flask web application for managing a bookstore. It allows you to add, update, and delete books. The application is integrated with a Neo4j database to store and retrieve book information.

Prerequisites
Before running this application, make sure you have the following dependencies installed:
  Python
  Flask
  Neo4j
  Py2neo
  
You can install Flask and Py2neo using pip:
  pip install Flask py2neo

Getting Started
1. Clone the repository to your local machine.

2. Set up a Neo4j database and replace the Neo4j connection details in app.py with your own. You need to change the following line to match your Neo4j server:
     graph = Graph("bolt://localhost:7687", auth=("your_username", "your_password"))
3. Create a virtual environment and activate it:
     python -m venv venv source venv/bin/activate
4. Run the following command to start the Flask application:
     python app.py
5. Open your web browser and go to 'http://localhost:5000' to access the bookstore application.


Usage
Adding a Book
  To add a book, fill in the Title, Author, and Genre fields in the form on the homepage and click the "Add Book" button.
Updating a Book
  Click the "Update" link next to the book you want to update.
  Update the book details in the form and click the "Update Book" button.
Deleting a Book
  Click the "Delete" link next to the book you want to delete.
Visualization
  The application also includes a simple pie chart that visualizes the count of books by author using Plotly.

Project Structure
  app.py: The Flask application code.
  index.html: The HTML template for the homepage.
  update.html: The HTML template for the book update page.

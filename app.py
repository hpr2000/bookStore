from flask import Flask, render_template, request, redirect, url_for
from py2neo import Graph
import uuid

app = Flask(__name__)
app.config['DEBUG'] = True
graph = Graph("bolt://localhost:7687", auth=("neo4j", "hardi1902"))  # Replace with your Neo4j connection details


@app.route('/')
def index():
    # Retrieve books from the Neo4j database
    query = """
        MATCH (book:Book)
        RETURN id(book) AS id, book.title AS title, book.author AS author, book.genre AS genre
    """
    books = graph.run(query).data()
    return render_template('index.html', books=books)


@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']

    # Generate a unique ID for the new book
    book_id = str(uuid.uuid4())

    # Create a new book node in the Neo4j database with the unique ID
    query = """
        CREATE (book:Book {id: $id, title: $title, author: $author, genre: $genre})
        """
    graph.run(query, id=book_id, title=title, author=author, genre=genre)

    return redirect(url_for('index'))


@app.route('/update/<int:book_id>', methods=['GET', 'POST'])
def update_book(book_id):
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']

        # Update the book in the Neo4j database
        query = """
            MATCH (book:Book)
            WHERE id(book) = $id
            SET book.title = $title, book.author = $author, book.genre = $genre
        """
        graph.run(query, id=book_id, title=title, author=author, genre=genre)

        return redirect(url_for('index'))
    else:
        # Retrieve book details for the update form, including the 'id' attribute
        query = """
            MATCH (book:Book)
            WHERE id(book) = $id
            RETURN id(book) AS id, book.title AS title, book.author AS author, book.genre AS genre
        """
        book = graph.run(query, id=book_id).data()[0]
        return render_template('update.html', book=book)


@app.route('/delete/<int:book_id>')
def delete_book(book_id):
    # Delete the book from the Neo4j database
    query = """
        MATCH (book:Book)
        WHERE id(book) = $id
        DELETE book
    """
    graph.run(query, id=book_id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()

document.addEventListener('DOMContentLoaded', async () => {
    const bookList = document.getElementById('book-list');
    
    const response = await fetch('http://localhost:8000/books/');
    const books = await response.json();
    
    books.forEach(book => {
        const bookElement = document.createElement('div');
        bookElement.textContent = `${book.title} by ${book.author}`;
        bookList.appendChild(bookElement);
    });
});

You are managing a book club. You have a collection of books and a list of club members. Each book has a specific genre, and each club member has a preferred genre. Your goal is to create a function named recommend_books that matches club members with books based on their genre preferences.

Details:

The function should take two arguments: members and books, where:

1. members is a list of dictionaries, each representing a club member's details like name and preferred_genre.

2. books is a list of dictionaries, each representing a book's details including its title and genre.
The function should recommend a book to each club member based on their preferred genre. A book can be recommended to multiple members. If a member's preferred genre isn't available in the book collection, they should not be recommended any book.

The function should return a list of dictionaries, each indicating the recommendation of a book to a club member. Each dictionary should have the keys "member" and "book" where the values are the names of the club member and the title of the book respectively. If no book is recommended for a member, the "book" key should have the value None.
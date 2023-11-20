def recommended_books(members,books):
    recom=[]

    for member in members:
        name=member["name"]
        genre=member["preferred_genre"]
        matchedBooks=[book["title"] for book in books if book["genre"]==genre]
        if matchedBooks:
            recom_book=matchedBooks[0]
        else:
            recom_book=None
        
        recom.append({"member":name,"book":recom_book})
    return recom


members=[
    {"name": "Alice","preferred_genre": "Romance"},
     {"name": "Bob","preferred_genre": "Sci-Fi"},
]
 
books=[
   { "title":"Love in the Rain","genre":"Romance"},
    { "title":"Historian gama","genre":"History"}
 ]


res= recommended_books(members,books)
print(res)
'''
Create a dictionary representing a library catalogue.
Each book should have a title, author, and publication year.
'''
# two dimential dictionary
library_catalogue = {
    "ONE": {
        "title": "Notes from a Dead House",
        "author": "Fyodor Dostoevsky",
        "publication_year": 1862
    },
    "TWO": {
        "title": "Nineteen Eighty-Four",
        "author": "George Orwell",
        "publication_year": 1949
    },
    "THREE": {
        "title": "Animal Farm",
        "author": "George Orwell",
        "publication_year": 1945
    }
}
for key, value in library_catalogue.items():
    print(f"{key} : {value}")

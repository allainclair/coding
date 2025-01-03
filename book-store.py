POST /book-store/

header = {Authenticate: "Bearer JWT"}

{
    "book": {
        "title": "The Lord of the Rings",
        "author": "J. R. R. Tolkien",
        "yea":  1954,
    }
}
RETURN: {id: uuid()}

GET /book-store/{id}

RETURN:
{
    "book": {
        "title": "The Lord of the Rings",
        "author": "J. R. R. Tolkien",
        "yea":  1954,
    }
}

PUT /book-store/{id}
{
    "book": {
        "title": "Another Title",
        "author": "J. R. R. Tolkien",
        "yea":  1954,
    }
}

RETURN: created 201

------
POST /users/ # Create a new user
{
    "user": {
        "name": "John",
        "email":  "email@me.com",
    }
}

RETURN: {user_id: uuid()}

GET /users/{id} # Get a user

# 100 requests
# JWT
# 101 expired
# Request with a JWT expired
{JWT}

POST /users/new-session

# from flask import Flask

# app = Flask(__name__)

# if __name__=="__main__":

#     app.run()




from flask import Flask

app = Flask(__name__)

usersList = [

    {

        "id": 1,

        "username": "prashant",

        "name": "Prashant Dey",

        "age": 30

    },

    {

        "id": 2,

        "username": "ashish",

        "name": "Ashish Kumar",

        "age": 70

    },

    {

        "id": 3,

        "username": "sarthak",

        "name": "Sarthak Nigam",

        "age": 29

    }

]

@app.route('/', methods=["GET"])

def main():

    return "Hello World!"

@app.route('/user/<string:username>')

def users(username):

    

    return f"User: {username}"

@app.route('/about', methods=["GET"])

def about():

    return "This is about section"

@app.route('/contact', methods=["GET","POST"])

def contact():

    return "This is contact"

if __name__=="__main__":

    app.run(debug=True, port=5005)

from flask import Flask

app = Flask(__name__)

usersList = [

    {

        "id": 1,

        "username": "prashant",

        "name": "Prashant Dey",

        "age": 30

    },

    {

        "id": 2,

        "username": "ashish",

        "name": "Ashish Kumar",

        "age": 70

    },

    {

        "id": 3,

        "username": "sarthak",

        "name": "Sarthak Nigam",

        "age": 29

    }

]

@app.route('/', methods=["GET"])

def main():

    return "Hello World!"

@app.route('/user/<string:username>')

def users(username):
    users == usersList
    return f"User: {username}"

@app.route('/about', methods=["GET"])

def about():

    return "This is about section"

@app.route('/contact', methods=["GET","POST"])

def contact():

    return "This is contact"

if __name__=="__main__":

    app.run(debug=True, port=5005)













    @app.route('/user/<string:username>')

def users(username):

    # Logic to fetch the user and show their age

    try:

        for user in usersList:

            if user['username'].lower() == username.lower():

                return f"User: {username}, Age: {user['age']}"

            else:

                return {"msg": "User not found"}        

    except Exception as e:

        print(e)

        return {"msg": "Something went wrong"}
    











    from flask import Flask, request

app = Flask(__name__)

usersList = [

    {

        "id": 1,

        "username": "prashant",

        "name": "Prashant Dey",

        "age": 30

    },

    {

        "id": 2,

        "username": "ashish",

        "name": "Ashish Kumar",

        "age": 70

    },

    {

        "id": 3,

        "username": "sarthak",

        "name": "Sarthak Nigam",

        "age": 29

    }

]

@app.route('/', methods=["GET"])

def main():

    return "Hello World!"

@app.route('/user/<string:username>')

def users(username):

    # Logic to fetch the user and show their age

    try:

        for user in usersList:

            if user['username'].lower() == username.lower():

                return f"User: {username}, Age: {user['age']}"

            else:

                return {"msg": "User not found"}        

    except Exception as e:

        print(e)

        return {"msg": "Something went wrong"}

@app.route("/people")

def people():

    user = request.args.get("user")

    age = request.args.get("age")

    return f"user: {user} | age: {age}"

 

@app.route('/about', methods=["GET"])

def about():

    return "This is about section"

@app.route('/contact', methods=["GET","POST"])

def contact():

    return "This is contact"

if __name__=="__main__":

    app.run(debug=True, port=5005)





    
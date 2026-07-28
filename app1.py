# from flask import Flask

# app = Flask(__name__)

# @app.route("/", methods= ["GET"])
# def main():
#     return "hello world!"
# @app.route("/user", methods= ["GET"])
# def set():
#     return "this is praveen webside"
# if __name__ == "__main__":
#     app.run(debug=True)



# # @app.route("/login", methods=["POST"])

# # def login():

# #     username = request.get_json("username")

# #     password = request.get_json("password")

# #     print(username, password)

# #     return usernamefro



# from flask import Flask 
# app = Flask(__name__)

userlist = [
 {
  "ID": "3856",
  "name": "navena",
  "study": "T TECH",
  "age": 30

 },
{
  "ID": "3456",
  "name": "vamsi sir",
  "study": "B TECH",
  "age": 28

 },

 {
  "ID": "4456",
  "name": "naveen",
  "study": "M TECH",
  "age": 29

 }

]

# @app.route("/user/<username>")
# def main (username):
 
#     for user in userlist:
#      if user["name"] == username:
#         return f'Name: {user["name"]},Age:{user["age"]}'
     
#     return "user not found"
       
# if __name__ == "__main__":
#  app.run(debug=True)


from flask import Flask , request

app = Flask(__name__)

@app.route("/user/<string:username>", methods=["GET", "POST"])
def HSB(username):
    try:
        for user in userlist:
            if user["name"].lower() == username.lower():
                return f'Name: {user["name"]}, Age: {user["age"]}'

        return {"msg": "User not found"}

    except Exception as e:
        return {"msg": str(e)}
    

@app.route("/people")
def people():
    user = request.args.get("user")
    age = request.args.get("age")
    return f'user: {user} | age: {age}'

if __name__ == "__main__":
    app.run(debug=True)
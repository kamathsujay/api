# To create a FastAPI application in Python that utilizes the PUT method for updating resources
from fastapi import FastAPI
from pydantic import BaseModel  # enforce data validation

app = FastAPI()  # Creates an instance of the FastAPI application.

# In-memory "database" for demonstration
user_db = {
    1:{"name":"sujay","age": 50},
    2:{"name":"radhika","age": 43},
    3:{"name":"jay","age": 17}
}

# Pydantic model for request body validation
class User(BaseModel): #User can be any value.
    name:str
    age:int

# Expose the function
@app.put("/user_db/data/v1/update/{user_id}")   
# can be any path as you wish, where user_id is parameter to send data inside body

# PUT method
# Create function to update
def user_update(user_id: int, user:User):
    if user_id in user_db:
        user_db[user_id] = user.dict()  # dict is dictionary operation
        print(user_db) #to print in Terminal
        return {"message": "User updated successfully", "user":user_db[user_id]}
    else:
        return{"message":"User not found"}

# Expose the function
@app.delete("/user_db/data/v1/delete/{user_id}")   
# DELETE method
def delete_user(user_id: int):
  if user_id in user_db:
        del user_db[user_id]
        print(user_db) #to print in Terminal
        return {"message": "User deleted successfully"}
  else:
        return{"message":"User not fclound"}   

# run the file.
# uvicorn testing081225:app --reload  
# Take URL from terminal http://localhost:8000/docs and paste in browser

# POSTMAN testing
# Type PUT; specify URL. 
'''
URL for updating record 2: http://localhost:8000/user_db/data/v1/update/2
json body as follows:
json
{
    "name": "Chitra",
    "age": 70
}
'''
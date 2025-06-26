from fastapi import FastAPI, Form, Request, Depends, HTTPException, Query       #Read password/user , allows reading http request
from fastapi.templating import Jinja2Templates #used for html files and python logic inside or rendering html pages
from fastapi.responses import HTMLResponse, RedirectResponse   # tells fastapi to return a full html page as response type
from sqlalchemy.orm import Session         #used to interact with database  , object-relation making
from database import SessionLocal, engine  #session your custom function to get database , engine is the actual database connection
from models import User           #import user table/class from models.py
# from passlib.hash import bcrypt #bcrypt is used to hash and verify passwords securely
from jose import jwt , JWTError  # a library that implements the JavaScript Object Signing and Encryption 
from datetime import datetime, timedelta
from passlib.context import CryptContext  
import bcrypt
from fastapi.responses import JSONResponse
from typing import List


#Helper for hashing passwords using different algorithms.

# Create table
# import models
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# templates = Jinja2Templates(directory="templates")

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db            #yield is used to create genrators , genrators allows you to declare a function that behaves like an iterator

#     finally:
#         db.close()



# Get all users (no Pydantic)
@app.get("/users")
def get_users():
    db: Session = SessionLocal()
    users = db.query(User).all()
    return [
        {
            "id": user.id,
            "username": user.username,
            "email": user.email
        } for user in users
    ]

@app.post("/login")
def login(email: str = Form(), password: str = Form()):
    db: Session = SessionLocal()
    user = db.query(User).filter(User.email == email).first()

    if user and bcrypt.checkpw(password.encode(), user.hashed_password.encode()):
        print("Login successful")
        return JSONResponse(content={"message": "Login successful"}, status_code=200)
    else:
        print("Invalid email or password")
        return JSONResponse(content={"message": "Invalid email or password"}, status_code=401)

# @app.post("/register")
# def register(
#     username: str = Form(...),
#     email: str = Form(...),
#     password: str = Form(...),
#     db: Session = Depends(get_db)
# ):
#     existing_user = db.query(User).filter(User.username == username).first()
#     if existing_user:
#         return {"error": "User already exists"}

#     hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
#     print("Hashed password:", hashed_password)

#     new_user = User(username=username, email=email, hashed_password=hashed_password)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

# @app.get("/emails")
# def get_all_emails(domain: str = None):
#     db: Session = SessionLocal()
    
#     if domain:
#         pattern = f"%@{domain}"
#         print("Searching with pattern:", pattern)
#         users = db.query(User.email).filter(User.email.ilike(pattern)).all()
#     else:
#         users = db.query(User.email).all()

#     email_list = [email[0] for email in users]
#     print("Found emails:", email_list)

#     return {"emails": email_list}

































# def hash_password(password:str):
#     return pwt_context.hash(password)
            
# def verify_password(plain:str , hashed:str):
#     return pwt_context.verfiy(hash_password)

# def create_token(username:str):
#     expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINITUES)
#     payload={"sub": username , "exp": expire}
#     return jwt.encode(payload,SECRET_KEY, algorithm= ALGORITHM)

# def decode_token(token:str):
#     try:
#         payload=jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
#         return payload.get("sub")
#     except JWTError:
#         raise HTTPException(status_code="101", detial= "Invalid" or "expire token")







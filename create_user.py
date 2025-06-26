from database import SessionLocal
from models import User
from passlib.hash import bcrypt

db = SessionLocal()
user = User(email="sarthak@gammaedge.com", hashed_password=bcrypt.hash("sarth123"))
db.add(user)
db.commit()
db.close()
print("Test user created.")



#hash return an integer value representing the input object
# passlib is a password hashing library
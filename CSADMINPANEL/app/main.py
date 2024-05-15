from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import User
from schemas import UserOut, UserCreate
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=UserOut)  # Use the User model as the response model
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.

    This endpoint creates a new user in the database.

    - **user**: UserCreate - The user data to be created.
    - **db**: Session = Depends(get_db) - The database session dependency.

    Returns:
        User: The newly created user.
    """
    # Check if passwords match
    if user.password != user.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    # Create user in database without specifying the id field
    db_user = User(
        firstname=user.firstname,
        lastname=user.lastname,
        phone_no=user.phone_no,
        email=user.email,
        password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/{user_id}", response_model=UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve user details by user ID.

    This endpoint retrieves user details from the database based on the provided user ID.

    - **user_id**: int - The ID of the user to retrieve.
    - **db**: Session = Depends(get_db) - The database session dependency.

    Returns:
        UserOut: The user details.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

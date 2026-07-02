from datetime import datetime, timedelta, UTC
from base64 import b64decode
from typing import List

import jwt
from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session

import setting
from database import Session
from .schemas.auth import UserAuth
from database.schemas.user import User
from database.schemas.role import Role


SECRET_KEY = b64decode(setting.SECRET_KEY)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 6000


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, Query
from typing import Optional

security_scheme = HTTPBearer(auto_error=False)

def get_token(
    request: Request,
    header_token: Optional[HTTPAuthorizationCredentials] = Depends(security_scheme),
    query_token: Optional[str] = Query(None, alias="token")
) -> str:
    if header_token:
        return header_token.credentials
    if query_token:
        return query_token
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Not authenticated",
        headers={"WWW-Authenticate": "Bearer"},
    )

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )


def get_current_user(token: str = Depends(get_token)):
    payload = verify_token(token)
    return UserAuth(**payload)


def get_current_user_with_role(token: str = Depends(get_token), db: Session = Depends(get_db)):
    payload = verify_token(token)
    user = db.query(User).filter(User.id == payload.get("user_id")).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


def check_role(required_roles: List[str]):
    async def role_checker(user: User = Depends(get_current_user_with_role)):
        if user.role.name not in required_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions",
            )
        return user
    return role_checker

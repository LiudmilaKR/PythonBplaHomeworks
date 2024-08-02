import jwt
from datetime import datetime, timezone, timedelta

SECRET_KEY = 'myKEY12345'

def generate_token(user_id):
    payload = {'user_id': user_id, 'exp': datetime.now(timezone.utc) + timedelta(seconds=5)}
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def get_token(user_id):
    if user_id:
        user_id = 'Inga'
        token = generate_token(user_id)
        return token
    return None

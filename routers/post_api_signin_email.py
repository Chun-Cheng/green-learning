from fastapi import APIRouter, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from datetime import datetime
import uuid
from model import model

router = APIRouter(prefix='/api', tags=['APIs'])
templates = Jinja2Templates(directory='templates')

class EmailSigninRequest(BaseModel):
    email: str
    device: str
    # verify_code: int

# sign in api
@router.post('/signin_email')
async def sign_in(request: Request, signin_request: EmailSigninRequest):#email: str, device: str):
    email = signin_request.email
    device = signin_request.device
    # check signup_request's format (regex)

    user = model.execute('SELECT username from users WHERE email = ?', (email,)).fetchone()
    # check whether the account exist
    if user is None:
        raise HTTPException(404)
    else:
        # add a new session
        username = user[0]
        timestamp = int(datetime.now().timestamp())
        session_id = str(uuid.UUID(int=timestamp))
        new_session = (
            session_id,  # id
            username,  # username
            datetime.now().isoformat(),  # create_datetime
            None,  # expire_datetime
            device  # device
        )
        # update sessions
        model.execute('INSERT INTO sessions VALUES(?, ?, ?, ?, ?)', new_session)
        # update users
        original_sessions = model.execute('SELECT sessions from users WHERE username = ? ', (username,))
        model.execute('UPDATE users SET sessions = ?', (f'{original_sessions},{session_id}',))
    
    response_content = {'session_id': session_id}
    response_content = jsonable_encoder(response_content)
    return JSONResponse(response_content)
    
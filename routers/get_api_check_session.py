from fastapi import APIRouter, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from datetime import datetime
from model import model

router = APIRouter(prefix='/api', tags=['APIs'])
templates = Jinja2Templates(directory='templates')

# check session api
@router.get('/check_session')
async def check_session(request: Request, session_id: str):
    # check format (regex)

    session = model.execute('SELECT username from sessions WHERE id = ?', (session_id,)).fetchone()
    # check whether the account exist
    if session is None:
        raise HTTPException(404)
    elif True:  # the session has expired
        pass
        # remove the session
        # raise HTTPException(404)
    
    username = session[0]
    response_content = {'username': username}
    response_content = jsonable_encoder(response_content)
    return JSONResponse(response_content)
    
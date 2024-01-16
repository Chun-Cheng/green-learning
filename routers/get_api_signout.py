from fastapi import APIRouter, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
# from pydantic import BaseModel
from model import model

router = APIRouter(prefix='/api', tags=['APIs'])
templates = Jinja2Templates(directory='templates')

# sign out api
@router.get('/signout')
async def sign_out(session_id: str):
    # delete from sessions
    session = model.execute('SELECT username from sessions WHERE id = ?', (session_id,)).fetchone()
    username = session[0]
    model.execute('DELETE FROM sessions WHERE id = ?', (session_id,))

    # delete from users
    session_list = model.execute('SELECT sessions from users WHERE username = ? ', (username,)).fetchone()
    if session_list is not None:
        session_list = session_list[0].split(',')
        session_list.remove(session_id)
        new_session_str = ''
        for session in session_list:
            new_session_str += f'{session},'
        new_session_str = new_session_str[:-1]
        model.execute('UPDATE users SET sessions = ?', (new_session_str,))

    response_content = { 'message': 'success!' }
    response_content = jsonable_encoder(response_content)
    return JSONResponse(response_content)
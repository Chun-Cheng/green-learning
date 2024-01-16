from fastapi import APIRouter, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from model import model

router = APIRouter(prefix='/api', tags=['APIs'])
templates = Jinja2Templates(directory='templates')

# sign in api
@router.get('/add_read_time')
async def add_read_time(session_id: str, page_id: str, seconds: int, update: str):
    # check params's format (regex)

    # get user by session_id
    session = model.execute('SELECT username FROM sessions WHERE id=?', (session_id,)).fetchone()
    if session is None:
        raise HTTPException(404)
    username = session[0]

    reading_record = model.execute('SELECT duration from reading_history WHERE username = ? AND page_id = ?', (username, page_id)).fetchone()
    if reading_record is None:
        new_reading_record = (
            f'{username}-{page_id}',  # id
            username,  # username
            page_id,  
            update,  # start_datetime
            update,  # update_datetime
            seconds  # duration
        )
        model.execute('INSERT INTO reading_history VALUES(?, ?, ?, ?, ?, ?)', new_reading_record)
        # update user.reading_history
    else:
        seconds += reading_record[0]
        model.execute('UPDATE reading_history SET duration = ?, update_datetime = ? WHERE username = ? AND page_id = ?', (seconds, update, username, page_id))
        # update user.reading_history

    # 
    print(model.execute('SELECT * from reading_history').fetchone())
    # 

    response_content = {}
    response_content = jsonable_encoder(response_content)
    return JSONResponse(response_content)
    
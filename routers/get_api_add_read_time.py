from fastapi import APIRouter, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from model import model

router = APIRouter(prefix='/api', tags=['APIs'])
templates = Jinja2Templates(directory='templates')

# sign in api
@router.post('/add_read_time')
async def add_read_time(request: Request, user: str, page_id: str, seconds: int, update: str):
    # check params's format (regex)

    # check whether the account exist
    # if not exist
    #     raise HTTPException()

    reading_record = model.execute('SELECT duration from reading_history WHERE username = ? AND page_id = ?', f'%{user}%', f'%{page_id}%')
    if reading_record is None:
        new_reading_record = [
            f'{user}-{page_id}',  # id
            user,  # username
            page_id,  
            update,  # start_datetime
            update,  # update_datetime
            seconds  # duration
        ]
        model.execute('INSERT INTO reading_history VALUES(?, ?, ?, ?, ?, ?)', new_reading_record)
    else:
        seconds += reading_record[0]
        model.execute('UPDATE reading_history SET duration = ?, update_datetime = ? WHERE username = ? AND page_id = ?', seconds, update)
    
    response_content = {}
    response_content = jsonable_encoder(response_content)
    return JSONResponse(response_content)
    
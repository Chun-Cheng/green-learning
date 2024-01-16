from fastapi import APIRouter, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
# from pydantic import BaseModel
from model import model

router = APIRouter(prefix='/api', tags=['APIs'])
templates = Jinja2Templates(directory='templates')

# class GetRecordRequest(BaseModel):
#     session_id: str
#     limit: int = 10
#     offset: int = 0

# get read records api
@router.get('/read_records', status_code=status.HTTP_201_CREATED)
async def get_read_records(session_id: str, limit: int = 10, offset: int = 0):
    # session_id = get_record_request.session_id
    # limit = get_record_request.limit
    # offset = get_record_request.offset

    session = model.execute('SELECT username FROM sessions WHERE id=?', (session_id,)).fetchone()
    if session is None:
        raise HTTPException(404)
    username = session[0]
    user = model.execute('SELECT name, reading_history FROM users WHERE username=?', (username,)).fetchone()
    if user is None:
        raise HTTPException(404)
    name = user[0]
    # reading_history_list = user[1].split(',')
    reading_history = model.execute('SELECT page_id, start_datetime, update_datetime, duration FROM reading_history WHERE username = ? ', (username,)).fetchall()
    # 'ORDER BY update_datetime DESC ' + 'LIMIT ? OFFSET ?'
    
    result = { 
        'username': username,
        'name': name,
        'data': [] 
    }
    for record in reading_history:
        page = model.execute('SELECT id, title, book_id FROM pages WHERE id=?', (record[0],)).fetchone()
        if page[2] is None or page[2] == '':
            url = f'/page/{page[0]}'
            title = page[1]
        else:
            book = model.execute('SELECT title FROM books WHERE id=?', (page[2],)).fetchone()
            url = f'/book/{page[2]}/{page[0]}'
            title = f'{page[1]} - {book[0]}'
        result['data'].append({ 
            'url': url, 
            'title': title,
            'start_datetime': record[1],
            'update_datetime': record[2],
            'duration': record[3]
        })
    response_content = jsonable_encoder(result)
    return JSONResponse(response_content)
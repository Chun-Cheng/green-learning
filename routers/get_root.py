from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from model import model

router = APIRouter()
templates = Jinja2Templates(directory='templates')

# homepage
@router.get('/', response_class=HTMLResponse)
async def homepage(request: Request):
    articles = model.execute('SELECT title, author, datetime, content FROM articles').fetchall()
    articles = map(lambda r: {'title': r[0],
                   'author': r[1],
                   'datetime': r[2],
                   'content': r[3]}, articles)
    topics = model.execute('SELECT title, description, courses FROM topics').fetchall()
    topics = map(lambda r: {'title': r[0],
                            'description': r[1],
                            'courses': r[2]}, topics)
    return templates.TemplateResponse('root.html', {'request': request, 
                                                    'articles': articles, 
                                                    'topics': topics})
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from model import model

router = APIRouter()
templates = Jinja2Templates(directory='templates')

# homepage
@router.get('/', response_class=HTMLResponse)
async def homepage(request: Request):
    articles = model.execute('SELECT id, title, author, update_datetime, content FROM pages WHERE book_id = \'\'').fetchall()  # Where book is None/Null/undefined
    articles = map(lambda r: {
                   'id': r[0],
                   'title': r[1],
                   'author': r[2],
                   'update_datetime': r[3],
                   'content': r[4]}, articles)
    # TODO: articles are not displayed
    topics = model.execute('SELECT id, title, description, pages FROM books').fetchall()
    topics = map(lambda r: {'id': r[0],
                            'title': r[1],
                            'description': r[2],
                            'pages': r[3]}, topics)
    return templates.TemplateResponse('root.html', {'request': request, 
                                                    'articles': articles, 
                                                    'topics': topics})
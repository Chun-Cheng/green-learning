from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory='templates')

# sign up page
@router.get('/signup', response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('signup.html', {'request': request})
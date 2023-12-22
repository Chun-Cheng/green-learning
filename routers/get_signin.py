from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory='templates')

# sign in page
@router.get('/signin', response_class=HTMLResponse)
async def sign_in_page(request: Request):
    return templates.TemplateResponse('signin.html', {'request': request})
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory='templates')

# sign up page
@router.get('/signup', response_class=HTMLResponse)
async def sign_up_page(request: Request):
    return templates.TemplateResponse('signup.html', {'request': request})
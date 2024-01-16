from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory='templates')

# sign out page
@router.get('/signout', response_class=HTMLResponse)
async def sign_out_page(request: Request):
    return templates.TemplateResponse('signout.html', {'request': request})
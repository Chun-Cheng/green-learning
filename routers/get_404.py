from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse #, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory='templates')

# 404 Not Found
@router.get('/404', response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('404.html', {'request': request}, 404)
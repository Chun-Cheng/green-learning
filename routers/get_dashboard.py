from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory='templates')

# dashboard page
@router.get('/dashboard', response_class=HTMLResponse)
async def dashboard(request: Request):
    read_records = []
    activity_records = []
    return templates.TemplateResponse('dashboard.html', {'request': request,
                                                         'read_records': read_records,
                                                         'activity_records': activity_records})
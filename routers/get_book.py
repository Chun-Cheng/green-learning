from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import re
from model import model

router = APIRouter()
templates = Jinja2Templates(directory='templates')

# book homepage
@router.get('/book/{book_id}', response_class=HTMLResponse)
async def book_homepage(request: Request, book_id: str):
    # check input data => regex
    book_id = re.search('[a-z0-9_-]+', book_id).string

    # get book data
    book = model.execute('SELECT pages FROM books WHERE id=?', (book_id,)).fetchone()
    # book not found
    if book is None:
        return RedirectResponse('/404')

    # organize and convert data
    # book
    book_pages = book[0].split(',')
    book_homepage = book_pages[0]

    # redirect
    return RedirectResponse(f'/book/{book_id}/{book_homepage}')

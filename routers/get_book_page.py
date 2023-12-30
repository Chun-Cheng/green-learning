from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import re
# import markdown
from model import model

router = APIRouter()
templates = Jinja2Templates(directory='templates')

# book page
@router.get('/book/{book_id}/{page_id}', response_class=HTMLResponse)
async def book_page(request: Request, book_id: str, page_id: str):
    # check input data => regex
    book_id = re.search('[a-z0-9_-]+', book_id).string
    page_id = re.search('[a-z0-9_-]+', page_id).string

    # get book data
    book = model.execute('SELECT id, title, pages FROM books WHERE id=?', (book_id,)).fetchone()
    # book not found
    if book is None:
        return RedirectResponse('/404')

    # get page data
    page = model.execute('SELECT title, author, update_datetime, tags, content FROM pages WHERE id=?', (page_id,)).fetchone()
    # page not found
    if page is None:
        return RedirectResponse('/404')

    # organize and convert data
    # book
    book_id = book[0]
    book_title = book[1]
    book_pages = book[2].split(',')
    # page
    page_title = page[0]
    page_author = page[1]
    page_last_update = page[2]
    page_tags = page[3].split(',')
    page_content = page[4]  # html
    # page_content = markdown.markdown(page[4])  # markdown to html

    # return
    return templates.TemplateResponse('book_page.html', {'request': request, 
                                                         'book_title': book_title, 
                                                         'page_title': page_title,
                                                         'page_author': page_author,
                                                         'page_last_update': page_last_update,
                                                         'page_tags': page_tags,
                                                         'page_content': page_content})

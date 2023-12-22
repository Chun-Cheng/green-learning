import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from model import model
from routers import get_root, get_book, get_book_page, get_page, get_404, get_signup, get_signin
from routers import post_api_signup, post_api_signin

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

app.include_router(get_root.router)  # homepage
app.include_router(get_book.router)  # book
app.include_router(get_book_page.router)  # book page
app.include_router(get_page.router)  # single article page
app.include_router(get_signup.router)  # signup page
app.include_router(get_signin.router)  # signin page

app.include_router(post_api_signup.router)  # signup api
app.include_router(post_api_signin.router)  # signin api

app.include_router(get_404.router)  # 404 Not Found


model.create_table()

'''
# homepage
@app.get('/', response_class=HTMLResponse)
async def root(request: Request):
    articles = [] # get articles from database
    topics = [] # get topics from database
    return templates.TemplateResponse('root.html', {'request': request, 
                                                    'articles': articles, 
                                                    'topics': topics})
'''

# list of articles
@app.get('/articles', response_class=HTMLResponse)
async def articles(request: Request):
    return templates.TemplateResponse('articles.html', {'request': request})

# specific article page
@app.get('/article/{article_id}', response_class=HTMLResponse)  # article_id is the article title
async def article(article_id: str, request: Request):
    # check article_id by regex
    articles = model.execute(f'SELECT title, datetime, tags, content FROM {article_id}')
    article = articles.fetchone()
    return templates.TemplateResponse('article.html', 
                                      {'title': article.title, 
                                       'datetime': article.datetime, 
                                       'tags': article.tags, 
                                       'content': article.contents}, 
                                      {'request': request})

# list of topics
@app.get('/topics', response_class=HTMLResponse)
async def topics(request: Request):
    return templates.TemplateResponse('topics.html', {'request': request})

# specific topic page (have several courses/materials and exams)
@app.get('/topic/{topic_id}', response_class=HTMLResponse)  # topic_id is the topic name
async def topic(topic_id: str, request: Request):
    # find topic data
    return templates.TemplateResponse('topic.html', {'request': request})

# specific course page
@app.get('/course/{course_id}', response_class=HTMLResponse)  # course_id is the course name
async def course(course_id: str, request: Request, topic: str | None = None):
    # topic None check
    # find course data
    return templates.TemplateResponse('course.html', {'request': request})

# specific exam page
@app.get('/exam/{exam_id}', response_class=HTMLResponse)  # exam_id is NOT the exam name
async def exam_form(exam_id: int, request: Request):
    return templates.TemplateResponse('exam_form.html', {'request': request})

# the result after the user submit the answer of specific exam
@app.post('/exam/{exam_id}', response_class=HTMLResponse)
async def exam_submit(exam_id: int, request: Request):
    # process
    return templates.TemplateResponse('exam_result.html', {'request': request})

# about me/us
@app.get('about', response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse('about.html', {'request': request})

# list of related websites
@app.get('/websites', response_class=HTMLResponse)
async def websites(request: Request):
    return templates.TemplateResponse('websites.html', {'request': request})


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=80, reload=True)

# Document: 
# https://fastapi.tiangolo.com/tutorial/first-steps/
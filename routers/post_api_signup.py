from fastapi import APIRouter, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from model import model

router = APIRouter(prefix='/api', tags=['APIs'])
templates = Jinja2Templates(directory='templates')

class SignupRequest(BaseModel):
    name: str
    email: str

# sign up api
@router.post('/signup', status_code=status.HTTP_201_CREATED)
async def sign_up(request: Request, signup_request: SignupRequest):
    # check content type
    content_type = request.headers.get('Content-Type')
    if content_type != 'application/json':
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY)

    name = signup_request.name
    email = signup_request.email

    # check signup_request's format (regex)

    # check whether the email has been registered
    search_result = model.execute('SELECT username FROM users WHERE email=?', (email,)).fetchone()
    if search_result is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
        # To add the additional status code in /docs or /redoc, read the article:
        # https://fastapi.tiangolo.com/advanced/additional-responses/

    # signup (update the database)
    new_user = (
        name, # username  # TODO: add postfix number
        name, # name
        email, # email
        '', # passkey
        '', # otp_key
        '', # sessions
        '', # interests
        '', # weights
        '', # reading_history
        '', # question_history
    )
    model.execute('INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', new_user)

    response_content = { 'username': name }
    response_content = jsonable_encoder(response_content)
    return JSONResponse(response_content, status_code=status.HTTP_201_CREATED)
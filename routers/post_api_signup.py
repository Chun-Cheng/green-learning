from fastapi import APIRouter, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import model

router = APIRouter(prefix='/api', tags=['APIs'])
templates = Jinja2Templates(directory='templates')

class SignupRequest(BaseModel):
    name: str
    email: str

# sign up api
@router.post('/signup', status_code=status.HTTP_201_CREATED)
async def sign_up(request: Request, signup_request: SignupRequest):
    # check signup_request's format (regex)

    # check whether the email has been registered
    search_result = model.execute('SELECT id FROM users WHERE email=?', (signup_request.email,)).fetchone()
    if len(search_result) > 0:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
        # To add the additional status code in /docs or /redoc, read the article:
        # https://fastapi.tiangolo.com/advanced/additional-responses/

    # signup (update the database)

    response_content = {}
    response_content = jsonable_encoder(response_content)
    return JSONResponse(response_content, status_code=status.HTTP_201_CREATED)
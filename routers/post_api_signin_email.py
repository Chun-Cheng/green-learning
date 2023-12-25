from fastapi import APIRouter, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from model import model

router = APIRouter(prefix='/api', tags=['APIs'])
templates = Jinja2Templates(directory='templates')

class EmailSigninRequest(BaseModel):
    #TODO: Modify this
    email: str
    verify_code: int

# sign in api
@router.post('/signin')
async def sign_in(request: Request, signin_request: EmailSigninRequest):
    # check signup_request's format (regex)

    # check whether the account exist
    # if not exist
    #     raise HTTPException()

    response_content = {}
    response_content = jsonable_encoder(response_content)
    return JSONResponse(response_content)
    
from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import model

router = APIRouter(prefix='/api', tags=['APIs'])
templates = Jinja2Templates(directory='templates')

class SigninRequest(BaseModel):
    #TODO: Modify this
    name: str
    email: str

# sign in api
@router.post('/signin')
async def sign_in(request: Request, signin_request: SigninRequest):
    # check signup_request's format (regex)

    # check whether the account exist
    response_content = {}
    response_content = jsonable_encoder(response_content)
    return JSONResponse(response_content)
    
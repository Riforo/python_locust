from typing import Optional

from pydantic import BaseModel

class ParamResp(BaseModel):
    code: str

class MainResponse(BaseModel):
    param: Optional[ParamResp]
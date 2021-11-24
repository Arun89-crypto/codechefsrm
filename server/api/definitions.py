from pydantic import BaseModel, constr


class ContactUsSchema(BaseModel):
    class Config:
        extra = "forbid"

    name: str
    email: constr(regex="(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    query: constr(min_length=30, strip_whitespace=True)


class AdminRegister(BaseModel):
    class Config:
        extra = "forbid"

    name: str
    email: constr(regex="(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    web_hook: constr(strip_whitespace=True)

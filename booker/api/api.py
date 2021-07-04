from fastapi import APIRouter

from booker.api.fundamentals import basic_authentication, cookies

api_router = APIRouter()

api_router.include_router(router=basic_authentication.router,
                          tags=["Basic auth example"])
api_router.include_router(router=cookies.router,
                          tags=["Cookies"])

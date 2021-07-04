"""
-- For Development Purposes --
Serves all all api challenges and training materials
Look out for auth clashes and multiple cookies
"""
from fastapi import FastAPI

from booker.api.api import api_router
app = FastAPI(
    title='Voyage Armada - Interstellar Hyperspace Communicaton Hub',
    description="The Spice expands consciousness, The Spice extends life, The Spice must flow!!!",
    version="1.0",
    docs_url="/",
    redoc_url=None
)

#TODO
# create source- destination objects and dicts - x,y coordinates to calculate distances
# create price calculator (distance, number of tickets, adults/kids luggage options)
# create admin panel with hardcoded credentails: AirfleetMarshall:GrandMoffTarkin
# create user registration/login via basicauth / session cookies
# crud for tickets / adding destinations / planes

#create
app.include_router(api_router, prefix='/api')

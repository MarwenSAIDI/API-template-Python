from app.v1.routers import heroRouter
from app.dependencies import SQLModel, engine
from fastapi import FastAPI

def create_app():
    """
    API app creation function
    """
    app_ = FastAPI(title="API template", version="1.0")

    
    SQLModel.metadata.create_all(engine)

    # Include the routes
    app_.include_router(heroRouter.router, prefix="/api/v1")

    return app_

app = create_app()
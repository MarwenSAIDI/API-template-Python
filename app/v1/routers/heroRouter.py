""" The hero router file"""
from fastapi import Depends, APIRouter, HTTPException
from app.dependencies import get_session, Session
from app.v1.schemas.hero import Hero, List
from app.v1.services.heroServices import (
    addHero,
    deleteHero,
    updateHero,
    getAllHeros,
    getHero,
)

router = APIRouter(
    prefix='/heroes',
    tags=['Heroes']
)

# Add hero to the database
@router.post('/', response_model=Hero)
def create_hero(hero: Hero, session: Session = Depends(get_session)) -> Hero:
    return addHero(hero, session)

# Get all the heroes
@router.get('/', response_model=List[Hero])
def read_heroes(
        skip: int = 0,
        limit: int = 10,
        session: Session = Depends(get_session),
) -> List[Hero]:
    
    return getAllHeros(skip, limit, session)

# Get a specific hero
@router.get('/{hero_id}', response_model=Hero)
def read_hero(hero_id: int, session: Session = Depends(get_session)) -> Hero:
    hero  = getHero(hero_id, session)

    if not hero:
        raise HTTPException(status_code=404, detail='Hero not found')
    return hero

# Update the hero
@router.put('/{hero_id}', response_model=Hero)
def update_hero(
        hero_id: int,
        hero_data: Hero,
        session: Session = Depends(get_session)
    ) -> Hero:

    hero  = getHero(hero_id, session)

    if not hero:
        raise HTTPException(status_code=404, detail='Hero not found')
    
    return updateHero(hero, hero_data, session)

# Delete the hero
@router.delete('/{hero_id}', response_model=Hero)
def delete_hero(
        hero_id: int,
        session: Session = Depends(get_session)
    ) -> Hero:

    hero  = getHero(hero_id, session)
    if not hero:
        raise HTTPException(status_code=404, detail='Hero not found')
    
    return deleteHero(hero, session)

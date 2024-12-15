from app.v1.schemas.hero import Hero
from app.dependencies import Session, select
from typing import List

def addHero(hero: Hero, session: Session) -> Hero:
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero

def deleteHero(hero: Hero, session: Session) -> Hero:

    session.delete(hero)
    session.commit()
    return hero

def updateHero(old_hero: Hero, new_hero: Hero , session: Session) -> Hero:
    
    # Update the heros values
    for field, value in new_hero.model_dump().items():
        setattr(old_hero, field, value)

    session.commit()
    session.refresh(old_hero)
    return new_hero

def getAllHeros(
        skip: int,
        limit: int,
        session: Session,
) -> List[Hero]:
    
    heroes = session.exec(select(Hero).offset(skip).limit(limit)).all()
    return heroes

def getHero(hero_id: int, session: Session):
    return session.get(Hero, hero_id)
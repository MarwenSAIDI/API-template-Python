"""Holds the object architecture"""
from typing import List, Optional
from sqlmodel import Field, SQLModel

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(
        title='ID',
        description='The identifier of the hero',
        primary_key=True,
        index=True,
    )

    name: str = Field(
        title='Name',
        description='The crime fighter name',
    )

    secret_name: str = Field(
        title='Secret name',
        description='The real name of the hero',
    )

    super_powers: str = Field(
        title='Super power',
        description="The heros' super power",
    )
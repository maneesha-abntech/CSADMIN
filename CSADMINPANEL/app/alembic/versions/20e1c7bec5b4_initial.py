"""initial

Revision ID: 20e1c7bec5b4
Revises: 
Create Date: 2024-05-09 00:47:43.438122

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20e1c7bec5b4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('firstname', sa.String),
        sa.Column('lastname', sa.String),
        sa.Column('phone_no', sa.String),
        sa.Column('email', sa.String, unique=True, index=True),
        sa.Column('password', sa.String)
    )



def downgrade() -> None:
    pass

"""add_qualification column

Revision ID: 7fe3347721cc
Revises: 20e1c7bec5b4
Create Date: 2024-05-10 17:18:32.331911

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7fe3347721cc'
down_revision: Union[str, None] = '20e1c7bec5b4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    # Add the new column using SQLAlchemy's `add_column()` method
    op.add_column('users', sa.Column('qualification', sa.String(length=100), nullable=True))

# If necessary, you can also define the downgrade() function to revert the changes made by the upgrade() function.

def downgrade() -> None:
    pass

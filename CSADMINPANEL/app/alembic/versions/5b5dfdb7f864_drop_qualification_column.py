"""drop qualification_column

Revision ID: 5b5dfdb7f864
Revises: 7fe3347721cc
Create Date: 2024-05-14 17:58:32.223761

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5b5dfdb7f864'
down_revision: Union[str, None] = '7fe3347721cc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Drop the qualification column from the User table
    op.drop_column('users', 'qualification')


def downgrade() -> None:
    pass

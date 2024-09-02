"""empty message

Revision ID: 8d026c9de41c
Revises: 9abd8cced541
Create Date: 2024-08-30 12:14:59.201777

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8d026c9de41c'
down_revision: Union[str, None] = '9abd8cced541'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

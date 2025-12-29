"""add column

Revision ID: 7a5c6796561a
Revises: 2f3828f4034b
Create Date: 2025-12-29 14:17:46.047129

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7a5c6796561a'
down_revision: Union[str, Sequence[str], None] = '2f3828f4034b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

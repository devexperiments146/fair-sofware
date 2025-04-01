"""add side to table

Revision ID: 4cf117674969
Revises: 32dbd32e45a3
Create Date: 2025-03-10 21:12:48.049968

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4cf117674969'
down_revision: Union[str, None] = '32dbd32e45a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("table") as batch_op:
        batch_op.add_column(sa.Column('side', sa.String(5), nullable=True))
    pass


def downgrade() -> None:
    with op.batch_alter_table("table") as batch_op:
        batch_op.drop_column('side')
    pass
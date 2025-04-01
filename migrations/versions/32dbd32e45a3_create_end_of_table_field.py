"""create end of table field

Revision ID: 32dbd32e45a3
Revises: e7de2ad80d86
Create Date: 2025-02-25 22:11:02.744111

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '32dbd32e45a3'
down_revision: Union[str, None] = 'e7de2ad80d86'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("exponent") as batch_op:
        batch_op.add_column(sa.Column('end_of_table', sa.Boolean, nullable=True))
    pass


def downgrade() -> None:
    with op.batch_alter_table("exponent") as batch_op:
        batch_op.drop_column('end_of_table')
    pass

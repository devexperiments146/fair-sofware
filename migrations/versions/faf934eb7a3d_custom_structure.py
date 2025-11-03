"""custom structure

Revision ID: faf934eb7a3d
Revises: 4cf117674969
Create Date: 2025-11-02 22:00:35.864826

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'faf934eb7a3d'
down_revision: Union[str, None] = '4cf117674969'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:  
    with op.batch_alter_table("structure") as batch_op:
        batch_op.add_column(sa.Column('structure_type', sa.Integer, nullable=False, server_default='0'))
    pass


def downgrade() -> None:
    with op.batch_alter_table("structure") as batch_op:
        batch_op.drop_column('structure_type')
    pass

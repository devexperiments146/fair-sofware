"""add position table line position

Revision ID: e7de2ad80d86
Revises: 
Create Date: 2025-02-18 13:31:05.549487

"""
from typing import Sequence, Union

from sqlalchemy.orm import mapped_column
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e7de2ad80d86'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("exponent") as batch_op:
        batch_op.add_column(sa.Column('table_line_choice_id', sa.Integer, nullable=True))
        batch_op.create_foreign_key(batch_op.f("fk_exponent_table_line_choice_id_table_line"),'table_line',['table_line_choice_id'],['id'])
        batch_op.add_column(sa.Column('table_line_position', sa.Integer, nullable=True))
    pass


def downgrade() -> None:
    with op.batch_alter_table("exponent") as batch_op:
        batch_op.drop_constraint(batch_op.f("fk_exponent_table_line_choice_id_table_line"),type_="foreignkey")
        batch_op.drop_column('table_line_choice_id')
        batch_op.drop_column('table_line_position')
    pass

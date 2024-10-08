"""empty message

Revision ID: 179d093450b8
Revises: 2bf33901bee8
Create Date: 2024-09-27 11:10:41.832870

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '179d093450b8'
down_revision: Union[str, None] = '2bf33901bee8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notice', sa.Column('notice_type', sa.String(), nullable=False))
    op.drop_column('notice', 'noticeType')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notice', sa.Column('noticeType', sa.VARCHAR(), nullable=False))
    op.drop_column('notice', 'notice_type')
    # ### end Alembic commands ###

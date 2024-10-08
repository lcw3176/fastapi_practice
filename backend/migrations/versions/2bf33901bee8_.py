"""empty message

Revision ID: 2bf33901bee8
Revises: 
Create Date: 2024-09-26 16:14:10.570724

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2bf33901bee8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('writer', sa.String(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('notice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('noticeType', sa.String(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('writer', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('commentCount', sa.Integer(), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    op.drop_table('notice')
    op.drop_table('comment')
    # ### end Alembic commands ###

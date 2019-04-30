"""Preferences

Revision ID: 40691992564a
Revises: 19a697956fb1
Create Date: 2019-04-24 18:58:37.302128

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40691992564a'
down_revision = '19a697956fb1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('preference',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('pair1', sa.String(length=7), nullable=True),
    sa.Column('pair2', sa.String(length=7), nullable=True),
    sa.Column('pair3', sa.String(length=7), nullable=True),
    sa.Column('pair4', sa.String(length=7), nullable=True),
    sa.Column('pair5', sa.String(length=7), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('preference')
    # ### end Alembic commands ###

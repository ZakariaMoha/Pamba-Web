"""empty message

Revision ID: 0fd38ca80f3a
Revises: 88d65b7162e3
Create Date: 2024-03-15 19:56:20.031363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fd38ca80f3a'
down_revision = '88d65b7162e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('businesses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('active', sa.Boolean(), nullable=True))
        batch_op.drop_column('status')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('businesses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
        batch_op.drop_column('active')

    # ### end Alembic commands ###

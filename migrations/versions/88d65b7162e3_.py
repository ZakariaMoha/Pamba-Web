"""empty message

Revision ID: 88d65b7162e3
Revises: e3c22ef112b5
Create Date: 2024-03-15 18:33:34.793016

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88d65b7162e3'
down_revision = 'e3c22ef112b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('businesses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category', sa.String(length=15), nullable=False))
        batch_op.alter_column('google_map',
               existing_type=sa.VARCHAR(length=300),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('businesses', schema=None) as batch_op:
        batch_op.alter_column('google_map',
               existing_type=sa.VARCHAR(length=300),
               nullable=False)
        batch_op.drop_column('category')

    # ### end Alembic commands ###

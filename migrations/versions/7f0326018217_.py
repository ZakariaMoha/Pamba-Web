"""empty message

Revision ID: 7f0326018217
Revises: 4f7db4481420
Create Date: 2024-04-29 13:47:16.148033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f0326018217'
down_revision = '4f7db4481420'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('businesses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('weekend_opening', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('weekend_closing', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('weekday_opening', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('weekday_closing', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('businesses', schema=None) as batch_op:
        batch_op.drop_column('weekday_closing')
        batch_op.drop_column('weekday_opening')
        batch_op.drop_column('weekend_closing')
        batch_op.drop_column('weekend_opening')

    # ### end Alembic commands ###

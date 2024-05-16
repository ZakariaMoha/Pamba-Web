"""empty message

Revision ID: 186b6377eeff
Revises: 6239e4a6e89e
Create Date: 2024-05-16 20:22:05.000582

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '186b6377eeff'
down_revision = '6239e4a6e89e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('businesses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rating', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('businesses', schema=None) as batch_op:
        batch_op.drop_column('rating')

    # ### end Alembic commands ###

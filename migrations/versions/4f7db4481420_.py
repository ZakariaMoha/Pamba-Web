"""empty message

Revision ID: 4f7db4481420
Revises: 00b35a9d0d9b
Create Date: 2024-04-29 11:29:05.257841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f7db4481420'
down_revision = '00b35a9d0d9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('services_businesses_association', schema=None) as batch_op:
        batch_op.add_column(sa.Column('specific_service', sa.String(length=100), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('services_businesses_association', schema=None) as batch_op:
        batch_op.drop_column('specific_service')

    # ### end Alembic commands ###

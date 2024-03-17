"""empty message

Revision ID: 6ed8aeb8a14f
Revises: 30e7e0e91218
Create Date: 2024-03-17 02:48:22.701478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ed8aeb8a14f'
down_revision = '30e7e0e91218'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('services', schema=None) as batch_op:
        batch_op.drop_constraint('services_business_id_fkey', type_='foreignkey')
        batch_op.drop_column('business_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('services', schema=None) as batch_op:
        batch_op.add_column(sa.Column('business_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('services_business_id_fkey', 'businesses', ['business_id'], ['id'])

    # ### end Alembic commands ###

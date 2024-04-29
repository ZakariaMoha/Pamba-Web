"""empty message

Revision ID: 5cd430332515
Revises: 2c1e98095e7f
Create Date: 2024-04-29 15:06:23.446313

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5cd430332515'
down_revision = '2c1e98095e7f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('services', schema=None) as batch_op:
        batch_op.add_column(sa.Column('business_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('service_category', sa.Integer(), nullable=True))
        batch_op.drop_constraint('services_category_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'service_categories', ['service_category'], ['id'], ondelete='SET NULL')
        batch_op.create_foreign_key(None, 'businesses', ['business_id'], ['id'])
        batch_op.drop_column('category')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('services', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('services_category_fkey', 'service_categories', ['category'], ['id'], ondelete='SET NULL')
        batch_op.drop_column('service_category')
        batch_op.drop_column('business_id')

    # ### end Alembic commands ###

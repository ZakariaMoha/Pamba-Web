"""empty message

Revision ID: a767b42f5bb1
Revises: 5cd430332515
Create Date: 2024-04-29 18:34:34.995170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a767b42f5bb1'
down_revision = '5cd430332515'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('businesses', schema=None) as batch_op:
        batch_op.drop_column('average_rating')

    with op.batch_alter_table('clients', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=300),
               nullable=True)

    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.add_column(sa.Column('appointment_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'appointments', ['appointment_id'], ['id'])

    with op.batch_alter_table('services', schema=None) as batch_op:
        batch_op.add_column(sa.Column('estimated_service_time', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('services', schema=None) as batch_op:
        batch_op.drop_column('estimated_service_time')

    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('appointment_id')

    with op.batch_alter_table('clients', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=300),
               nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)

    with op.batch_alter_table('businesses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('average_rating', sa.INTEGER(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###

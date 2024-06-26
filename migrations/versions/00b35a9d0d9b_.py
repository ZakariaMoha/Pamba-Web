"""empty message

Revision ID: 00b35a9d0d9b
Revises: e2b8455583ef
Create Date: 2024-04-26 20:42:53.403515

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00b35a9d0d9b'
down_revision = 'e2b8455583ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('businesses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('parent_id', sa.Integer(), nullable=True))
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.create_foreign_key(None, 'businesses', ['parent_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('businesses', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.drop_column('parent_id')

    # ### end Alembic commands ###

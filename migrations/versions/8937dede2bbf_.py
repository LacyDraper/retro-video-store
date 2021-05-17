"""empty message

Revision ID: 8937dede2bbf
Revises: 8cd7d3f680fc
Create Date: 2021-05-17 11:17:55.615200

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8937dede2bbf'
down_revision = '8cd7d3f680fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('phone', sa.String(), nullable=False))
    op.add_column('customer', sa.Column('registered_at', sa.DateTime(), nullable=True))
    op.drop_column('customer', 'phone_number')
    op.drop_column('customer', 'register_at')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('register_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('customer', sa.Column('phone_number', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('customer', 'registered_at')
    op.drop_column('customer', 'phone')
    # ### end Alembic commands ###

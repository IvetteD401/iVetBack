"""empty message

Revision ID: fe3da0d6a7e0
Revises: 61baa44ab81e
Create Date: 2020-02-11 22:49:07.976526

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fe3da0d6a7e0'
down_revision = '61baa44ab81e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('general_records', sa.Column('caregiver', sa.String(length=100), nullable=False))
    op.drop_column('general_records', 'cargiver')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('general_records', sa.Column('cargiver', mysql.VARCHAR(length=100), nullable=False))
    op.drop_column('general_records', 'caregiver')
    # ### end Alembic commands ###

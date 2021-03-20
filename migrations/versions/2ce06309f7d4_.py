"""empty message

Revision ID: 2ce06309f7d4
Revises: fe3da0d6a7e0
Create Date: 2020-02-12 16:59:38.701848

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2ce06309f7d4'
down_revision = 'fe3da0d6a7e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('insurance_policy', table_name='general_records')
    op.drop_column('general_records', 'groomer_address')
    op.drop_column('general_records', 'vet_address')
    op.drop_column('general_records', 'insurance_provider')
    op.drop_column('general_records', 'insurance_policy')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('general_records', sa.Column('insurance_policy', mysql.VARCHAR(length=120), nullable=False))
    op.add_column('general_records', sa.Column('insurance_provider', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.add_column('general_records', sa.Column('vet_address', mysql.VARCHAR(length=120), nullable=False))
    op.add_column('general_records', sa.Column('groomer_address', mysql.VARCHAR(length=120), nullable=False))
    op.create_index('insurance_policy', 'general_records', ['insurance_policy'], unique=True)
    # ### end Alembic commands ###
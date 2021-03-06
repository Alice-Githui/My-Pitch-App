"""Add passwords to the user class

Revision ID: 08cf5ad95b96
Revises: 66d8c3fa6425
Create Date: 2021-04-24 11:34:40.099555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08cf5ad95b96'
down_revision = '66d8c3fa6425'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###

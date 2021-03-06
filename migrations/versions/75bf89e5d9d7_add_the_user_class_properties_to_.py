"""Add the user class properties to include a profile picture

Revision ID: 75bf89e5d9d7
Revises: e06b1693ccf5
Create Date: 2021-04-24 15:25:43.803602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75bf89e5d9d7'
down_revision = 'e06b1693ccf5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    # ### end Alembic commands ###

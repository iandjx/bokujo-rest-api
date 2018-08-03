"""added current pen to cowmodel

Revision ID: 5840bdd194a5
Revises: 4264c1fb198c
Create Date: 2018-08-03 23:37:06.573928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5840bdd194a5'
down_revision = '4264c1fb198c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cows', sa.Column('current_pen', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cows', 'current_pen')
    # ### end Alembic commands ###

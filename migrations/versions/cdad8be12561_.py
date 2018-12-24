"""empty message

Revision ID: cdad8be12561
Revises: 515cd21af8a5
Create Date: 2018-12-25 00:11:57.538024

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'cdad8be12561'
down_revision = '515cd21af8a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('problems')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('problems',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('date_diagnosed', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('date_treated', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('date_cured', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('problem_type', sa.VARCHAR(length=32), autoincrement=False, nullable=False),
    sa.Column('cow_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['cow_id'], ['cows.id'], name='problems_cow_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='problems_pkey')
    )
    # ### end Alembic commands ###

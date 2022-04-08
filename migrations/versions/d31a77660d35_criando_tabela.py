"""criando tabela

Revision ID: d31a77660d35
Revises: 
Create Date: 2022-04-08 11:28:07.943740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd31a77660d35'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('leads',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('creation_date', sa.String(), nullable=True),
    sa.Column('last_visit', sa.String(), nullable=True),
    sa.Column('visits', sa.Integer(), nullable=True),
    sa.CheckConstraint("phone ~ '^\\([1-9]{2}\\)[0-9]{5}\\-[0-9]{4}$'"),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('leads')
    # ### end Alembic commands ###

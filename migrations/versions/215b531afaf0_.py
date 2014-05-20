"""empty message

Revision ID: 215b531afaf0
Revises: None
Create Date: 2014-05-20 02:37:07.668295

"""

# revision identifiers, used by Alembic.
revision = '215b531afaf0'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shift',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time_in', sa.DateTime(), nullable=False),
    sa.Column('time_out', sa.DateTime(), nullable=True),
    sa.Column('project', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shift')
    ### end Alembic commands ###
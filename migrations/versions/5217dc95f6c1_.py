"""empty message

Revision ID: 5217dc95f6c1
Revises: 372402b69254
Create Date: 2015-01-22 14:48:10.419000

"""

# revision identifiers, used by Alembic.
revision = '5217dc95f6c1'
down_revision = '372402b69254'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('category_name', sa.String(length=120), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'category_name')
    ### end Alembic commands ###
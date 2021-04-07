"""empty message

Revision ID: b886fb3fb1cc
Revises: 7a9730258c78
Create Date: 2021-04-07 17:05:41.586140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b886fb3fb1cc'
down_revision = '7a9730258c78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('parent', sa.Column('mother_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'parent', 'person', ['mother_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'parent', type_='foreignkey')
    op.drop_column('parent', 'mother_id')
    # ### end Alembic commands ###

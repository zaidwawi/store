"""empty message

Revision ID: f475d9b3880e
Revises: 9b036776f1a3
Create Date: 2022-01-30 20:58:01.532515

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f475d9b3880e'
down_revision = '9b036776f1a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('checkout_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'order', 'checkout', ['checkout_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'order', type_='foreignkey')
    op.drop_column('order', 'checkout_id')
    # ### end Alembic commands ###

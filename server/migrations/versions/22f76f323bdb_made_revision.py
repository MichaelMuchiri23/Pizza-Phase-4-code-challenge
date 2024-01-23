"""Made revision

Revision ID: 22f76f323bdb
Revises: 966650047e8c
Create Date: 2024-01-23 10:19:27.033205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22f76f323bdb'
down_revision = '966650047e8c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurants', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address', sa.String(length=100), nullable=False))
        batch_op.drop_column('location')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurants', schema=None) as batch_op:
        batch_op.add_column(sa.Column('location', sa.VARCHAR(length=100), nullable=False))
        batch_op.drop_column('address')

    # ### end Alembic commands ###

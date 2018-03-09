"""Add a column

Revision ID: 35a2eeb252d0
Revises: 4f1960e78fb0
Create Date: 2018-03-10 00:42:00.448950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35a2eeb252d0'
down_revision = '4f1960e78fb0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account', sa.Column('updated_at', sa.DateTime))


def downgrade():
    op.drop_column('account', 'updated_at')

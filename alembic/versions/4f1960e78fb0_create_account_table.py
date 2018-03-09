"""create account table

Revision ID: 4f1960e78fb0
Revises:
Create Date: 2018-03-09 23:51:43.787055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f1960e78fb0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account',
        sa.Column('id',    sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name',  sa.String),
        sa.Column('email', sa.String,  nullable=False),
    )

def downgrade():
    op.drop_table('account')


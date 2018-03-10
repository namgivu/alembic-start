"""raw sql trial

Revision ID: ac2562bd9ae4
Revises: 35a2eeb252d0
Create Date: 2018-03-10 08:51:25.413245

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'ac2562bd9ae4'
down_revision = '35a2eeb252d0'
branch_labels = None
depends_on = None


def upgrade():
    sql_up = '''
    ALTER TABLE account DROP COLUMN updated_at;
    '''
    c=op.get_bind(); c.execute(sql_up) #ref. https://www.johbo.com/2016/data-migrations-with-alembic-plain-sql.html


def downgrade():
    sql_down = '''
    ALTER TABLE account ADD COLUMN updated_at TIMESTAMP;
    '''
    c=op.get_bind(); c.execute(sql_down) #ref. https://www.johbo.com/2016/data-migrations-with-alembic-plain-sql.html

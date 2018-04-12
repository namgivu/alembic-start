"""branch01

Revision ID: 8b07f0efc9db
Revises: ac2562bd9ae4
Create Date: 2018-04-12 23:43:43.159756

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b07f0efc9db'
down_revision = 'ac2562bd9ae4'
branch_labels = None
depends_on = None


def upgrade():
    sql_up = '''
    ALTER TABLE account ADD COLUMN branch01 INT;
    '''
    c=op.get_bind(); c.execute(sql_up) #ref. https://www.johbo.com/2016/data-migrations-with-alembic-plain-sql.html


def downgrade():
    sql_down = '''
    ALTER TABLE account DROP COLUMN branch01;
    '''
    c=op.get_bind(); c.execute(sql_down) #ref. https://www.johbo.com/2016/data-migrations-with-alembic-plain-sql.html

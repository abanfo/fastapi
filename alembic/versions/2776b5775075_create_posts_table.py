"""create posts table

Revision ID: 2776b5775075
Revises: 
Create Date: 2023-07-26 15:10:09.115198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2776b5775075'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',sa.Column('id', sa.Integer,primary_key=True,nullable = False),
                            sa.Column('title',sa.String,nullable=False))
    pass



def downgrade() -> None:
    op.drop_table('posts', cascade=True)
    pass

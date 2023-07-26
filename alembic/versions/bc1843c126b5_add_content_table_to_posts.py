"""Add content table to posts

Revision ID: bc1843c126b5
Revises: 2776b5775075
Create Date: 2023-07-26 19:10:17.273702

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc1843c126b5'
down_revision = '2776b5775075'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String,nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass

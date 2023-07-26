"""Add foreign-key to the posts table

Revision ID: 846f742aa482
Revises: c0eb0abc1cdd
Create Date: 2023-07-26 19:40:22.404035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '846f742aa482'
down_revision = 'c0eb0abc1cdd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',
                  sa.Column('owner_id',sa.Integer,nullable=False))
    op.create_foreign_key('post_users_fk',source_table='posts',referent_table='users',
    local_cols=['owner_id'],remote_cols=['id'],ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk',table_name='posts')
    op.drop_column('posts','owner_id')
    pass

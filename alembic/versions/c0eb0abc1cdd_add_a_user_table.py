"""Add a user table

Revision ID: c0eb0abc1cdd
Revises: bc1843c126b5
Create Date: 2023-07-26 19:22:11.130025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0eb0abc1cdd'
down_revision = 'bc1843c126b5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id',sa.Integer,nullable=False),
                    sa.Column('email',sa.String,nullable=False),
                    sa.Column('password',sa.String,nullable=False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass

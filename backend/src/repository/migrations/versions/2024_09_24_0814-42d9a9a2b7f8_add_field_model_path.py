"""Add field model path

Revision ID: 42d9a9a2b7f8
Revises: 60d1844cb5d3
Create Date: 2024-09-24 08:14:19.413719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42d9a9a2b7f8'
down_revision = '60d1844cb5d3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('model', sa.Column('path', sa.String))


def downgrade() -> None:
    op.drop_column('model', 'path')

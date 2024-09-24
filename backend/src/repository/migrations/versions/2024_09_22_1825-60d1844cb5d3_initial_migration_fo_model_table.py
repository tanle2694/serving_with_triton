"""initial migration for account table

Revision ID: 60d1844cb5d3
Revises:
Create Date: 2022-12-09 18:25:25.301186

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.schema import Table

# revision identifiers, used by Alembic.
revision = "60d1844cb5d3"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Define the table
    model_table = Table(
        "model",
        sa.MetaData(),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=64), nullable=False),
        sa.Column("type", sa.String(length=64), nullable=False),
        sa.Column("description", sa.String(length=1024), nullable=True),
        sa.Column("status", sa.String(length=64), nullable=False),
        sa.Column("last_active", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("is_deleted", sa.Boolean(), nullable=False, server_default=sa.text('false')),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )

    # Create the table if it doesn't exist
    model_table.create(op.get_bind(), checkfirst=True)

def downgrade() -> None:
    # Drop the table if it exists
    op.drop_table("model", if_exists=True)
"""Add isbn13 to books

Revision ID: f2e1d6538e26
Revises: 160a88161427
Create Date: 2022-04-22 22:54:23.839429

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "f2e1d6538e26"
down_revision = "160a88161427"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("books", sa.Column("isbn13", sa.String(length=13), nullable=True))


def downgrade():
    op.drop_column("books", "isbn13")

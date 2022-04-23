"""Add the books table

Revision ID: 160a88161427
Revises: 830b301dfe1d
Create Date: 2022-04-22 21:00:01.846717

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy_utils import UUIDType

# revision identifiers, used by Alembic.
revision = "160a88161427"
down_revision = "830b301dfe1d"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "books",
        sa.Column("id", UUIDType(), nullable=False),
        sa.Column("title", sa.String(100), nullable=False),
        sa.Column("description", sa.String(255), nullable=True),
        sa.Column("author_id", UUIDType(), nullable=False),
        sa.ForeignKeyConstraint(["author_id"], ["authors.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_books_title"), "books", ["title"], unique=False)


def downgrade():
    op.drop_index(op.f("ix_books_title"), table_name="books")
    op.drop_table("books")

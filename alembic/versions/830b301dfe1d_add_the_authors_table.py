"""Add the authors table

Revision ID: 830b301dfe1d
Revises: 
Create Date: 2022-04-22 20:57:08.750821

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy_utils import UUIDType

# revision identifiers, used by Alembic.
revision = "830b301dfe1d"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "authors",
        sa.Column("id", UUIDType(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_authors_name"), "authors", ["name"], unique=False)


def downgrade():
    op.drop_index(op.f("ix_authors_name"), table_name="authors")
    op.drop_table("authors")

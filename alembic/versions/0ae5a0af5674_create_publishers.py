"""Create publishers

Revision ID: 0ae5a0af5674
Revises: f2e1d6538e26
Create Date: 2022-04-22 23:01:24.426025

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy_utils import UUIDType

# revision identifiers, used by Alembic.
revision = "0ae5a0af5674"
down_revision = "f2e1d6538e26"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "publishers",
        sa.Column("id", UUIDType(), nullable=False),
        sa.Column("name", sa.String(100), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_publishers_name"), "publishers", ["name"], unique=False)

    op.add_column("books", sa.Column("publisher_id", UUIDType(), nullable=True))
    op.create_foreign_key(None, "books", "publishers", ["publisher_id"], ["id"])


def downgrade():
    op.drop_constraint("books_publisher_id_fkey", "books", type_="foreignkey")
    op.drop_column("books", "publisher_id")

    op.drop_index(op.f("ix_publishers_name"), table_name="publishers")
    op.drop_table("publishers")

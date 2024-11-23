"""init

Revision ID: 0001
Revises: 
Create Date: 2024-11-23 03:10:51.882350

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "open_ports",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("ip", sa.String(length=16), nullable=False),
        sa.Column("port", sa.Integer(), nullable=False),
        sa.Column("type", sa.String(length=36), nullable=False),
        sa.Column("protocol", sa.String(length=36), nullable=False),
        sa.Column("service", sa.String(length=256), nullable=False),
        sa.Column("version", sa.String(length=128), nullable=False),
        sa.PrimaryKeyConstraint("id", "ip", "port", name=op.f("pk_open_ports")),
    )
    op.create_table(
        "scan_results",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("ip", sa.String(length=16), nullable=False),
        sa.Column("ptr_record", sa.String(length=1024), nullable=True),
        sa.Column("severity", sa.String(length=1024), nullable=True),
        sa.PrimaryKeyConstraint("id", "ip", name=op.f("pk_scan_results")),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("scan_results")
    op.drop_table("open_ports")
    # ### end Alembic commands ###

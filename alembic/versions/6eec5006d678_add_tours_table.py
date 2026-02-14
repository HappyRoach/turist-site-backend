"""add tours table

Revision ID: add_tours_001
Revises: ee80889cd9c0
Create Date: 2026-02-14 18:15:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa



revision: str = 'add_tours_001'
down_revision: Union[str, None] = 'ee80889cd9c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('tours',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('country', sa.String(length=100), nullable=True),
    sa.Column('city', sa.String(length=100), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('operator', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('image_url', sa.String(length=500), nullable=True),
    sa.Column('external_url', sa.String(length=500), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tours_id'), 'tours', ['id'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_tours_id'), table_name='tours')
    op.drop_table('tours')
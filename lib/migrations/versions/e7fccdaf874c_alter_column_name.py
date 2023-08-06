"""Alter column name

Revision ID: e7fccdaf874c
Revises: 57f10ba98be0
Create Date: 2023-08-06 13:43:05.445205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7fccdaf874c'
down_revision = '57f10ba98be0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars', 'email', new_column_name='mail')


def downgrade() -> None:
    op.alter_column('scholars', 'mail', new_column_name='email')

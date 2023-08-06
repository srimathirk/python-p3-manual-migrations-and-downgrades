"""Renaming students to scholars

Revision ID: 57f10ba98be0
Revises: 791279dd0760
Create Date: 2023-08-06 13:27:15.364979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57f10ba98be0'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students','scholars')


def downgrade() -> None:
    op.rename_table('scholars','students')

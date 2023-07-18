"""sqlite_miggration

Revision ID: e4af30e10a19
Revises: 
Create Date: 2023-07-18 13:47:32.121362

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4af30e10a19'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('strava_activities',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('strava_activities')
    # ### end Alembic commands ###
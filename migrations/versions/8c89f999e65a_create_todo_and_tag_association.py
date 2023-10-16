"""create todo and tag association

Revision ID: 8c89f999e65a
Revises: c17e0caaf823
Create Date: 2023-10-13 17:25:03.487220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c89f999e65a'
down_revision = 'c17e0caaf823'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo_and_tag',
    sa.Column('todo_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ),
    sa.ForeignKeyConstraint(['todo_id'], ['todo.id'], ),
    sa.PrimaryKeyConstraint('todo_id', 'tag_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todo_and_tag')
    # ### end Alembic commands ###

import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import models
from models import Base

# this Alembic Config object provides access to the .ini file values
config = context.config

# Load DB URL from env (Render -> Environment)
db_url = os.environ.get("DATABASE_URL", "")

# Normalize for SQLAlchemy driver + optional SSL
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql+psycopg2://", 1)
if "render.internal" not in db_url and "sslmode" not in db_url:
    db_url += ("&" if "?" in db_url else "?") + "sslmode=require"

# Push into alembic config so both offline/online modes use it
if db_url:
    config.set_main_option("sqlalchemy.url", db_url)

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()





from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# --- START: AiTuki Configuration ---
# 1. Import your database URL from your main database.py file.
#    This ensures Alembic uses the same connection string as your app.
from database import SQLALCHEMY_DATABASE_URL

# 2. Import your Base model from your models.py file so Alembic knows about your tables.
import models
from models import Base
# --- END: AiTuki Configuration ---

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# --- START: AiTuki Configuration ---
# 3. Set the SQLAlchemy URL in the config using the one from your database.py.
#    This makes database.py the single source of truth for the connection string.
config.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)
# --- END: AiTuki Configuration ---


# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# --- START: AiTuki Configuration ---
# 4. Tell Alembic that your models' metadata is the target for autogeneration.
target_metadata = models.Base.metadata
# --- END: AiTuki Configuration ---


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.QueuePool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()




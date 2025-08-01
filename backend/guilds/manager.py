from datetime import datetime

from sqlalchemy.orm import Session

from backend.core.database import engine
from backend.guilds.models import Guild
from backend.punishments.models import PunishmentConfig


def get_guild_by_id(guild_id: int):
    with Session(engine) as session:
        return session.query(Guild).filter_by(guild_id=guild_id).first()


def create_or_update_guild(guild_id: int, **kwargs):
    with Session(engine) as session:
        guild = session.query(Guild).filter_by(guild_id=guild_id).first()

        if not guild:
            guild = Guild(guild_id=guild_id, added_at=datetime.utcnow(), is_active=True)
            guild.punishment_config = PunishmentConfig(guild_id=guild_id)

        for field, value in kwargs.items():
            if value is not None and hasattr(guild, field):
                setattr(guild, field, value)

        session.add(guild)
        session.commit()
        session.refresh(guild)
        return guild

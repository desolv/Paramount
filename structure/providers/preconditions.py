from discord.ext import commands

from structure.providers.helper import load_json_data


def is_owner():
    return commands.is_owner()


def is_admin():
    async def predicate(ctx):
        if is_owner():
            return True

        return ctx.author.guild_permissions.administrator
    return commands.check(predicate)


def has_roles(name: str, sub: str = "_default"):
    async def predicate(ctx):
        if is_admin():
            return True

        command = load_json_data("permissions").get(name, {})
        role_ids = command.get(sub, [])
        user_role_ids = [role.id for role in ctx.author.roles]

        return any(x in role_ids for x in user_role_ids)
    return commands.check(predicate)




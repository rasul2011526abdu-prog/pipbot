from your_project import bot, permissions

@bot.command()
@permissions.is_admin()
async def warn(ctx, user: str, reason: str):
    await ctx.send(f'User {user} has been warned for: {reason}')

@bot.command()
@permissions.is_admin()
async def unwarn(ctx, user: str):
    await ctx.send(f'User {user} has had their warning removed.')

@bot.command()
@permissions.is_admin()
async def mute(ctx, user: str, time: str):
    await ctx.send(f'User {user} has been muted for {time}.')

@bot.command()
@permissions.is_admin()
async def unmute(ctx, user: str):
    await ctx.send(f'User {user} has been unmuted.')

@bot.command()
@permissions.is_admin()
async def ban(ctx, user: str):
    await ctx.send(f'User {user} has been banned.')

@bot.command()
@permissions.is_admin()
async def unban(ctx, user: str):
    await ctx.send(f'User {user} has been unbanned.')

@bot.command()
@permissions.is_admin()
async def stats(ctx):
    await ctx.send('Displaying server statistics...')

@bot.command()
@permissions.is_admin()
async def logs(ctx):
    await ctx.send('Displaying logs...')

import discord
from discord.ext import commands
import spotipy

bot = commands.Bot(command_prefix="+p")

# Initialize Spotify API
spotify_token = spotipy.oauth2.SpotifyClientCredentials(
    client_id="your client id", client_secret="your secreat id"
)
spotify = spotipy.Spotify(auth=spotify_token.get_access_token())

# Discord Bot function
@bot.command()
async def play(ctx, url: str):
    # check if url is spotify
     if "spotify" in url:
        # use spotify API to play the audio
        await ctx.send("Playing Audio from Spotify")
        await ctx.send("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
        # get track URI
        uri = url.split("track/")[-1]
        # get track info from spotify API
        track = spotify.track(uri)
        # extract track name and artist from track info
        name = track["name"]
        artist = track["artists"][0]["name"]
        # send playing message
        await ctx.send(f"Playing {name} by {artist}")
        await ctx.send("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")


# run the bot
bot.run("token")

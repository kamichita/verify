import os

BOTTOKEN = os.getenv("DISCORD_TOKEN")
CLIENT_ID = "1347091568552841226"
CLIENT_SECRET = "Cf3y2WcY4rJKtXfxE6LIYPKiuG1zTOiy"
REDIRECT_URI = "https://backup-production-0f5f.up.railway.app/"

usadata_path = "userdata.json"
serverdata_folder_path = "./server/"
authurl = "https://discord.com/oauth2/authorize?client_id=1347091568552841226&response_type=code&redirect_uri=https%3A%2F%2Fbackup-production-0f5f.up.railway.app%2F&scope=identify+guilds.join"

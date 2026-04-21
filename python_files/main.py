from env_config import load_env_variables
from apis.reddit_api import get_reddit_access_token
from discord_bot import SiphonBot

if __name__ == "__main__":
    env_vars = load_env_variables()

    print("Environment variables loaded successfully.")

    reddit_access_token = get_reddit_access_token(
        env_vars["REDDIT_CLIENT_ID"],
        env_vars["REDDIT_CLIENT_SECRET"],
        env_vars["REDDIT_USERNAME"],
        env_vars["REDDIT_PASSWORD"],
        env_vars["REDDIT_USER_AGENT"],
    )

    headers = {
        "Authorization": f"bearer {reddit_access_token}",
        "User-Agent": env_vars["REDDIT_USER_AGENT"],
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest",
    }

    bot = SiphonBot(env_vars["DISCORD_TOKEN"], env_vars["WEBHOOK"], headers)
    bot.run()

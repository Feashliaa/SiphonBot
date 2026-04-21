# SiphonBot

A Discord bot that grabs media from Reddit and YouTube and posts it directly into your server.

## What it does

- **Reddit scraping** - Pull images, videos, and GIFs from subreddits by filter (hot, new, top, rising)
- **Reddit links** - Paste any Reddit post URL and SiphonBot downloads and posts the media, including share links (`/s/` short URLs)
- **YouTube downloads** - Paste a YouTube URL and SiphonBot downloads the video and uploads it to Discord
- **Oversize handling** - Videos that exceed Discord's 50MB upload limit can be compressed (480p re-encode) or split into timestamped parts
- **NSFW tagging** - Reddit posts marked NSFW are automatically prefixed

## Commands

| Command                                                                  | Description                          |
| ------------------------------------------------------------------------ | ------------------------------------ |
| `/yt <url>`                                                              | Download a YouTube video and post it |
| `/reddit <url>`                                                          | Fetch media from a Reddit post URL   |
| `/scrape <subreddit_number> [num_posts] [filter_type] [time_range]`      | Scrape posts from a preset subreddit |
| `/scrape_custom <subreddit_name> [num_posts] [filter_type] [time_range]` | Scrape posts from any subreddit      |
| `/list_subreddits`                                                       | List preset subreddits               |

## YouTube size limits

Discord's upload limit is 50MB (Level 2 boost). When a video exceeds this, SiphonBot presents two options via buttons:

- **Compress** - Re-encodes at 480p with a calculated bitrate to fit under the limit. Only offered when the video is short enough for compression to produce a watchable result (≥500kbps video bitrate).
- **Split into parts** - Splits the video into chunks using stream copy (no quality loss). Each part is labeled with timestamps, e.g. `Video Title (Part 2/4 - 2:30–5:00)`.

## Setup

### Environment variables

Create a `.env` file in the project root:

```
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=your_user_agent
REDDIT_USERNAME=your_username
REDDIT_PASSWORD=your_password
DISCORD_TOKEN=your_discord_bot_token
WEBHOOK=your_discord_webhook_url
```

### Run with Docker

```bash
docker compose up -d --build
```

### View logs

```bash
docker logs -f reddit_scraper_bot
```

### Rebuild after changes

```bash
docker compose down
docker compose up -d --build
```

## Project structure

```
├── Dockerfile
├── docker-compose.yml
├── python_files/
│   ├── main.py                  # Entry point - loads env, authenticates Reddit, starts bot
│   ├── discord_bot.py           # Discord client, slash commands, command tree
│   ├── env_config.py            # Environment variable loader
│   ├── utils.py                 # Filename sanitization
│   ├── apis/
│   │   └── reddit_api.py        # Reddit OAuth token + subreddit validation
│   └── media/
│       ├── common.py            # Shared helpers - file send, cleanup, temp dirs
│       ├── reddit_handler.py    # Reddit media pipeline - images, videos, GIFs, galleries
│       └── youtube_handler.py   # YouTube download, compress, split pipeline
└── text_files/
    └── requirements.txt
```

## Dependencies

- [discord.py](https://discordpy.readthedocs.io/) - Discord bot framework
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - YouTube downloader
- [ffmpeg](https://ffmpeg.org/) - Video compression and splitting
- [aiohttp](https://docs.aiohttp.org/) - Async HTTP for Reddit API
- [python-dotenv](https://github.com/theskumar/python-dotenv) - Environment variable loading
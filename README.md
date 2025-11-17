# Discord Starboard - OBS Overlay

A Discord bot that monitors a channel for images and displays them as an overlay in OBS Studio. Perfect for showcasing community submissions, memes, or any images posted to your Discord channel in real-time.

## Features

- 🖼️ **Real-time Image Display**: Automatically detects and displays images posted to a Discord channel
- 🎨 **Discord-style UI**: Beautiful card-based overlay that matches Discord's aesthetic
- ⚡ **Automatic Updates**: Checks for new images and updates the overlay
- 🎬 **Smooth Animations**: Fade in/out transitions for professional-looking overlays
- 👤 **Author Attribution**: Shows who posted each image
- ⏰ **Timestamp Display**: Displays when the image was posted
- 🔄 **Replay Functionality**: Replay the last displayed image
- 🔒 **Secure Configuration**: Uses environment variables

## How It Works

1. **Discord Bot** (`stars.py`) monitors a specified Discord channel for messages containing images
2. When an image is detected (as an attachment or URL), it writes metadata to `image_data.json`
3. **HTML Overlay** (`index.html`) polls the JSON file and displays images in a Discord-style card
4. Images automatically fade in, display for a set duration, then fade out
5. The overlay is designed to be used as an **OBS Browser Source**

## Prerequisites

- Python 3.11 or higher
- A Discord Bot Token ([Discord Developer Portal](https://discord.com/developers/applications))
- OBS Studio (for displaying the overlay)

## Installation

1. **Clone the repository:**
   ```bash
   git clone git@the-dro:The-Dro/Discord-Images-to-OBS.git
   cd starboard
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your credentials:
   ```env
   DISCORD_TOKEN=your-discord-bot-token-here
   DISCORD_CHANNEL_ID=your-discord-channel-id-here
   ```

## Discord Bot Setup

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application or select an existing one
3. Navigate to the "Bot" section and create a bot
4. Copy the bot token and add it to your `.env` file
5. Enable the following bot intents:
   - **MESSAGE CONTENT INTENT** (Required to read message content)
   - **SERVER MEMBERS INTENT** (Optional, for better author names)
6. Invite the bot to your server with the necessary permissions
7. Get your channel ID (Enable Developer Mode in Discord, right-click channel → Copy ID)

## Running the Bot

### Manual Start

```bash
source .venv/bin/activate
python stars.py
```

### As a Systemd Service

The bot can run as a systemd service for automatic startup and management:

```bash
# Service file location: /etc/systemd/system/starboard-bot.service
sudo systemctl start starboard-bot.service
sudo systemctl enable starboard-bot.service  # Auto-start on boot
sudo systemctl status starboard-bot.service   # Check status
```

## OBS Studio Setup

1. **Add Browser Source:**
   - In OBS, add a new "Browser Source"
   - Set the URL to the full path of `index.html` 
   - Or host it on a web server and use the HTTP URL

2. **Configure Browser Source:**
   - Width: `1920` (or your stream resolution width)
   - Height: `1080` (or your stream resolution height)
   - Custom CSS: Leave empty (styling is handled in the HTML)

3. **Position the Overlay:**
   - The overlay appears in the bottom-right corner by default
   - Adjust the position as needed

## File Structure

```
starboard/
├── stars.py              # Discord bot that monitors channel and writes JSON
├── index.html            # OBS overlay that displays images
├── image_data.json       # JSON file containing current image data (auto-generated)
├── .env                  # Environment variables (not in git)
├── .env.example          # Example environment file
├── requirements.txt     # Python dependencies
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Configuration

### Image Display Settings

Edit `index.html` to customize:
- `POLL_INTERVAL`: How often to check for new images (default: 1000ms)
- `FADE_IN_DURATION`: Fade in animation duration (default: 2000ms)
- `DISPLAY_DURATION`: How long image is displayed (default: 8000ms)
- `FADE_OUT_DURATION`: Fade out animation duration (default: 2000ms)

### Supported Image Formats

- Direct image attachments (`.jpg`, `.png`, `.jpeg`)
- Image URLs in messages (must end with `.jpg`, `.png`, or `.jpeg`)

## Troubleshooting

### Bot not connecting
- Verify your `DISCORD_TOKEN` is correct in `.env`
- Ensure the bot has been invited to your server
- Check that MESSAGE CONTENT INTENT is enabled

### Images not displaying
- Verify `image_data.json` is being updated (check file contents)
- Ensure the HTML file can access `image_data.json` (check file permissions)
- Check browser console for errors (F12 in browser)

### Service not starting
- Check service logs: `sudo journalctl -u starboard-bot.service -n 50`
- Verify virtual environment path in service file
- Ensure `.env` file exists and has correct permissions

## Starboard
- Use starboard to have users vote on which images show up: https://starboardbot.github.io/docs/about/introduction/


## Security Notes

- **Never commit `.env` to git** - it contains sensitive credentials
- The `.env` file is already in `.gitignore`
- Rotate your Discord bot token if it's ever exposed
- Keep your bot token secure and never share it publicly

## License

This project is provided as-is for personal use.

## Contributing

Feel free to submit issues or pull requests for improvements!

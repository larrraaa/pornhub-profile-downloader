# Pornhub Profile Downloader

> **Last Updated:** April 26, 2026 — Added proxy support, improved CLI options.

## Description

This tool allows you to download videos from a specific content creator's profile on Pornhub. It scrapes the creator's profile page and downloads all the available videos. The tool is intended for personal use and educational purposes only. **It should only be applied to your own profiles or profiles for which you have explicit permission**.

The tool uses `yt-dlp` for the video download functionality and `BeautifulSoup` for web scraping. With a simple command-line interface, users can download all videos from a creator's profile.

> **Important Note:** Use this tool responsibly and respect content creators' rights. It should only be used on your own profiles or with permission from the content creator.

## What's New (April 26, 2026)

- **Proxy support** — Route all requests through a proxy with `--proxy`. Works with HTTP, HTTPS, and SOCKS5 proxies. Completely optional — the tool works fine without it.

## Installation

### Prerequisites

Make sure you have the following dependencies installed:

1. **Python 3.x**
2. **Pip** (Python package installer)

Follow these steps to install the dependencies:

1. Clone the repository:

   ```bash
   git clone https://github.com/larrraaa/pornhub-profile-downloader.git
   cd pornhub-profile-downloader
   ```

2. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

### Libraries

- `requests` – for fetching web pages.
- `beautifulsoup4` – for web scraping.
- `yt-dlp` – for downloading videos.

## Usage

1. **Run the tool**:

   ```bash
   python ph_downloader.py
   ```

2. Enter the creator's name whose videos you want to download. The tool will automatically scan their profile page and save all the video URLs.

3. The tool saves the found URLs in a text file (`phvid.txt`). You can specify how many videos to download or download all of them.

4. You can also adjust the domain to your region. By default, `https://de.pornhub.org` is used, but you can change the URL in the `ph_downloader.py` file.

### Proxy Usage (Optional)

If you want to route traffic through a proxy, you can pass it as a command-line argument:

```bash
python ph_downloader.py --proxy http://127.0.0.1:8080
python ph_downloader.py --proxy socks5://user:pass@proxy-server:1080
```

The proxy is **entirely optional**. If you don't provide `--proxy`, the tool connects directly as before.

Supported proxy formats:
- `http://host:port`
- `https://host:port`
- `socks5://host:port`
- `socks5://user:password@host:port`

## License

**MIT License**

Do whatever you want with the code – provided that you take responsibility for its use. The tool is shared for **educational purposes** and should only be used on **your own profiles** or with **explicit permission** from the content creator.

## Disclaimer

This tool is shared for **educational purposes** and should only be used on **your own profiles** or with **explicit permission** from the content creator. Any use of this tool outside of these guidelines is your own responsibility.

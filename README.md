# Pornhub Profile Downloader

## Description

This tool allows you to download videos from a specific content creator’s profile on Pornhub. It scrapes the creator's profile page and downloads all the available videos. The tool is intended for personal use and educational purposes only. **It should only be applied to your own profiles or profiles for which you have explicit permission**.

The tool uses `yt-dlp` for the video download functionality and `BeautifulSoup` for web scraping. With a simple command-line interface, users can download all videos from a creator’s profile.

> **Important Note:** Use this tool responsibly and respect content creators' rights. It should only be used on your own profiles or with permission from the content creator.

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

### Libraries:

- `requests` – for fetching web pages.
- `beautifulsoup4` – for web scraping.
- `yt-dlp` – for downloading videos.

Create a `requirements.txt` file that includes the dependencies:

```text
requests
beautifulsoup4
yt-dlp
```

## Usage

1. **Run the tool**:

   Execute the script to download videos from a specific content creator:

   ```bash
   python ph_downloader.py
   ```

2. Enter the creator's name whose videos you want to download. The tool will automatically scan their profile page and save all the video URLs.

3. The tool saves the found URLs in a text file (`phvid.txt`). You can specify how many videos to download or download all of them.

4. You can also adjust the domain to your region. By default, `https://de.pornhub.org` is used, but you can change the URL in the `ph_downloader.py` file at the line `profile_url = f"https://de.pornhub.org/model/{convert_creator_name(creator)}/videos"`.

## License

**MIT License**

Do whatever you want with the code – provided that you take responsibility for its use. The tool is shared for **educational purposes** and should only be used on **your own profiles** or with **explicit permission** from the content creator.

## Disclaimer

This tool is shared for **educational purposes** and should only be used on **your own profiles** or with **explicit permission** from the content creator. Any use of this tool outside of these guidelines is your own responsibility.

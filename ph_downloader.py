import os
import time
import requests
from bs4 import BeautifulSoup
import yt_dlp as youtube_dl
import sys

# Rate Limiter: Waiting time between requests (in seconds)
RATE_LIMIT_SECONDS = 1


def get_video_urls_from_page(page_url):
    video_urls = []

    try:
        response = requests.get(page_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Suche nach Video-Links
        video_elements = soup.find_all('a', href=True)
        for element in video_elements:
            href = element['href']
            if '/view_video.php?viewkey=' in href:
                full_url = f"https://www.pornhub.org{href}"
                video_urls.append(full_url)

    except requests.RequestException:
        pass  # Fehler beim Abrufen der Seite ignorieren

    return video_urls


def get_all_video_urls(profile_url):
    all_video_urls = []
    page_number = 1

    while True:
        page_url = f"{profile_url}?page={page_number}"

        video_urls = get_video_urls_from_page(page_url)

        if not video_urls:
            # Wenn keine Videos gefunden werden, beenden
            break

        all_video_urls.extend(video_urls)
        page_number += 1

        # Rate Limiter: Kurze Pause zwischen den Seitenanfragen
        time.sleep(RATE_LIMIT_SECONDS)

    return all_video_urls


def save_urls_to_file(urls, filename):
    try:
        with open(filename, 'w') as file:
            for url in urls:
                file.write(url + '\n')
    except IOError:
        pass  # Fehler beim Speichern der URLs ignorieren


def convert_creator_name(creator_name):
    # Ersetze Leerzeichen durch Bindestriche und konvertiere in Kleinbuchstaben
    return creator_name.replace(' ', '-').lower()


def normalize_name(name):
    # Ersetze Bindestriche durch Leerzeichen und konvertiere in Kleinbuchstaben
    return name.replace('-', ' ').lower()

def download_video(url, folder_path, creator_name):
    def progress_hook(d):
        if d['status'] == 'downloading':
            total = d.get('total_bytes', 0)
            downloaded = d.get('downloaded_bytes', 0)
            percentage = (downloaded / total) * 100 if total else 0
            print(f"Downloading: {percentage:.2f}% complete", end='\r')

    creator_name_converted = convert_creator_name(creator_name)
    creator_name_normalized = normalize_name(creator_name_converted)

    # Add the creator's name to the folder_path
    folder_path = os.path.join(folder_path, creator_name_converted)

    # Ensure the directory exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # yt-dlp options for downloading the video
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(folder_path, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'progress_hooks': [progress_hook],
        'quiet': True,  # Do not display verbose info
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_author = info_dict.get('uploader', '').lower()

            # Check if the video author matches the specified creator
            if creator_name_converted not in video_author and creator_name_normalized not in video_author:
                return False  # Video not downloaded

            print(f"Starting download: {info_dict.get('title', 'Unknown video')}")
            ydl.download([url])
            print(f"Download completed: {info_dict.get('title', 'Unknown video')}")
            return True  # Video successfully downloaded

    except Exception as e:
        print(f"Error downloading video: {e}")
        return False  # Video not downloaded


def download_videos_from_file(filename, folder_path, creator_name, count=None):
    try:
        with open(filename, 'r') as file:
            urls = file.readlines()

        urls = [url.strip() for url in urls]

        downloaded_count = 0
        for url in urls:
            if count is not None and downloaded_count >= count:
                break

            print(f"Checking URL: {url}")
            if download_video(url, folder_path, creator_name):
                downloaded_count += 1

            # Rate Limiter: Short pause between video downloads
            time.sleep(RATE_LIMIT_SECONDS)

        return downloaded_count

    except IOError:
        pass  # Ignore file read errors


def shutdown_pc():
    print("The PC will now shut down...")
    time.sleep(2)
    if sys.platform == 'win32':
        os.system('shutdown /s /t 1')
    elif sys.platform == 'darwin':
        os.system('sudo shutdown -h now')
    elif sys.platform == 'linux':
        os.system('sudo shutdown -h now')

if __name__ == "__main__":
    creator = input("Gib den Content Creator Namen ein: ")
    profile_url = f"https://de.pornhub.org/model/{convert_creator_name(creator)}/videos"

    print("Scanning the page for videos...")

    all_urls = get_all_video_urls(profile_url)

    if all_urls:
        save_urls_to_file(all_urls, 'phvid.txt')

        confirm = input(
            f"Found {len(all_urls)} video URLs. Do you want to save them to the file 'phvid.txt'? (yes/no): ").strip().lower()
        if confirm == 'yes':
            folder_path = input("Enter the download folder: ")

            # Extend the download folder with the creator's name
            folder_path = os.path.join(folder_path, convert_creator_name(creator))

            # Ask whether to shut down the PC after downloading
            shutdown_decision = input(
                "Do you want to shut down the PC after all videos have been downloaded? (yes/no): ").strip().lower()

            # Download options
            download_decision = input("Do you want to download the videos? (yes/no): ").strip().lower()
            if download_decision == 'yes':
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                number = input(
                    "How many videos do you want to download? (Enter a number, 'A' for All, or 'N' for None): ").strip().upper()
                if number == 'N':
                    print("No videos will be downloaded.")
                elif number == 'A':
                    downloaded_count = download_videos_from_file('phvid.txt', folder_path, creator)
                else:
                    try:
                        number = int(number)
                        downloaded_count = download_videos_from_file('phvid.txt', folder_path, creator, number)
                    except ValueError:
                        downloaded_count = 0  # Ignore invalid input

                # Shut down the PC if requested
                if shutdown_decision == 'yes' and downloaded_count > 0:
                    shutdown_pc()
            else:
                print("Videos were not downloaded.")
        else:
            print("URLs were not saved.")
    else:
        print("No videos found or error retrieving the pages.")

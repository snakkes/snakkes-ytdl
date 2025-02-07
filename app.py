import sys
from rich.console import Console
from downloader import Downloader
from combiner import Combiner
from utils import check_ffmpeg
import subprocess
import os
import pyfiglet
import random
import time

console = Console()

def scrolling_header():
    """Displays a scrolling text header with 'snakkes-ytdl' in red."""
    ascii_banner = pyfiglet.figlet_format("snakkes-ytdl")
    scroll_chars = ["|", ",", "/", "}", "{", "]", "["]
    speed = 0.005
    
    for char in ascii_banner:
        if char != " " and char != "\n" and random.random() > 0.8:
            console.print(random.choice(scroll_chars), end="", style="red")
        else:
            console.print(char, end="", style="red")
        sys.stdout.flush()
        time.sleep(speed)
    print("\n")

def main():
    if not check_ffmpeg():
        sys.exit(1)

    try:
        subprocess.run(["ffmpeg", "-version"], check=True)
        print("FFmpeg is installed and working.")
    except subprocess.CalledProcessError:
        print("FFmpeg is not working correctly.")
    except FileNotFoundError:
        print("FFmpeg is not installed.")

    venv_python = sys.executable  # Assuming the script is run within the venv

    downloader = Downloader(venv_python)
    combiner = Combiner()

    print(os.environ['PATH'])

    while True:
        scrolling_header()  # Display the scrolling header
        downloader.display_options()  # Call the new method to display options

        choice = console.input("\n[bold]Enter choice (1-5): [/bold]")

        if choice == "1":
            video_url = console.input("\n[bold]Enter YouTube video URL: [/bold]").strip()
            downloader.download_video(video_url, choice)
        elif choice == "2":
            video_file = console.input("\n[bold]Enter video file path: [/bold]").strip()
            audio_file = console.input("\n[bold]Enter audio file path: [/bold]").strip()
            output_file = console.input("\n[bold]Enter output file path: [/bold]").strip()
            combiner.combine_audio_video(video_file, audio_file, output_file)
        elif choice == "3":
            console.print("[bold green]Exiting... Goodbye![/bold green]")
            break
        else:
            console.print("[bold red]Invalid choice. Please try again.[/bold red]")

if __name__ == "__main__":
    main()

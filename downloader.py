import subprocess
import os
import shutil
from rich.console import Console
import certifi
import ssl
import re
from alive_progress import alive_bar
import time

console = Console()

class Downloader:
    def __init__(self, venv_python):
        self.venv_python = venv_python

    def display_options(self):
        """Displays available download options with detailed descriptions."""
        options = [
            {"name": "1. Best Quality (MP4)", "desc": "Highest video and audio quality combined, suitable for large screens.", "color": "green"},
            {"name": "2. Medium Quality", "desc": "720p resolution, balanced quality for most uses.", "color": "orange1"},
            {"name": "3. Audio Only", "desc": "Extracts the audio track in MP3 format, ideal for music.", "color": "pink1"},
            {"name": "4. Custom Selection", "desc": "Choose a specific format from available options.", "color": "cyan"},
            {"name": "5. Exit Program", "desc": "Exit the application.", "color": "red"}
        ]
        
        console.print("\n[bold white]MAIN MENU:[/bold white]\n")
        for option in options:
            console.print(
                f"[{option['color']}]{option['name']}[/{option['color']}] - [white]{option['desc']}[/white]"
            )

    def download_video(self, video_url, quality_choice):
        """Downloads video with selected quality."""
        output_dir = os.path.join("downloaded_videos")
        os.makedirs(output_dir, exist_ok=True)

        format_map = {
            "1": "bestvideo+bestaudio/best",
            "2": "bestvideo[height<=720]+bestaudio/best",
            "3": "bestaudio/best",
            "4": None
        }

        selected_format = format_map.get(quality_choice, "1")

        if quality_choice == "4":
            console.print("\n[bold yellow]Fetching available formats...[/bold yellow]")
            subprocess.run([self.venv_python, "-m", "yt_dlp", "-F", video_url])
            selected_format = console.input("\n[bold]Enter format code: [/bold]")

        command = [
            self.venv_python,
            "-m",
            "yt_dlp",
            "--ffmpeg-location", shutil.which("ffmpeg"),
            "-f", selected_format,
            "--merge-output-format", "mp4",
            "-o", os.path.join(output_dir, "%(title)s.%(ext)s"),
            "--embed-thumbnail",
            "--embed-metadata",
            video_url
        ]

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        with alive_bar(100, title="Downloading") as bar:
            for _ in range(100):
                time.sleep(0.1)  # Simulate progress
                bar()

            process.wait()

        if process.returncode == 0:
            console.print("\n[bold green]Download completed successfully![/bold green]")
        else:
            console.print(f"[bold red]An error occurred: {process.stderr}[/bold red]") 
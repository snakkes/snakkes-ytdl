import subprocess
import sys
import os
from rich.console import Console

console = Console()

def combine_audio_video(video_file, audio_file, output_file):
    """Combines a video file and an audio file into a single output file."""
    if not os.path.exists(video_file):
        console.print(f"[bold red]Error: Video file '{video_file}' not found.[/bold red]")
        return

    if not os.path.exists(audio_file):
        console.print(f"[bold red]Error: Audio file '{audio_file}' not found.[/bold red]")
        return

    try:
        console.print(f"[bold yellow]Combining '{video_file}' and '{audio_file}' into '{output_file}'...[/bold yellow]")
        command = [
            "ffmpeg",
            "-i", video_file,
            "-i", audio_file,
            "-c:v", "copy",
            "-c:a", "aac",
            "-strict", "experimental",
            output_file
        ]
        subprocess.run(command, check=True)
        console.print(f"[bold green]Successfully combined into '{output_file}'![/bold green]")
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]Error during combination: {str(e)}[/bold red]")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        console.print("[bold red]Usage: python combine_av.py <video_file> <audio_file> <output_file>[/bold red]")
        sys.exit(1)

    video_file = sys.argv[1]
    audio_file = sys.argv[2]
    output_file = sys.argv[3]

    combine_audio_video(video_file, audio_file, output_file) 
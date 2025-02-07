import subprocess
import os
from rich.console import Console
import re
from alive_progress import alive_bar

console = Console()

class Combiner:
    def combine_audio_video(self, video_file, audio_file, output_file):
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

            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

            with alive_bar(100, title="Combining") as bar:
                for line in process.stdout:
                    console.print(line.strip())
                    # Example parsing logic (you'll need to adjust this based on actual output)
                    match = re.search(r'(\d+)%', line)
                    if match:
                        bar(int(match.group(1)) - bar.current())

                process.wait()

            console.print(f"[bold green]Successfully combined into '{output_file}'![/bold green]")
        except subprocess.CalledProcessError as e:
            console.print(f"[bold red]Error during combination: {str(e)}[/bold red]") 
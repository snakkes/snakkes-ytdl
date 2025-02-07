import shutil
from rich.console import Console

console = Console()

def check_ffmpeg():
    """Checks if ffmpeg is installed."""
    ffmpeg_path = shutil.which("ffmpeg")
    if not ffmpeg_path:
        console.print("[bold red]FFmpeg not found! Please install it and try again.[/bold red]")
        return False
    return True 
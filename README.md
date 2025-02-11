# Snakkes-ytdl

Snakkes-ytdl is a feature-rich Python terminal application for downloading YouTube videos and audio with various quality options. It provides a user-friendly interface with dynamic progress bars and customizable download settings.

## Screenshot

https://prnt.sc/GEf_BD4aom1y

## Features

- Download videos in multiple resolutions (Best, Medium, Audio Only)
- Extract audio-only (MP3 format)
- Embedded metadata and thumbnails
- Automatic dependency installation
- Beautiful terminal interface with rich formatting
- Continuous download mode
- Real-time progress bars using `alive-progress`

## Installation

### Prerequisites

- **Python 3.7+**: Ensure Python is installed on your system.
- **FFmpeg**: Required for video processing.

#### Install FFmpeg

- **macOS**:
  ```bash
  brew install ffmpeg
  ```

- **Linux**:
  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```

- **Windows**:
  - Use a package manager like Chocolatey:
    ```powershell
    choco install ffmpeg
    ```

### Clone the Repository

1. **Clone the repository**:
   ```bash
   git clone https://github.com/snakkes/snakkes-ytdl.git
   cd snakkes-ytdl
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**:
   ```bash
   python app.py
   ```

2. **Main Menu**:
   - The application will display a scrolling header and a main menu with options:
     - **1. Best Quality (MP4)**: Highest video and audio quality combined.
     - **2. Medium Quality**: 720p resolution, balanced quality.
     - **3. Audio Only**: Extracts the audio track in MP3 format.
     - **4. Custom Selection**: Choose a specific format from available options.
     - **5. Exit Program**: Exit the application.

3. **Download Process**:
   - Enter the YouTube video URL when prompted.
   - Select the desired quality option.
   - The application will display a progress bar while downloading.

4. **Combining Audio and Video**:
   - If you choose to combine audio and video, the application will prompt for file paths and display a progress bar during the process.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the developers of `yt-dlp`, `rich`, and `alive-progress` for their excellent libraries. 

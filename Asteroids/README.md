# Asteroids

This project is a retro-style Asteroids game built with Python's Pygame. It was converted to a browser-compatible format using Pygbag and deployed on GitHub Pages.

## Visit The Site

Feel free to check out the [project here](https://barronbytes.github.io/Asteroids/)!

![Asteroids Game Screenshot](images/asteroids_game.PNG)

## Features

- **Pygame:** Utilized to create 5 classes for game environment

## Prerequisites

Before running this project locally, ensure you have the following installed:

- Python (version 2.6.1 or above)
- Pygame module
- VcXsrv (if running WSL--instructions below)
- Pygbag (will need this to create web-ready version of project)

## Installations

### Pygame Setup

1. Setup virtual environment:
``` bash
python3 -m venv venv
source venv/bin/activate
```
2. Install Pygame using requirements.txt file:
``` bash
pip install -r requirements.txt
```
3. Verify Pygame installation
``` bash
python3 -m pygame
```

### VcXsrv Setup

1. Open the PowerShell (not Linux) terminal and ensure you have WSL2 installed with this command:
``` powershell
wsl --version # This will verify if installed
wsl --install -d Ubuntu # Run this line only if not installed
```
2. Install [VcXsrv](https://vcxsrv.com/) on Windows. [This medium article](https://medium.com/@youngtuo/run-pygame-through-wsl2-in-3-steps-2ee0b776dbaa) provides detailed installation steps.
3. Open the Linux terminal, and save changes to the configuration file.
``` bash
nano ~/.bashrc # Opens config file
export DISPLAY=$(grep nameserver /etc/resolv.conf | awk '{print $2}'):0.0 # Save to end of file
source ~/.bashrc # Applies changes
```
4. Use the Linux terminal to confirm changes work properly. (A popup window of eyes should open if everything works.)
``` bash
sudo apt update
sudo apt install x11-apps # 11 are numbers
xeyes
```
5. This works the first time. On subsequent attempts to run your code, you should **ALWAYS** open a new session of VcXsrv. You do this by launching the **XLaunch** app.

### Pygbag Setup

1. Be inside project folder before using Linux commands
2. Linux (update package manager): sudo apt update
3. Linux (virtual environment): python3 -m venv myenv && source myenv/bin/activate
4. Linux (install pygbag): pip install pygbag
5. Linux (verify install): pygbag --version
6. Edit **main.py** file only as instructed by the [pygbag community](https://pygame-web.github.io/wiki/pygbag/).
7. Linux (convert files): **pygbag .**

## Usage (How To Play!)

Use keyboard strokes to control spaceship:
- Move up: *w* or *up* arrow
- Move down: *s* or *down* arrow
- Move left: *a* or *left* arrow
- Move right: *d* or *right* arrow
- Shot asteroids: *spacebar*

User keyboard or mouse actions to exit game:
- Click upper righthand corner 'X' to close game browser (only works on pygame version)
- Click **Esc** button (works on both pygame and web version)

## Credits & Contributing

Thank you [boot.dev](https://www.boot.dev/) for providing an online back-end learning platform with integrated project ideas Contributions are welcome! Feel free to submit a pull request to improve the project or open an issue to report any problems.

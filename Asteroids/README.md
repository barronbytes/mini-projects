# Asteroids

This is a retro asteroids game.

## Visit The Site

Feel free to check out the project here!

## Features

- **Pygame:** Module

## Prerequisites

Before running this project locally, ensure you have the following installed:

- Python (version 2.6.1 or above)
- Pygame module
- VcXsrv (if running WSL--instructions below)

## Installations

**Pygame**
1. Open the PowerShell (not Linux) terminal and ensure you have WSL2 installed with this command:
``` powershell
wsl --version # This will verify if installed
wsl --install -d Ubuntu # Run this line only if not installed
```
2. Install [VcXsrv](https://vcxsrv.com/) on Windows. [This medium article](https://medium.com/@youngtuo/run-pygame-through-wsl2-in-3-steps-2ee0b776dbaa) provided detailed installation steps.
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

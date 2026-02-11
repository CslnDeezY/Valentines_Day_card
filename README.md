# Valentine's Day Card 

A cute interactive Valentine's Day card application built with Python, Tkinter, and CustomTkinter. Dockerized for cross-platform compatibility.

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your system
- [Docker Compose](https://docs.docker.com/compose/install/) installed


## Installation & Running

### On Linux

1. **Allow X server access** (run once per session):
   ```bash
   xhost +local:docker
   ```

2. **Build and run the application**:
   ```bash
   docker-compose --profile linux up --build
   ```

   Or using Docker directly:
   ```bash
   docker build -t valentines-card .
   docker run -it --rm \
     -e DISPLAY=$DISPLAY \
     -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
     --network host \
     valentines-card
   ```

3. **Clean up X server access** (optional, after closing the app):
   ```bash
   xhost -local:docker
   ```

### On Windows

1. **Install and configure an X Server** (e.g., VcXsrv):
   - Download and install [VcXsrv](https://sourceforge.net/projects/vcxsrv/)
   - Launch XLaunch from the Start menu
   - Configure with these settings:
     - Display mode: **Multiple windows**
     - Display number: **0**
     - Start no client: ✓
     - **Disable access control**: ✓ (Important!)
   - Save the configuration for future use

2. **Build and run the application**:
   ```bash
   docker-compose --profile windows up --build
   ```

   Or using Docker directly:
   ```bash
   docker build -t valentines-card .
   docker run -it --rm ^
     -e DISPLAY=host.docker.internal:0 ^
     valentines-card
   ```

   **Note**: If using PowerShell, replace `^` with `` ` `` for line continuation.

3. **Keep the X Server running** while the application is active.


## Manual Run (Without Docker)

If you prefer to run without Docker:

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   python The_card.py
   ```

## Technologies Used

- **Python 3.11**
- **Tkinter** - GUI framework
- **CustomTkinter** - Modern UI components
- **Pillow (PIL)** - Image and GIF handling
- **Docker** - Containerization for cross-platform compatibility

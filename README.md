# Linux System Performance Manager

## Overview

Linux System Performance Manager is a mini project designed to automate the management, diagnostics, and performance analysis of Linux servers using Ansible and Python. It provides a set of playbooks and scripts to monitor system health, manage essential services, and generate detailed reports on server status.

## Features

- Automated start and verification of critical services (Nginx, Apache2)
- Installation and verification of Python3
- User session and update checks
- Custom Python system analysis script (`sysanalyzer.py`) for:
  - System information (CPU, memory, disk, network)
  - Performance metrics (CPU load, I/O, top processes)
  - System logs and network statistics
- Easy setup with a single requirements script
- Modular and extensible for additional diagnostics

## Project Structure

- `sysmanager.yml` — Main Ansible playbook for server management and diagnostics
- `sysanalyzer.py` — Python script for advanced system analysis
- `requirements.sh` — Shell script to install all required dependencies
- `inventory.ini` — Ansible inventory file (define your `linux_servers` group here)

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/SoufianeAmghar/linux-sys-performance.git
   cd linux-sys-performance
   ```

2. **Install requirements**
   ```bash
   sudo bash requirements.sh
   ```

3. **Configure your inventory**
   - Edit `inventory.ini` and add your Linux server IPs under the `[linux_servers]` group.

4. **Run the Ansible playbook**
   ```bash
   ansible-playbook -i inventory.ini sysmanager.yml
   ```

## Usage

- The playbook will:
  - Start Nginx and Apache2
  - Ensure Python3 is installed
  - List logged-in users and available updates
  - Run `sysanalyzer.py` for a detailed system analysis
  - Print all results in the Ansible output

## Customization

- You can extend `sysanalyzer.py` to add more checks or output formats.
- Add more tasks to `sysmanager.yml` for additional automation needs.

## Troubleshooting

- Ensure all target servers are accessible via SSH and have Python3 installed.
- If you encounter missing commands, rerun `requirements.sh` or manually install the required packages.
- For permission issues, run scripts and playbooks with `sudo`.

## License

MIT License

## Author

Soufiane Amghar
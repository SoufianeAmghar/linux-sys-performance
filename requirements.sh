#!/bin/bash

# --- Variables ---
DATE_TIME=$(date +"%Y-%m-%d %H:%M:%S")

# --- Functions ---
function error_exit {
    echo "[ERROR] $1" >&2
    exit 1
}

# --- Check for root ---
if [[ $EUID -ne 0 ]]; then
   error_exit "This script must be run as root. Use sudo."
fi

echo "[$DATE_TIME] Updating and upgrading system packages..."
apt update -y || error_exit "apt update failed"
apt upgrade -y || error_exit "apt upgrade failed"

echo "[$DATE_TIME] Installing required packages..."
apt install -y software-properties-common || error_exit "Failed to install software-properties-common"
add-apt-repository --yes --update ppa:ansible/ansible || error_exit "Failed to add Ansible repository"
apt install -y ansible python3-apt python3-pip python3-psutil || error_exit "Failed to install Ansible or Python packages"
apt install -y openssh-server || error_exit "Failed to install OpenSSH server"

echo "[$DATE_TIME] Installing Python pip packages..."
pip3 install --upgrade pip || error_exit "Failed to upgrade pip"
pip3 install ansible-lint || error_exit "Failed to install ansible-lint"

# --- Check for required commands ---
for cmd in ansible python3 pip3 lscpu ifconfig dmesg iostat netstat free ps; do
    if ! command -v $cmd &> /dev/null; then
        error_exit "$cmd is not installed or not in PATH."
    fi
done

echo "[$DATE_TIME] All requirements installed successfully."

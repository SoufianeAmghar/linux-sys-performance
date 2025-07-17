import subprocess

def run_command(command):
    """
    Éxecutez une commande shell et retourner son statut.
    """
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command '{command}': {e.stderr.decode('utf-8').strip()}")
        return None
    
def analyze_system():
    """
    Analysez le système pour collecter des informations globales.
    """
    print("Collecting system information...")
    
    # Collect basic system information
    uname = run_command("uname -a")
    if uname:
        print(f"System Information: {uname}")
    
    # Collect CPU information
    cpu_info = run_command("lscpu")
    if cpu_info:
        print(f"CPU Information:\n{cpu_info}")

    # Collect network information
    network_info = run_command("ifconfig")
    if network_info:
        print(f"Network Information:\n{network_info}")  

    # Collect system logs
    sys_logs = run_command("dmesg | tail -n 50")
    if sys_logs:
        print(f"System Logs:\n{sys_logs}")
    print("System analysis completed.")


def analyze_performance():
    """
    Analysez les performances du système.
    """
    print("Analyzing system performance...")
    
    # Collect CPU load
    cpu_load = run_command("uptime")
    if cpu_load:
        print(f"CPU Load: {cpu_load}")

    # Collect I/O statistics
    io_stats = run_command("iostat")
    if io_stats:
        print(f"I/O Statistics:\n{io_stats}")

    # Collect network statistics
    net_stats = run_command("netstat -i")
    if net_stats:
        print(f"Network Statistics:\n{net_stats}")


def analyze_memory():
    """Analyse l'utilisation de la mémoire."""
    output = run_command("free -h")
    if output:
        lines = output.split('\n')
        mem_line = lines[1] # Ligne 'Mem:'
        parts = mem_line.split()
        total_mem = parts[1]
        used_mem = parts[2]
        free_mem = parts[3]
        print(f"--- Analyse Mémoire ---")
        print(f"Mémoire totale : {total_mem}")
        print(f"Mémoire utilisée : {used_mem}")
        print(f"Mémoire libre : {free_mem}")

def analyze_disk_usage():
    """Analyse l'utilisation du disque."""
    output = run_command("df -h")
    if output:
        lines = output.split('\n')
        print(f"\n--- Analyse Utilisation Disque ---")
        for line in lines:
            if line.startswith('/dev/') or line.startswith('Filesystem'):
                print(line)

def analyze_top_processes(count=5):
    """Analyse les processus les plus gourmands en CPU."""
    output = run_command(f"ps aux --sort=-%cpu | head -n {count + 1}") # +1 pour l'en-tête
    if output:
        lines = output.split('\n')
        print(f"\n--- Top {count} Processus par CPU ---")
        for line in lines:
            print(line)

if __name__ == "__main__":
    print("Début de l'analyse système...")
    analyze_system()
    analyze_performance()
    analyze_memory()
    analyze_disk_usage()
    analyze_top_processes()
    print("\nAnalyse système terminée.")

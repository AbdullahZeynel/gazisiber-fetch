#!/usr/bin/env python3
"""
GaziSiber Fetch - A system information display tool for Linux
"""

import os
import platform
import subprocess
import shutil
from datetime import timedelta


class Colors:
    """ANSI color codes for terminal output"""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'


class SystemInfo:
    """Collects system information"""
    
    def __init__(self):
        self.info = {}
        self._collect_info()
    
    def _run_command(self, cmd):
        """Run a shell command and return output"""
        try:
            result = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True,
                timeout=5
            )
            return result.stdout.strip()
        except Exception:
            return "Unknown"
    
    def _get_os_info(self):
        """Get OS information"""
        try:
            # Try to read from os-release
            if os.path.exists('/etc/os-release'):
                with open('/etc/os-release', 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        if line.startswith('PRETTY_NAME='):
                            return line.split('=')[1].strip().strip('"')
            return f"{platform.system()} {platform.release()}"
        except Exception:
            return f"{platform.system()} {platform.release()}"
    
    def _get_kernel(self):
        """Get kernel version"""
        return platform.release()
    
    def _get_architecture(self):
        """Get system architecture"""
        return platform.machine()
    
    def _get_hostname(self):
        """Get system hostname"""
        return platform.node()
    
    def _get_uptime(self):
        """Get system uptime"""
        try:
            with open('/proc/uptime', 'r') as f:
                uptime_seconds = float(f.readline().split()[0])
                uptime_td = timedelta(seconds=int(uptime_seconds))
                days = uptime_td.days
                hours, remainder = divmod(uptime_td.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                
                parts = []
                if days > 0:
                    parts.append(f"{days}d")
                if hours > 0:
                    parts.append(f"{hours}h")
                if minutes > 0:
                    parts.append(f"{minutes}m")
                
                return " ".join(parts) if parts else "0m"
        except Exception:
            return "Unknown"
    
    def _get_cpu_info(self):
        """Get CPU information"""
        try:
            with open('/proc/cpuinfo', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if 'model name' in line:
                        cpu = line.split(':')[1].strip()
                        # Simplify CPU name
                        cpu = cpu.replace('(R)', '').replace('(TM)', '').replace('  ', ' ')
                        return cpu
            return "Unknown"
        except Exception:
            return "Unknown"
    
    def _get_cpu_cores(self):
        """Get CPU core count"""
        try:
            return str(os.cpu_count())
        except Exception:
            return "Unknown"
    
    def _get_memory_info(self):
        """Get memory information"""
        try:
            with open('/proc/meminfo', 'r') as f:
                lines = f.readlines()
                mem_total = 0
                mem_available = 0
                
                for line in lines:
                    if 'MemTotal' in line:
                        mem_total = int(line.split()[1])
                    elif 'MemAvailable' in line:
                        mem_available = int(line.split()[1])
                
                if mem_total > 0:
                    mem_used = mem_total - mem_available
                    mem_total_gb = mem_total / 1024 / 1024
                    mem_used_gb = mem_used / 1024 / 1024
                    return f"{mem_used_gb:.1f}GB / {mem_total_gb:.1f}GB"
            return "Unknown"
        except Exception:
            return "Unknown"
    
    def _get_gpu_info(self):
        """Get GPU information"""
        # Try lspci first - get everything after "VGA compatible controller:" or similar
        gpu = self._run_command("lspci | grep -i 'vga\\|3d\\|display' | head -1 | sed 's/.*: //'")
        if gpu and gpu != "Unknown" and gpu.strip():
            return gpu.strip()
        
        # Fallback to checking for common GPU info
        gpu = self._run_command("lshw -C display 2>/dev/null | grep product | head -1 | cut -d':' -f2")
        if gpu and gpu != "Unknown" and gpu.strip():
            return gpu.strip()
        
        return "Unknown"
    
    def _get_shell(self):
        """Get current shell"""
        shell = os.environ.get('SHELL', 'Unknown')
        if shell != 'Unknown':
            shell = os.path.basename(shell)
        return shell
    
    def _get_terminal(self):
        """Get terminal emulator"""
        term = os.environ.get('TERM', 'Unknown')
        return term
    
    def _collect_info(self):
        """Collect all system information"""
        self.info = {
            'hostname': self._get_hostname(),
            'os': self._get_os_info(),
            'kernel': self._get_kernel(),
            'arch': self._get_architecture(),
            'uptime': self._get_uptime(),
            'shell': self._get_shell(),
            'terminal': self._get_terminal(),
            'cpu': self._get_cpu_info(),
            'cpu_cores': self._get_cpu_cores(),
            'memory': self._get_memory_info(),
            'gpu': self._get_gpu_info(),
        }


def get_ascii_art():
    """Return ASCII art logo"""
    art = [
        "   ____           _ ____  _ _               ",
        "  / ___| __ _ ___(_) ___(_) |__   ___ _ __ ",
        " | |  _ / _` |_  / \\___ \\| | '_ \\ / _ \\ '__|",
        " | |_| | (_| |/ /| |___) | | |_) |  __/ |   ",
        "  \\____|\\__,_/___|_|____/|_|_.__/ \\___|_|   ",
        "                                             ",
    ]
    return art


def display_info(sysinfo):
    """Display system information in a nice format"""
    ascii_art = get_ascii_art()
    info = sysinfo.info
    
    # Prepare info lines
    info_lines = [
        "",
        f"{Colors.BOLD}{Colors.YELLOW}OS:{Colors.RESET}       {info['os']}",
        f"{Colors.BOLD}{Colors.YELLOW}Kernel:{Colors.RESET}   {info['kernel']}",
        f"{Colors.BOLD}{Colors.YELLOW}Arch:{Colors.RESET}     {info['arch']}",
        f"{Colors.BOLD}{Colors.YELLOW}Host:{Colors.RESET}     {info['hostname']}",
        f"{Colors.BOLD}{Colors.YELLOW}Uptime:{Colors.RESET}   {info['uptime']}",
        f"{Colors.BOLD}{Colors.YELLOW}Shell:{Colors.RESET}    {info['shell']}",
        f"{Colors.BOLD}{Colors.YELLOW}Terminal:{Colors.RESET} {info['terminal']}",
        "",
        f"{Colors.BOLD}{Colors.CYAN}CPU:{Colors.RESET}      {info['cpu']}",
        f"{Colors.BOLD}{Colors.CYAN}Cores:{Colors.RESET}    {info['cpu_cores']}",
        f"{Colors.BOLD}{Colors.CYAN}Memory:{Colors.RESET}   {info['memory']}",
        f"{Colors.BOLD}{Colors.CYAN}GPU:{Colors.RESET}      {info['gpu']}",
        "",
    ]
    
    # Display ASCII art and info side by side
    max_lines = max(len(ascii_art), len(info_lines))
    
    for i in range(max_lines):
        # Print ASCII art with color
        if i < len(ascii_art):
            print(f"{Colors.CYAN}{ascii_art[i]}{Colors.RESET}", end="")
        else:
            print(" " * len(ascii_art[0]), end="")
        
        # Print info
        if i < len(info_lines):
            print(f"  {info_lines[i]}")
        else:
            print()
    
    # Print color palette
    print(f"\n  {Colors.RED}███{Colors.GREEN}███{Colors.YELLOW}███{Colors.BLUE}███"
          f"{Colors.MAGENTA}███{Colors.CYAN}███{Colors.WHITE}███{Colors.RESET}\n")


def main():
    """Main entry point"""
    try:
        sysinfo = SystemInfo()
        display_info(sysinfo)
    except KeyboardInterrupt:
        print("\n")
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())

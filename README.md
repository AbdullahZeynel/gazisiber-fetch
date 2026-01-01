# GaziSiber Fetch

A fast and lightweight system information display tool for Linux, designed as a modern alternative to fastfetch and neofetch.

## Features

- 🚀 **Fast execution** - Minimal dependencies and optimized code
- 🎨 **Colorful display** - Beautiful ASCII art and colored output
- 💻 **System information** - OS, kernel, architecture, hostname, uptime
- 🔧 **Hardware details** - CPU, memory, GPU information
- 🐚 **Shell information** - Current shell and terminal emulator
- 📦 **Easy installation** - Simple installation via pip or make

## Installation

### Method 1: Using pip (Recommended)

```bash
# Install for current user
pip3 install --user .

# Or install system-wide (requires sudo)
sudo pip3 install .
```

### Method 2: Using Make

```bash
# Install for current user
make install

# Or install system-wide (requires sudo)
sudo make install-system
```

### Method 3: Building Debian Package

For installation via `apt`, you can build a Debian package:

```bash
# Install build dependencies
sudo apt-get install debhelper python3-all python3-setuptools dh-python

# Build the package
dpkg-buildpackage -us -uc -b

# Install the package
sudo dpkg -i ../gazisiber-fetch_1.0.0-1_all.deb
```

## Usage

After installation, simply run:

```bash
gazisiber
```

This will display your system information with a colorful ASCII art logo.

## Requirements

- Python 3.6 or higher
- Linux operating system
- Standard Linux utilities (`/proc` filesystem)

## Uninstallation

### If installed with pip:
```bash
pip3 uninstall gazisiber-fetch
```

### If installed with make:
```bash
make uninstall
```

### If installed from .deb package:
```bash
sudo apt remove gazisiber-fetch
```

## Development

### Testing the script without installation:

```bash
python3 gazisiber_fetch.py
```

### Building the project:

```bash
python3 setup.py build
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

GaziSiber Team
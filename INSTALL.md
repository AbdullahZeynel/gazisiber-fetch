# Installation Guide for GaziSiber Fetch

This guide provides detailed instructions for installing GaziSiber Fetch on various Linux distributions.

## Quick Install (Any Linux Distribution)

The easiest way to install GaziSiber Fetch is using pip:

```bash
pip3 install --user .
```

After installation, add `~/.local/bin` to your PATH if it's not already there:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Now you can run:
```bash
gazisiber
```

## Building a Debian/Ubuntu Package

For Debian and Ubuntu-based distributions, you can build and install a native package:

### Step 1: Install Build Dependencies

```bash
sudo apt-get update
sudo apt-get install -y debhelper python3-all python3-setuptools dh-python build-essential
```

### Step 2: Build the Package

```bash
dpkg-buildpackage -us -uc -b
```

This will create a `.deb` file in the parent directory.

### Step 3: Install the Package

```bash
sudo dpkg -i ../gazisiber-fetch_1.0.0-1_all.deb
```

### Step 4: Install Dependencies (if needed)

If there are missing dependencies, run:

```bash
sudo apt-get install -f
```

### Step 5: Run GaziSiber Fetch

```bash
gazisiber
```

## Creating a PPA Repository (For APT Installation)

To enable installation via `sudo apt install gazisiber-fetch`, you need to create a PPA (Personal Package Archive) on Launchpad:

### Prerequisites:
1. A Launchpad account
2. GPG key for signing packages
3. SSH key registered with Launchpad

### Steps:

1. **Create a PPA on Launchpad:**
   - Go to https://launchpad.net/
   - Navigate to your profile
   - Create a new PPA (e.g., `ppa:gazisiber/fetch`)

2. **Prepare the source package:**
   ```bash
   debuild -S -sa
   ```

3. **Upload to PPA:**
   ```bash
   dput ppa:gazisiber/fetch ../gazisiber-fetch_1.0.0-1_source.changes
   ```

4. **Users can then install with:**
   ```bash
   sudo add-apt-repository ppa:gazisiber/fetch
   sudo apt-get update
   sudo apt install gazisiber-fetch
   ```

## Alternative: Manual Installation

If you prefer not to use package managers:

### Step 1: Copy the script

```bash
sudo cp gazisiber_fetch.py /usr/local/bin/gazisiber
sudo chmod +x /usr/local/bin/gazisiber
```

### Step 2: Run it

```bash
gazisiber
```

## Verifying Installation

After installation, verify it works:

```bash
gazisiber
```

You should see a colorful display of your system information.

## Troubleshooting

### Command not found
If you get "command not found" after pip installation:
- Make sure `~/.local/bin` is in your PATH
- Log out and log back in, or run: `source ~/.bashrc`

### Permission denied
If you get permission errors:
- Use `sudo` for system-wide installation
- Or use `--user` flag for user installation

### Missing dependencies
If some information is missing:
- Install `lshw`: `sudo apt-get install lshw`
- Install `pciutils`: `sudo apt-get install pciutils`

## Uninstallation

### If installed with pip:
```bash
pip3 uninstall gazisiber-fetch
```

### If installed from .deb:
```bash
sudo apt remove gazisiber-fetch
```

### If installed manually:
```bash
sudo rm /usr/local/bin/gazisiber
```

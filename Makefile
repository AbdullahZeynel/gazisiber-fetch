.PHONY: install uninstall test clean

PREFIX ?= /usr/local
BINDIR = $(PREFIX)/bin
PYTHON = python3

install:
	@echo "Installing gazisiber-fetch..."
	$(PYTHON) setup.py install --user
	@echo "Installation complete! You can now run 'gazisiber' command."

install-system:
	@echo "Installing gazisiber-fetch system-wide..."
	$(PYTHON) setup.py install
	@echo "System-wide installation complete!"

uninstall:
	@echo "Uninstalling gazisiber-fetch..."
	pip3 uninstall -y gazisiber-fetch
	@echo "Uninstall complete!"

test:
	@echo "Testing gazisiber..."
	$(PYTHON) gazisiber_fetch.py

clean:
	@echo "Cleaning build artifacts..."
	rm -rf build/ dist/ *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	@echo "Clean complete!"

help:
	@echo "GaziSiber Fetch - Makefile commands:"
	@echo ""
	@echo "  make install        - Install for current user"
	@echo "  make install-system - Install system-wide (requires sudo)"
	@echo "  make uninstall      - Uninstall gazisiber-fetch"
	@echo "  make test           - Test the script"
	@echo "  make clean          - Clean build artifacts"
	@echo "  make help           - Show this help message"

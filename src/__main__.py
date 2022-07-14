"""Sample Main Project File.

This file is executed when the entire src directory is run using Python
and serves as the main entry point for the application.

Usage:
    python3 -m src - execute this program (when run from project root).

Author: Russell Feldhausen russfeld@ksu.edu
Version: 0.1
"""
import sys
from src.hello.HelloWorld import HelloWorld
HelloWorld.main(sys.argv)


# app = Web.main(sys.argv)
# app.run()

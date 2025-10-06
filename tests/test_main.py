import subprocess
import sys
import os

def run_cli(args):
    # Run the module as a script to test the entry point quickly.
    cmd = [sys.executable, "-m", "hello_cli.main"] + args
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result

def test_default_greeting():
    result = run_cli([])
    assert result.returncode == 0
    assert "Hello, World!" in result.stdout

def test_named_greeting():
    result = run_cli(["--name", "Junha"])
    assert result.returncode == 0
    assert "Hello, Junha!" in result.stdout

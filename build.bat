@echo off

python setup.py check
rmdir /s /Q dist
python -m build

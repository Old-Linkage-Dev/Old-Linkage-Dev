@echo off

twine upload dist/*
echo wait for effect
sleep 10
pip install --upgrade Old-Linkage-Dev

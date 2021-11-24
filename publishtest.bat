@echo off

twine upload --repository testpypi dist/*
echo wait for effect
sleep 10
pip install --upgrade -i https://test.pypi.org/simple/ Old-Linkage-Dev

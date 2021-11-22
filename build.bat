@echo off

python setup.py check
python -m build
twine upload --repository testpypi dist/*
pip install --upgrade -i https://test.pypi.org/simple/ Old-Linkage-Dev

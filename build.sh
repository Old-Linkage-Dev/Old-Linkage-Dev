
python3 setup.py check
python3 -m build
twine upload --repository testpypi dist/*
pip install --upgrade -i https://test.pypi.org/simple/ Old-Linkage-Dev

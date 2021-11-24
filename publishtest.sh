
twine upload --repository testpypi dist/*
sleep 10
pip install --upgrade -i https://test.pypi.org/simple/ Old-Linkage-Dev

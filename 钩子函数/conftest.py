# conftest.py
def pytest_collection_modifyitems(config, items):
    items.sort(key=lambda item: item.get_closest_marker("run").args[0])



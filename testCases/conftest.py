from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

################## Pytest HTML Report #################

def pytest_configure(config):
    config.addinivalue_line("markers", "Project_Name: nop Commerce")
    config.addinivalue_line("markers", "Module_Name: Customer")
    config.addinivalue_line("markers", "Tester: Umesh")

@pytest.hookimpl(optionalhook=True)
def pytest_collection_modifyitems(config, items):
    for item in items:
        if "Project_Name" in item.keywords:
            config._metadata['Project Name'] = item.get_closest_marker("Project_Name").args[0]
        if "Module_Name" in item.keywords:
            config._metadata['Module Name'] = item.get_closest_marker("Module_Name").args[0]
        if "Tester" in item.keywords:
            config._metadata['Tester'] = item.get_closest_marker("Tester").args[0]







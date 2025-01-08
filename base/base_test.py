import pytest
from config.data import Data
from pages.dashboard_page import DashboarPage
from pages.login_page import LoginPage
from pages.personal_page import PersonalPage



class BaseTest:

    data: Data
    login_page: LoginPage
    dashboard_page: DashboarPage
    personal_page: PersonalPage

    @pytest.fixture(autouse=True)
    def setup(self, driver, request):
        request.cls.driver = driver
        request.cls.data = Data
        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard_page = DashboarPage(driver)
        request.cls.personal_page = PersonalPage(driver)
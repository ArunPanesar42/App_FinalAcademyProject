import pytest
from config_manager import itjobswatch_home_page_test_file, itjobswatch_home_page_url, get_test_env_setting
from src.http_management.http_manager import HttpManager


class TestHttpManager:

    @pytest.fixture()
    def HttpManager(self):
        if get_test_env_setting() == 'live':
            return HttpManager(itjobswatch_home_page_url())
        else:
            return HttpManager(itjobswatch_home_page_test_file())

    def test_html_manager_file_is_opened_correctly(self, HttpManager):
        assert type(HttpManager.html) is str

    def test_incorrect_file_or_url_path_raises_name_error(self):
        with pytest.raises(NameError):
            assert HttpManager("test")

    @pytest.mark.skipif(get_test_env_setting() == 'test', reason='This test is specific to a http call and is not valid when testing locally')
    def test_html_manager_status_response_is_200(self, HttpManager):
        assert HttpManager.url_response.status_code == 200

    def test_html_manager_returns_html_from_url(self, HttpManager):
        assert 'Tracking the IT Job Market' in HttpManager.html


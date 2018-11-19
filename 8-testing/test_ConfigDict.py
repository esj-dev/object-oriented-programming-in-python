import os
import pytest
import shutil

from ConfigDict import ConfigDict


class TestConfigDict:
    """
    Creates temporary data file and runs all test associated with class.
    Executes by writing py.test in terminal.
    """

    config_test_data = 'config_test_data.txt'
    config_temp_data = 'config_temp_data.txt'

    @classmethod
    def setup_class(cls):
        shutil.copy(TestConfigDict.config_test_data, TestConfigDict.config_temp_data)

    @classmethod
    def teardown_class(cls):
        os.remove(TestConfigDict.config_temp_data)

    def test_obj(self):
        cc = ConfigDict(TestConfigDict.config_test_data)
        assert isinstance(cc, ConfigDict)
        assert isinstance(cc, dict)

    def test_filename(self):
        cc = ConfigDict(TestConfigDict.config_temp_data)
        assert TestConfigDict.config_temp_data == cc._filename

    def test_path_error(self):
        with pytest.raises(FileNotFoundError):
            ConfigDict('bad_file.txt')

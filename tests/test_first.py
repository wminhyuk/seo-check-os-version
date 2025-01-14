from seo-check-os-version
def test_first():
    assert False

from seo_check_os_version.osver import get_os_pretty_name

def test_first():
    v = get_os_pretty_name()
    assert v == "Ubuntu 24.04.1 LTS"


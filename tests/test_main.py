import pytest

from baseline_project.main import cmd_run


@pytest.mark.parametrize(
    "input_cmd",
    [
        "google.com",
        "www.google.com",
        "www.google.com/:8080",
        "; touch /tmp/banana.com"
    ],
)
def test_main(input_cmd):
    print(input_cmd)
    cmd_run(input_cmd)

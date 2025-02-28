import os
import pytest
from typing import Generator
from letta_client import Letta, LettaEnvironment


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        default="cloud",
        choices=["cloud", "localhost"],
        help="Specify the Letta environment (cloud, localhost)",
    )


@pytest.fixture(scope="session")
def letta_env(pytestconfig) -> LettaEnvironment:
    env_map = {
        "cloud": LettaEnvironment.LETTA_CLOUD,
        "localhost": LettaEnvironment.SELF_HOSTED,
    }
    env_name = pytestconfig.getoption("env")
    return env_map[env_name]


@pytest.fixture(scope="session")
def client(letta_env) -> Generator[Letta, None, None]:
    api_key = os.getenv('LETTA_API_KEY')
    #client = Letta(environment=letta_env, token=api_key)
    client = Letta(base_url="http://localhost:8283", token=api_key)
    yield client
"""Test that environment variables are set correctly."""
import os

from ou_container_builder.__main__ import run_build

from ..utils import clean_build, compare_files


BASEDIR = os.path.join('tests', 'build_test', 'env_test', 'fixtures')


def test_basic_env():
    """Test that environment variables end up in the container build."""
    context = os.path.join(BASEDIR, 'basic_env')
    clean_build(context)

    settings = {
        'module': {
            'code': 'Test',
            'presentation': '1'
        },
        'type': 'jupyter-notebook',
        'environment': [
            {'name': 'TEST', 'value': 'Testing'},
            {'name': 'OPTHOME', 'value': '/opt/home'}
        ]
    }
    result = run_build(settings, context, False, False, [])
    assert not result
    compare_files(os.path.join(context, 'EnvDockerfile'), os.path.join(context, 'Dockerfile'))

    clean_build(context)

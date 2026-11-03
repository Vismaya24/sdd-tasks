import os
import tempfile
import gc

import pytest

from app import create_app


@pytest.fixture()
def app():
    handle, database = tempfile.mkstemp(suffix=".sqlite3")
    os.close(handle)
    application = create_app({"TESTING": True, "DATABASE": database})
    yield application
    gc.collect()
    os.unlink(database)


@pytest.fixture()
def client(app):
    return app.test_client()

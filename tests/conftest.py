#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tests/conftest.py

""" Pytest configuration file. """

import os
# import shutil
# import subprocess
import sys
# import time
# from pathlib import Path

# import pytest
# import redis
# import requests
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, clear_mappers
# from tenacity import retry, stop_after_delay

# from your_pkg_name import config
# from your_pkg_name import metadata, start_mappers

# Add the project root (CWD) to sys.path
sys.path.insert(0, os.path.abspath(os.getcwd()))

# # Register the custom assertion module
# pytest.register_assert_rewrite("tests.e2e.api_client")

# @pytest.fixture
# def in_memory_sqlite_db():
#     """ Create an in-memory SQLite database. """
#     engine = create_engine("sqlite:///:memory:")
#     metadata.create_all(engine)
#     return engine


# @pytest.fixture
# def sqlite_session_factory(in_memory_sqlite_db):
#     """ Create a SQLAlchemy session factory. """
#     yield sessionmaker(bind=in_memory_sqlite_db)


# @pytest.fixture
# def mappers():
#     """ Start the SQLAlchemy mappers. """
#     start_mappers()
#     yield
#     clear_mappers()


# @retry(stop=stop_after_delay(10))
# def wait_for_postgres_to_come_up(engine):
#     """ Wait for the PostgreSQL database to come up. """
#     return engine.connect()


# @retry(stop=stop_after_delay(10))
# def wait_for_webapp_to_come_up():
#     """ Wait for the web application to come up. """
#     return requests.get(config.get_api_url())


# @retry(stop=stop_after_delay(10))
# def wait_for_redis_to_come_up():
#     """ Wait for the Redis server to come up. """
#     r = redis.Redis(**config.get_redis_host_and_port())
#     return r.ping()


# @pytest.fixture(scope="session")
# def postgres_db():
#     """ Create a PostgreSQL database. """
#     engine = create_engine(config.get_postgres_uri(), isolation_level="SERIALIZABLE")
#     wait_for_postgres_to_come_up(engine)
#     metadata.create_all(engine)
#     return engine


# @pytest.fixture
# def postgres_session_factory(postgres_db):
#     """ Create a SQLAlchemy session factory. """
#     yield sessionmaker(bind=postgres_db)


# @pytest.fixture
# def postgres_session(postgres_session_factory):
#     """ Create a SQLAlchemy session. """
#     return postgres_session_factory()


# @pytest.fixture
# def restart_api():
#     """ Restart the API. """
#     (Path(__file__).parent / "../src/allocation/entrypoints/flask_app.py").touch()
#     time.sleep(0.5)
#     wait_for_webapp_to_come_up()


# @pytest.fixture
# def restart_redis_pubsub():
#     """ Restart the Redis Pub/Sub. """
#     wait_for_redis_to_come_up()
#     if not shutil.which("docker-compose"):
#         print("skipping restart, assumes running in container")
#         return
#     subprocess.run(
#         ["docker-compose", "restart", "-t", "0", "redis_pubsub"],
#         check=True,
#     )

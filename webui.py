from __future__ import annotations

import os
import time

from modules import timer
from modules import initialize_util
from modules import initialize
from threading import Thread
from modules_forge.initialization import initialize_forge
from modules_forge import main_thread


startup_timer = timer.startup_timer
startup_timer.record("launcher")

initialize_forge()

initialize.imports()

initialize.check_versions()

initialize.initialize()


def create_api(app):
    from modules.api.api import Api
    from modules.call_queue import queue_lock

    api = Api(app, queue_lock)
    return api


def api_only_worker():
    from fastapi import FastAPI
    from modules.shared_cmd_options import cmd_opts

    app = FastAPI()
    initialize_util.setup_middleware(app)
    api = create_api(app)

    from modules import script_callbacks
    script_callbacks.before_ui_callback()
    script_callbacks.app_started_callback(None, app)

    print(f"Startup time: {startup_timer.summary()}.")
    api.launch(
        server_name=initialize_util.gradio_server_name(),
        port=cmd_opts.port if cmd_opts.port else 7861,
        root_path=f"/{cmd_opts.subpath}" if cmd_opts.subpath else ""
    )


def api_only():
    Thread(target=api_only_worker, daemon=True).start()


if __name__ == "__main__":
    from modules.shared_cmd_options import cmd_opts

    api_only()
    main_thread.loop()

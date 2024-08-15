from concurrent.futures import Future, ThreadPoolExecutor, as_completed
from typing import Any

from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    SpinnerColumn,
    TaskProgressColumn,
    TextColumn,
    TimeElapsedColumn,
    track,
)
from scrapli import Scrapli
from scrapli.response import Response


def get_output(device: dict[str, Any], command: str) -> Response:
    with Scrapli(**device) as conn:
        output = conn.send_command(command)
    return output


progress = Progress(
    # SpinnerColumn(),
    # *Progress.get_default_columns(),
    # TimeElapsedColumn(),
    SpinnerColumn(),
    TextColumn("[progress.description]{task.description}"),
    BarColumn(),
    TaskProgressColumn(),
    MofNCompleteColumn(),
    TimeElapsedColumn(),
)


def execute_tasks(devices: list[dict[str, Any]], command: str, max_workers: int = 5) -> None:
    with progress:
        task1 = progress.add_task("[red]collecting...", total=len(devices))
        with ThreadPoolExecutor(max_workers=max_workers) as pool:
            futures: dict[Future, str] = {
                pool.submit(get_output, scrapli, command): host for host, scrapli in devices.items()
            }

            for f in as_completed(futures):
                progress.update(task1, advance=1)
                host = futures.get(f)
                exc = f.exception()

                if exc is not None:
                    print(f"{host}: результат: 'ошибка выполнения, {exc.__class__.__name__}: {str(exc)}'")
                else:
                    print(f"{host}: результат: '{f.result().result}'")

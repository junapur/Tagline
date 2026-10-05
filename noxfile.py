import nox
import nox_uv

nox.options.default_venv_backend = "uv"
nox.options.sessions = ["lint", "type_check"]
nox.options.error_on_external_run = True


@nox_uv.session(venv_backend="none")
def type_check(session: nox.Session) -> None:
    session.run("pyrefly", "check")


@nox_uv.session(venv_backend="none")
def lint(session: nox.Session) -> None:
    session.run("ruff", "format", "--check")
    session.run("ruff", "check", "--no-fix")


@nox_uv.session(venv_backend="none")
def tidy(session: nox.Session) -> None:
    session.run("ruff", "format")
    session.run("ruff", "check", "--fix")

import hashlib

from mcp.server.fastmcp import FastMCP

EMAIL = "23f2000797@ds.study.iitm.ac.in"

mcp = FastMCP("exam-server")


@mcp.tool()
def solve_challenge() -> str:
    """
    Returns the first 16 hex chars of
    SHA256(challenge:normalized_email)
    """

    headers = mcp.request_context.headers

    challenge = headers.get("x-exam-challenge", "")

    digest = hashlib.sha256(
        f"{challenge}:{EMAIL}".encode()
    ).hexdigest()

    return digest[:16]


app = mcp.streamable_http_app()

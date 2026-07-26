import hashlib
from fastmcp import FastMCP

EMAIL = "23f2000797@ds.study.iitm.ac.in"

mcp = FastMCP("exam-server")

@mcp.tool
def solve_challenge() -> str:
    headers = mcp.request_context.headers
    challenge = headers.get("x-exam-challenge", "")
    return hashlib.sha256(
        f"{challenge}:{EMAIL}".encode()
    ).hexdigest()[:16]

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8000,
    )


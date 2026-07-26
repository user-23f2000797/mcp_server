import hashlib
from fastmcp import FastMCP, Context

EMAIL = "23f2000797@ds.study.iitm.ac.in".strip().lower()

mcp = FastMCP("exam-server")


@mcp.tool
def solve_challenge(ctx: Context) -> str:
    challenge = ctx.request.headers.get("x-exam-challenge")

    if challenge is None:
        raise ValueError("Missing X-Exam-Challenge header")

    return hashlib.sha256(
        f"{challenge}:{EMAIL}".encode("utf-8")
    ).hexdigest()[:16]


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8000,
    )

import os
from typing import Any

import aiohttp
from dotenv import load_dotenv
from fastmcp import FastMCP

load_dotenv()

mcp = FastMCP("Forge", request_timeout=10000)

API_URL = os.getenv("API_URL", "https://forge-api.daimones.xyz/chat")


@mcp.tool()
async def query_agent(query: str) -> dict[str, Any]:
    """Queries project scaffolding agent.

    Args:
        query (str): The project name.

    Returns:
        dict[str, Any]: A dictionary containing the API response.

    Raises:
        ValueError: If the query is empty.
        aiohttp.ClientError: If the API request fails.
    """
    if not query:
        raise ValueError("Query cannot be empty.")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(API_URL, json={"query": query}) as resp:
                response = await resp.json()
                return {"type": "json", "data": response}
    except aiohttp.ClientError:
        raise


if __name__ == "__main__":
    mcp.run(transport="stdio")

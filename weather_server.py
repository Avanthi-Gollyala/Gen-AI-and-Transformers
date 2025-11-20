#pip install mcp[cli]
import asyncio
from typing import Any
import json
import requests 
from mcp.server.fastmcp import FastMCP 

# Initialize FastMCP server
mcp = FastMCP("weather_server")

#defining constants
weather_api_base = "https://wttr.in"
user_agent = "weather-mcp-server/1.0"

# defining the MCP tools
@mcp.tool()
def get_weather_info(location: str) -> str:
    """Get Weather information for a given location.
    
    Args:
        location (str): The location for which to get the weather information. The location needs to be a proper city name like Mumbai, Tokyo etc.
    """
    
    url = f"{weather_api_base}/{location}?format=j1"
    
    response = requests.get(url)
    
    return str(response.json())

if __name__ == "__main__":
    # initialize and start the MCP server
    mcp.run()
    
    
import os 
import requests 
from dotenv import load_dotenv 
from mcp.server.fastmcp import FastMCP

load_dotenv()
TOKEN_GIT = os.getenv("TOKEN_GIT")
if not TOKEN_GIT:
    raise ValueError("TOKEN_GIT is missing from .env")

mcp = FastMCP("Github mcp serevr")
HEADERS = {"Accept":"application/vnd.github+json",
           "Authorization":f"Bearer {TOKEN_GIT}",
           "X-Github-Api-Version": "2026-03-10"
}

@mcp.tool()
def search_repositories(query: str) -> list:
    response = requests.get(
        "https://api.github.com/search/repositories",
        headers=HEADERS,
        params={
            "q": query,
            "per_page":10
        }
    )
    response.raise_for_status()
    data = response.json()
    results =[]
    for repo in data["items"]:
        results.append({
            "name":repo["name"],
            "creator":repo["owner"]["login"],
            "url":repo["html_url"]
        })
    return results 

@mcp.tool()
def search_users(query: str) -> list:
    response = requests.get(
        f"https://api.github.com/users/{query}",
        headers=HEADERS,
    )

    response.raise_for_status()
    user = response.json()
    return[{
        "username": user["login"],
        "repositories": user["public_repos"],
        "followers": user["followers"],
        "profile_url": user["html_url"]                          
    }]

if __name__ == "__main__":
    mcp.run()


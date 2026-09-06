import sys
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client 
server_params = StdioServerParameters(
    command=sys.executable,
    args=["server.py"]
)

async def main():
    async with stdio_client(server_params) as (read,write):
        async with ClientSession(read,write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("\nAvailable MCP tools:")
            for i,tool in enumerate(tools.tools,1):
                print(f"{i}.{tool.name}")
            choice = input("\nChoose a tool (1/2):")
            if choice == "1":
                repo = input("\nenter repo search:")
                result = await session.call_tool(
                    "search_repositories",
                    {"query": repo}
                )
                print("\nRepository results:")
                print(result.content)
            elif choice == "2":
                user = input("\n enter github username:")
                result = await session.call_tool(
                    "search_users",
                    {"query":user}
                )
                print("\nuser result:")
                print(result.content)
            else:
                print("\n invalid choice . please choose 1 or 2")
if __name__ == "__main__":
    asyncio.run(main())
    




from fastmcp import FastMCP

mcp = FastMCP("init MCP server")

def main():
    mcp.run()
    print("Hello from n8n-builder-mcp!")


if __name__ == "__main__":
    main()

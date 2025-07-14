# Forge MCP Server

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/)
[![MCP](https://img.shields.io/badge/MCP-Model%20Control%20Protocol-green.svg)](https://github.com/lmql-lang/mcp)
[![MCP Server](https://img.shields.io/badge/MCP%20Server-FastMCP-orange.svg)](https://github.com/lmql-lang/mcp)

A Model Control Protocol (MCP) server for the Forge project scaffolding agent. This server acts as a bridge between Large Language Models (LLMs) and the Forge API, enabling AI assistants to scaffold new projects based on user requirements.

![MCP Inspector Screenshot](assets/mcp-inspector-screenshot.jpg)

## Overview

Forge MCP Server uses the FastMCP framework to create tools that LLMs can use to interact with the Forge project scaffolding API. This allows AI assistants to generate project structures, boilerplate code, and configurations based on natural language descriptions.

## Features

- Easy integration with LLMs using the Model Control Protocol
- Connection to the Forge project scaffolding API
- Simple query interface for project generation
- Error handling and timeout management

## Prerequisites

- Python 3.13+
- Pipenv

## Installation

Clone the repository:

```bash
git clone https://github.com/believemanasseh/forge-mcp.git
cd forge-mcp
```

Install dependencies:

```bash
pipenv --python 3.13
source .venv/bin/activate
pipenv install
```

## Development

### Running the Server

```bash
fastmcp dev server.py
```

The server uses stdio for communication by default, making it compatible with various LLM integration frameworks.

### API Reference

#### `query_agent`

Sends request queries to the Forge API and returns the results.

**Parameters:**

- `query` (string): Natural language description of the project to scaffold

**Returns:**

- JSON response from the Forge API

**Example:**

```txt
query_agent("Create a Django project named deet.")
```

## Integration with MCP Hosts

Select your favourite host from the options below and follow the configuration instructions.

### Integrating Cursor

Update your Cursor configuration file at `~/.cursor/mcp.json` or `.cursor/mcp.json`:

```json
{
    "mcpServers": {
        "forge-mcp": {
        "command": "pipenv",
        "args": ["run", "fastmcp", "run", "server.py"],
        "transport": "stdio"
        }
    }
}
```

### Integrating Claude Desktop

In Claude Desktop, go to `Settings > Developer > Edit Config`. Replace the configuration with:

```json
{
    "mcpServers": {
        "forge-mcp": {
            "command": "pipenv",
            "args": [
                "run",
                "fastmcp",
                "run",
                "server.py"
            ],
            "cwd": "/path/to/your/forge-mcp"
        }
    }
}
```

*Note: Replace `/path/to/your/forge-mcp` with the absolute path to your cloned `forge-mcp` directory.*

### Integrating VSCode

Update the VSCode workspace configuration file at `.vscode/mcp.json`:

```json
{
    "servers": {
        "forge-mcp": {
            "type": "stdio",
            "command": "pipenv",
            "args": ["run", "fastmcp", "run", "server.py"],
        }
    }
}
```

## Contributing

We welcome contributions to the Forge MCP Server project! Here's how you can contribute:

1. **Fork the repository** - Create your own fork of the project
2. **Create a feature branch** - `git checkout -b feature/your-feature-name`
3. **Commit your changes** - Make sure to write clear commit messages
4. **Push to your branch** - `git push origin feature/your-feature-name`
5. **Open a pull request** - Describe the changes you've made and why they should be included

### Development Guidelines

- Follow PEP 8 style guidelines for Python code
- Write docstrings for all functions, classes, and methods
- Add appropriate unit tests for new features
- Update documentation to reflect any changes

## License

[Apache License 2.0](LICENSE)

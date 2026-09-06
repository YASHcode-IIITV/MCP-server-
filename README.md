# Multi-Service MCP Server

A modular **Model Context Protocol (MCP) server** built with Python that connects an MCP client to multiple external APIs through MCP tools.

## Services

### 🐙 GitHub MCP
- Search GitHub repositories
- Look up GitHub users
- GitHub API authentication using environment variables

### 🌦️ Weather MCP
- Get weather information for a location
- Retrieve weather forecasts
- Access weather data through MCP tools

### 🚀 NASA MCP
- Access NASA astronomy data
- Retrieve space and planetary information
- Search and retrieve NASA images and related data

## Architecture

```text
                 MCP Client
                     │
                     ▼
              ┌──────────────┐
              │  MCP Server  │
              └──────┬───────┘
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       GitHub      Weather      NASA
        MCP          MCP         MCP
          │          │           │
          ▼          ▼           ▼
     GitHub API   Weather API  NASA API

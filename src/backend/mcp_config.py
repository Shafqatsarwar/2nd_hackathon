"""
Model Context Protocol (MCP) Configuration for Backend Services

This configuration enables the backend to work with MCP-enabled clients
such as Claude Code and other AI assistants that support the protocol.
"""
import os
from typing import Dict, Any, Optional
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings


class MCPConfig(BaseSettings):
    """
    Model Context Protocol Configuration Settings
    """
    # MCP Server Configuration
    MCP_SERVER_ENABLED: bool = True
    MCP_SERVER_HOST: str = "0.0.0.0"
    MCP_SERVER_PORT: int = 8080

    # Authentication for MCP endpoints
    MCP_AUTH_TOKEN: Optional[str] = Field(default_factory=lambda: os.getenv("MCP_AUTH_TOKEN"))

    # API endpoint configuration
    MCP_API_BASE_URL: str = "/mcp"

    # Context provider configuration
    MCP_CONTEXT_PROVIDERS: Dict[str, Any] = {
        "todo-context": {
            "name": "Todo Application Context",
            "description": "Provides context about the todo application structure and current state",
            "enabled": True
        },
        "database-context": {
            "name": "Database Schema Context",
            "description": "Provides database schema information for the todo application",
            "enabled": True
        },
        "auth-context": {
            "name": "Authentication Context",
            "description": "Provides information about authentication system and user management",
            "enabled": True
        }
    }

    # MCP Client Configuration (for connecting to other MCP services)
    MCP_CLIENT_ENABLED: bool = False
    MCP_CLIENT_SERVER_URL: Optional[str] = None

    class Config:
        env_prefix = "MCP_"


# Global MCP configuration instance
mcp_config = MCPConfig()


def get_mcp_config() -> MCPConfig:
    """
    Retrieve the global MCP configuration instance
    """
    return mcp_config


def is_mcp_enabled() -> bool:
    """
    Check if MCP functionality is enabled
    """
    return mcp_config.MCP_SERVER_ENABLED
class ConfigurationError(Exception):
    """Raised when application configuration is invalid."""


class ValidationError(Exception):
    """Raised when user input is invalid."""


class AIProviderError(Exception):
    """Raised when communication with the AI provider fails."""
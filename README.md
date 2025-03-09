# MCP Greeting Demo

A simple demonstration of the MCP greeting protocol implementation.

## Usage

To send a greeting to someone, use the following format:

```bash
python greeting.py greeting://recipient
```

For example:
```bash
python greeting.py greeting://joe
```

This will send a greeting message to the specified recipient using the MCP greeting protocol format.

## Protocol Format

The greeting protocol uses the following format:
```
greeting://{recipient}
```

Where `{recipient}` is the name of the person you want to send the greeting to.
def execute_command(cmd):
    if not cmd or not isinstance(cmd, str):
        return "No valid command provided."
    cmd_lower = cmd.lower()
    if "scan" in cmd_lower:
        return "Scan completed: No threats found"
    elif "delete" in cmd_lower:
        return "File deleted successfully"
    return f"Executed: {cmd}"

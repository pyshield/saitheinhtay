def require_non_empty(value: str, field_name: str = "value") -> str:
    if not value or not value.strip():
        raise ValueError(f"{field_name} cannot be empty")
    return value.strip()

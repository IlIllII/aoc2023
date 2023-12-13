
def load_input(file_name: str) -> list[str]:
    with open(file_name, 'r') as f:
        return f.read().splitlines()

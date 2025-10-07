from pathlib import Path

def find(path: str | Path, filename: str) -> list[Path]:
    """
    Recursively collect all entries named `filename` under `path`.
    Returns a list of absolute Paths.
    """
    root = Path(path)
    results: list[Path] = []

    def dfs(cur: Path):
        try:
            for entry in cur.iterdir():
                # record a match (file or directory) by exact name
                if entry.name == filename:
                    try:
                        results.append(entry.resolve())
                    except Exception:
                        results.append(entry)  # fallback if resolve fails
                # recurse into directories
                if entry.is_dir():
                    # avoid following symlinked dirs to prevent cycles
                    if not entry.is_symlink():
                        dfs(entry)
        except PermissionError:
            # skip folders we can't read
            pass
        except FileNotFoundError:
            # race condition if the dir disappears
            pass

    if root.is_dir():
        dfs(root)
    else:
        # if root is a file, check its name directly
        if root.name == filename:
            results.append(root.resolve())
    return results

if __name__ == "__main__":
    # Example: look inside your Medical Books\Surgery folder for a file
    path = r"C:\Users\dartb\OneDrive\Documents\health infomatics\Books\SQL"
    filename = "sqlsingleRowFunctions.pdf"
    matches = find(path, filename)
    if matches:
        print("Found:")
        for m in matches:
            print(m)
    else:
        print("No matches found.")

import os
import subprocess

def generate_preview():
    """
    Generate a human-readable preview document summarizing recent changes in the codebase.
    """
    # Define paths
    root_path = os.path.abspath(os.path.dirname(__file__))
    diff_output_file = os.path.join(root_path, "Documentation", "Changes_Preview.md")
    documentation_dir = os.path.dirname(diff_output_file)

    # Ensure the Documentation directory exists
    if not os.path.exists(documentation_dir):
        os.makedirs(documentation_dir)

    try:
        # Run git diff to get recent changes
        git_diff = subprocess.check_output(["git", "diff"], universal_newlines=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to retrieve git diff: {e}")

    if not git_diff.strip():
        raise ValueError("No changes detected in the git diff.")

    # Parse the git diff
    diff_lines = git_diff.splitlines()
    formatted_diff = ["# Recent Code Changes\\n"]
    current_file = None

    for line in diff_lines:
        if line.startswith("diff --git"):
            # Extract file name
            parts = line.split(" ")
            current_file = parts[-1] if len(parts) > 2 else None
            if current_file:
                formatted_diff.append(f"\\n## {current_file}\\n")
        elif line.startswith("+") and not line.startswith("+++"):
            # Added lines
            formatted_diff.append(f"- **Added**: {line[1:].strip()}")
        elif line.startswith("-") and not line.startswith("---"):
            # Removed lines
            formatted_diff.append(f"- **Removed**: {line[1:].strip()}")

    # Write the formatted diff to the markdown file
    with open(diff_output_file, "w") as f:
        f.write("\\n".join(formatted_diff))

    print(f"Changes preview saved to {diff_output_file}")

if __name__ == "__main__":
    generate_preview()
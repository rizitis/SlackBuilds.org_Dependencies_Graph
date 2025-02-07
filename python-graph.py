import json
import graphviz
import os
import re

# Path to the JSON file
json_file = "/var/lib/slpkg/repos/ponce/data.json"

# Load JSON data
with open(json_file, "r") as f:
    data = json.load(f)

# Create output directory if not exists
output_dir = "dependency_graphs"
os.makedirs(output_dir, exist_ok=True)

# Function to sanitize names for Graphviz
def sanitize_name(name):
    """Removes or replaces problematic characters for Graphviz"""
    return re.sub(r'[^a-zA-Z0-9_-]', '_', name)  # Replace special chars with "_"

# Generate dependency graph for each package
for package, details in data.items():
    if "requires" in details and details["requires"]:
        dependencies = details["requires"]

        # Initialize Graphviz Digraph
        dot = graphviz.Digraph(format="png")

        # Sanitize package name
        safe_package = sanitize_name(package)
        dot.node(safe_package, shape="box", style="filled", fillcolor="lightblue")

        # Add dependency nodes and edges
        for dep in dependencies:
            safe_dep = sanitize_name(dep)  # Sanitize dependency name
            dot.node(safe_dep, shape="ellipse", style="filled", fillcolor="lightgray")
            dot.edge(safe_package, safe_dep)

        # Render and save the graph
        output_path = os.path.join(output_dir, f"{safe_package}_dependencies")
        try:
            dot.render(output_path, format="png", cleanup=True)
            print(f"Graph saved: {output_path}.png")
        except graphviz.backend.execute.CalledProcessError as e:
            print(f"⚠️ Error processing {package}: {e}")

print("All dependency graphs generated successfully!")

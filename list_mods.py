
import os

ignore =[".gitattributes", ".gitignore", "README.md", "list_mods.py", ".git", ".idea", "allmods.md"]
mods = []
dependencies = []
total = 0

# Loop through every file in the current directory
for filename in os.listdir('.'):
    # Ignore files that are in the ignore list
    if filename not in ignore:
        # Clean the filename
        filename = filename.replace(".jar", "")
        filename = filename.replace("-", " ")

        total += 1

        # If the file starts with DEP_ then it is a dependency
        if filename.startswith("DEP_"):
            dependencies.append(filename)
        else:
            mods.append(filename)


# write a header to the file allmods.md and open it for writing
with open("allmods.md", "w") as f:
    f.write(f"# All Mods | {len(dependencies) + len(mods)} total \n\n")

    # Write the dependencies to the file
    f.write(f"## Dependencies | {len(dependencies)} total \n")
    for dep in dependencies:

        version = dep.split("_")[2]
        version = version.replace("V", "")
        name = dep.split("_")[1]

        f.write("* **" + name + "** " + version + "\n")
    # Write the mods to the file
    f.write(f"\n## Mods | {len(mods)} total \n")
    for mod in mods:
        version = mod.split("_")[1]
        version = version.replace("V", "")
        name = mod.split("_")[0]

        f.write("* **" + name + "** " + version + "\n")

    # Close the file
    f.close()


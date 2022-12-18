import os

ignore = [".gitattributes", ".gitignore", "README.md", "list_mods.py", ".git", ".idea", "changelogs.md"]
mods = []
dependencies = []
total = 0

# Loop through every file in the current directory
for filename in os.listdir('.'):
    # Check if file has .jar
    if filename.endswith(".jar"):
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
with open("README.md", "w") as f:
    f.write("Generated by [**list_mods.py**](list_mods.py), I will not correct incorrect information.\nLinks may not show the mod\n\n")
    f.write("View changes to the mod pack [**here**](https://github.com/j1165-mods/mods/commits/main)\n\n")
    f.write(f"# All Mods | {len(dependencies) + len(mods)} total \n\n")

    # Write the dependencies to the file
    f.write(f"## Dependencies | {len(dependencies)} total \n")
    for dep in dependencies:
        version = dep.split("_")[2]
        version = version.replace("V", "")
        name = dep.split("_")[1]
        link = "https://www.curseforge.com/minecraft/mc-mods/search?search=" + name.lower().replace(" ", "-")

        f.write("* [**" + name + "**](" + link + ") " + version + "\n")
    # Write the mods to the file
    f.write(f"\n## Mods | {len(mods)} total \n")
    for mod in mods:
        print(mod)
        version = mod.split("_")[1]
        version = version.replace("V", "")
        name = mod.split("_")[0]
        link = "https://www.curseforge.com/minecraft/mc-mods/search?search=" + name.lower().replace(" ", "-")

        f.write("* [**" + name + "**](" + link + ") " + version + "\n")

    # Close the file
    f.close()

print("Done")
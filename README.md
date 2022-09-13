# SRModsList
Listing of valid mods per Synthriderz version, for [Noodle Manager X](https://github.com/tommaier123/NoodleManagerX) mod download support.

## Adding New Mods/Versions
1. Update mods.json
2. If a new mod, add a folder under Downloads named after the mod's id/name
3. Create a new zip folder named "{modid}_{version}.synthmod" containing:
    - A LocalItem.json with the following format (replace modId):
    ```
    {
        "hash": "modId"
    }
    ```
    - All necessary mod files that aren't found in linked dependencies, in a file structure relative to the base SynthRiders directory (see existing .synthmod files for examples)
4. Push to separate branch and verify download in Noodle Manager X (update apiEndpoint in ModHandler)
5. Create PR against main/master branch
6. Mod must be verified to be safe to install by at least one other person (preferably more)
    - Not malware
    - Not cheats/hacks
    - Not breaking main game functionality

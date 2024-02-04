# mawscan

This malware scanner will first <b>index files</b> and then will perform <b>scanning</b> on select indexed files.

### WHAT PROCESSES ARE CACHED ?

|  | INDEX | SCAN | 
| - | - | - |
| CACHE | cached | not cached | 

Essentially, the program will not repeat the <b>INDEXING PROCESS</b> for subsequent scans.

### WHAT PROCESS WILL THE PROGRAM PERFORM ?

|  | INDEX + SCAN | ONLY SCAN |
| - | - | - |
| FLAG | with --index flag | default (if db is cached) |

If there has been a change in the filesystem then user can force <b>INDEXING PROCESS</b> and update the cache.

### NOTE - 

`YOU DO NOT REQUIRE --INDEX FLAG FOR YOUR FIRST USE OF THE TOOL`

The tool will automatically index the filesystem. The flag is only required on subsequent scans.


### TODOs

- [ ] Include ARGSPARSE
- [ ] Exclude Folders
- [ ] Exclude FileTypes
- [ ] Restrict Scan Scope
- [ ] Proper Documentation
- [ ] dotenv config for locations
- [ ] status of completion - database created ? manual control over rescan of files

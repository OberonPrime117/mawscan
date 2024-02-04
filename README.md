# mawscan

This malware scanner will first <b>index files</b> and then will perform <b>scanning</b> on select indexed files.

### WHAT PROCESSES ARE CACHED ?

|  | INDEX | SCAN | 
| - | - | - |
| CACHE | cached | not cached | 

Essentially, the program will not repeat the <b>INDEXING PROCESS</b> for subsequent scans.

### WHAT PROCESS WILL THE PROGRAM PERFORM ?

|  | INDEX + SCAN | ONLY SCAN | ONLY INDEX |
| - | - | - | - |
| FLAG | with --index flag | default (if db is cached) | with --noscan flag |

If there has been a change in the filesystem then user can force <b>INDEXING PROCESS</b> and update the cache.

If your filesystem is huge and system specs are low then <b>INDEXING + SCANNING</b> can take quite a long time. Refresh cache without committing time for a scan.

### NOTE - 

`YOU DO NOT REQUIRE --INDEX FLAG FOR YOUR FIRST USE OF THE TOOL`

The tool will automatically index the filesystem. The flag is only required on subsequent scans.


### TODOs

- [x] Include ARGSPARSE
- [ ] Exclude Folders
- [ ] Exclude FileTypes
- [ ] Restrict Scan Scope
- [ ] Proper Documentation
- [x] dotenv config for locations
- [x] status of completion - database created ? manual control over rescan of files

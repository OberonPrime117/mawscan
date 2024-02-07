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

### RECOMMENDATIONS

For YARA rules, I recommend the following repository ->

`git clone https://github.com/Yara-Rules/rules.git`

### FLAGS

`python runme.py --help`

`usage: runme.py [-h] [-i] [-ns] [-t THREADS]`

#### `-h` // `--help`

Show this help message and exit

#### `-i` // `--index`

Refresh indexing cache

#### `-ns` // `--noscan`

Perform only file indexing, no scan

#### `-t THREADS` // `--threads THREADS`

Specify the number of threads required for scanning (default=10)

#### `-p PROCESSES` // `--processes PROCESSES`

Specify the number of processes required for scanning (default=10)


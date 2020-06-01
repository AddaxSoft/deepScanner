# deepScanner
a tiny script to use nmap script scan on a previous nmap SYN (lighter) scans results

# usage
`python deepscanner.py nmap-results.xml`

# generating light fast nmap scan report to feedin
the nmap output you need to feed in into the script are the XML output of a large scope scan. Example syntax:

    nmap -n -Pn -sS -p- -T4 --max-rtt-timeout 300ms --stats-every 15m --open -oX results.xml -iL largeScopeList.txt`

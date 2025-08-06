#!/bin/bash

# 1. Log Running Processes
DATE=$(date +%F)
PROCESS_LOG="process_log_$DATE.log"

echo "🔍 Logging running processes to $PROCESS_LOG..."
ps aux > "$PROCESS_LOG"

# 2. Check for High Memory Usage
echo "🔎 Checking for processes using more than 30% memory..."
HIGH_MEM_PROCESSES=$(ps aux --sort=-%mem | awk '$4 > 30')

if [ ! -z "$HIGH_MEM_PROCESSES" ]; then
    echo "⚠️ Warning: Processes using more than 30% memory found!"
    echo "$HIGH_MEM_PROCESSES" >> high_mem_processes.log
else
    echo "✅ No processes are using more than 30% memory."
fi

# 3. Check Disk Space on Root (/)
DISK_USAGE=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')

echo "💽 Checking disk space on / partition..."
if [ "$DISK_USAGE" -gt 80 ]; then
    echo "⚠️ Warning: Disk usage on / is above 80% (currently ${DISK_USAGE}%)"
else
    echo "✅ Disk usage on / is under control (${DISK_USAGE}%)"
fi

# 4. Display Summary
TOTAL_PROCESSES=$(ps aux | wc -l)
HIGH_MEM_COUNT=$(echo "$HIGH_MEM_PROCESSES" | wc -l)

echo
echo "📊 ===== System Health Summary ====="
echo "🔢 Total running processes: $TOTAL_PROCESSES"
echo "🔥 Processes >30% memory: $HIGH_MEM_COUNT"
echo "💾 Disk usage on /: ${DISK_USAGE}%"
echo "===================================="

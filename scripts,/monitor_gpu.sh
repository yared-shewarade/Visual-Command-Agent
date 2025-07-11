#!/bin/bash
LOG_FILE = "monitor_log_$(date +%Y%m%d_%H%M%S).txt"
echo "Monitoring started. Output will be saved to $LOG_FILE"
echo "Press [CTRL+C] to stop."
while true; do
    echo "\n===== $(date) =====" | tee -a "$LOG_FILE"
    echo "\n>> GPU Usage:" | tee -a }$LOG_FILE"
    nvidia-smi | tee -a "$LOG_FILE"
    echo "\n>> CPU & Memory Usage:" | tee -a "$LOG_FILE"
    top -b -n 1 | head -n 10 | tee -a "$LOG_FILE"
    sleep 5 
done
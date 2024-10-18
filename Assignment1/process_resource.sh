#!/bin/bash

if [ $# -lt 2 ]; then
    echo "Usage: $0 <PID> <duration_in_seconds>"
    exit 1
fi

PID=$1
DURATION=$2

if ! ps -p $PID > /dev/null; then
    echo "Process with PID $PID does not exist."
    exit 1
fi

PROCESS_NAME=$(ps -p $PID -o comm=)
echo "Monitoring process: $PROCESS_NAME (PID: $PID) for $DURATION seconds"

# Temporary file to store data
TEMP_FILE=$(mktemp)

# Function to get resource usage
get_resource_usage() {
    top -b -n 1 -p $PID | tail -n 1 | awk '{print $9 "," $10 "," $11 "," $12}'
}

# Collect data
echo "Timestamp,CPU%,MEM%,VIRT,RES" > $TEMP_FILE
start_time=$(date +%s)
end_time=$((start_time + DURATION))

while [ $(date +%s) -lt $end_time ]; do
    timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    usage=$(get_resource_usage)
    echo "$timestamp,$usage" >> $TEMP_FILE
    sleep 1
done

# Process and summarize data
echo "Resource Utilization Summary for $PROCESS_NAME (PID: $PID)"
echo "Duration: $DURATION seconds"
echo "---------------------------------------------------"

# CPU Usage
echo "CPU Usage (%):"
awk -F',' '{print $2}' $TEMP_FILE | tail -n +2 | sort -n | awk '
BEGIN {
    count = 0
    sum = 0
}
{
    count++
    sum += $1
    values[count] = $1
}
END {
    if (count > 0) {
        avg = sum / count
        if (count % 2) {
            median = values[int(count/2) + 1]
        } else {
            median = (values[count/2] + values[count/2 + 1]) / 2
        }
        print "  Min:    " values[1]
        print "  Max:    " values[count]
        print "  Avg:    " avg
        print "  Median: " median
    } else {
        print "  No data collected"
    }
}'

# Memory Usage
echo -e "\nMemory Usage:"
awk -F',' '{print $3 "," $4 "," $5}' $TEMP_FILE | tail -n +2 | sort -n | awk '
BEGIN {
    count = 0
    sum_mem_percent = 0
    sum_virt = 0
    sum_res = 0
}
{
    count++
    sum_mem_percent += $1
    sum_virt += $2
    sum_res += $3
    mem_percent[count] = $1
    virt[count] = $2
    res[count] = $3
}
END {
    if (count > 0) {
        print "  Memory % (Min/Avg/Max): " mem_percent[1] " / " sum_mem_percent/count " / " mem_percent[count]
        print "  VIRT (Min/Avg/Max):     " virt[1] " / " sum_virt/count " / " virt[count]
        print "  RES (Min/Avg/Max):      " res[1] " / " sum_res/count " / " res[count]
    } else {
        print "  No data collected"
    }
}'

# Clean up
rm $TEMP_FILE

echo -e "\nNote: VIRT and RES are typically in KB unless otherwise specified by top"
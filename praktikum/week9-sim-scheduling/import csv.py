import csv

# Membaca dataset dari CSV
processes = []
with open("dataset.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        processes.append({
            "process": row["Process"],
            "arrival": int(row["ArrivalTime"]),
            "burst": int(row["BurstTime"])
        })

# Urutkan berdasarkan Arrival Time (FCFS)
processes.sort(key=lambda x: x["arrival"])

current_time = 0
total_waiting = 0
total_turnaround = 0

print("=== SIMULASI CPU SCHEDULING FCFS ===\n")
print(f"{'Proses':<8}{'Arrival':<10}{'Burst':<8}{'Waiting':<10}{'Turnaround':<12}")

for p in processes:
    if current_time < p["arrival"]:
        current_time = p["arrival"]

    waiting_time = current_time - p["arrival"]
    turnaround_time = waiting_time + p["burst"]

    total_waiting += waiting_time
    total_turnaround += turnaround_time

    print(f"{p['process']:<8}{p['arrival']:<10}{p['burst']:<8}{waiting_time:<10}{turnaround_time:<12}")

    current_time += p["burst"]

n = len(processes)
print("\nRata-rata Waiting Time     :", total_waiting / n)
print("Rata-rata Turnaround Time :", total_turnaround / n)


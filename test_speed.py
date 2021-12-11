import os, runpy, time

folders = [filename for filename in os.listdir() if os.path.isdir(os.path.join(filename)) if filename[0] != "."]

times = [time.perf_counter()]
for folder in folders:
    runpy.run_path(f"{folder}\\part1.py")
    times.append(time.perf_counter())    
    runpy.run_path(f"{folder}\\part2.py")
    times.append(time.perf_counter())
    
for i, folder in enumerate(folders):
    part1_time = '{:.4f}'.format(round(times[i*2+1]-times[i*2], 4))
    part2_time = '{:.4f}'.format(round(times[i*2+2]-times[i*2+1], 4))
    print(folder, end=" | ")
    print(f"part1 -> {part1_time}s", end=" | ")
    print(f"part2 -> {part2_time}s")

print(f"Total time: {round(times[-1]-times[0], 4)}s")
import os, runpy, timeit

folders = [filename for filename in os.listdir() if os.path.isdir(os.path.join(filename)) if filename[0] != "."]

times = [timeit.default_timer()]
for folder in folders:
    if folder == "06":
        runpy.run_path(f"{folder}\\part1_fast.py")
    else:
        runpy.run_path(f"{folder}\\part1.py")
    times.append(timeit.default_timer())    
    if folder != "07":
        runpy.run_path(f"{folder}\\part2.py")
    else:
        runpy.run_path(f"{folder}\\part2_fast.py")
    times.append(timeit.default_timer())

part1_total = 0
part2_total = 0
for i, folder in enumerate(folders):
    part1_time = '{:.4f}'.format(round(times[i*2+1]-times[i*2], 4))
    part2_time = '{:.4f}'.format(round(times[i*2+2]-times[i*2+1], 4))
    part1_total += times[i*2+1]-times[i*2]
    part2_total += times[i*2+2]-times[i*2+1]
    print(folder, end=" | ")
    print(f"part1 -> {part1_time}s", end=" | ")
    print(f"part2 -> {part2_time}s")

print(f"Total time: {round(times[-1]-times[0], 4)}s")
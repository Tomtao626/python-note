import psutil

cpu_login_nums = psutil.cpu_count()
print(cpu_login_nums)
cpu_login_nums = psutil.cpu_count(logical=False)
print(cpu_login_nums)

# cpu性能
print(psutil.cpu_times().idle)
print(psutil.cpu_times()[2])
# 内存信息
print(psutil.virtual_memory())
print(psutil.virtual_memory().percent)
# 虚拟内存信息
print(psutil.swap_memory())
print(psutil.swap_memory().percent)
# 磁盘容量
print(psutil.disk_usage('/'))
# 磁盘分区
print(psutil.disk_partitions())
# 磁盘IO
print(psutil.disk_io_counters())
# 网络IO
print(psutil.net_io_counters())
print(psutil.net_io_counters(pernic=True))

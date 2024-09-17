from datetime import datetime

import platform
import psutil


class SystemInfo:

    def get_size(self, bytes: int = 0, sufix: str = "b") -> str:
        """
        bytes : int Amount of byts need to convert
        """
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes: .2f} {unit}{sufix}"
            bytes /= factor

    def get_platfrom_info(self, ) -> list[any]:
        uname = platform.uname()
        return [uname.system, uname.node, uname.release, uname.version, uname.machine, uname.processor]

    def boot_time_start(self) -> list[any]:
        boot_time_timestop = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestop)
        return [f"{bt.day}/{bt.month}/{bt.day}", f"{bt.hour}:{bt.minute}:{bt.second}"]

    def get_vmem(self) -> list[str]:
        svmem = psutil.virtual_memory()
        return [self.get_size(info) if isinstance(info, int) else f"{info}%" for info in svmem]

    def get_disk_usage(self):
        partitions, info, disk_info = psutil.disk_partitions(), [], []
        for partition in partitions:
            info.append({partition.device: {"mountpoint": partition.mountpoint, "fstype": partition.fstype}})
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except:
                continue
            for _ in partition_usage:
                disk_info.append([
                    self.get_size(data) if isinstance(data, int) else f"{data}%"
                    for data in partition_usage
                ])
        storage_info = list(set(tuple(sorted(sub)) for sub in disk_info))
        
        return [storage_info, info]



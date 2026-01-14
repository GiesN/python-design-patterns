from abc import ABC, abstractmethod


class Device(ABC):
    volumne = 0

    @abstractmethod
    def get_name(self) -> str:
        pass


class Radio(Device):
    def get_name(self):
        return f"Radio {self}"


class TV(Device):
    def get_name(self):
        return f"TV {self}"


class Remote(ABC):
    @abstractmethod
    def volumne_up(self):
        pass

    @abstractmethod
    def volumne_down(self):
        pass


class BasicRemote(Remote):
    def __init__(self, device: Device):
        self.device = device

    def volumne_up(self):
        self.device.volumne += 1
        print(f"{self.device.get_name()} volumne up: {self.device.volumne}")

    def volumne_down(self):
        self.device.volumne -= 1
        print(f"{self.device.get_name()} volumne down: {self.device.volumne}")


if __name__ == "__main__":
    radio = Radio()
    tv = TV()

    radio_remote = BasicRemote(radio)
    tv_remote = BasicRemote(tv)

    radio_remote.volumne_up()
    radio_remote.volumne_up()
    radio_remote.volumne_down()

    tv_remote.volumne_up()
    tv_remote.volumne_down()
    tv_remote.volumne_up()
    tv_remote.volumne_up()

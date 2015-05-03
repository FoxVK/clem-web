__author__ = 'fox@vsetin.org'
import subprocess


class Card:

    @staticmethod
    def get():
        cid = 0
        for line in subprocess.check_output(["amixer", "info"]).decode().split('\n'):
            if line.startswith('Card '):
                name = line.split("'")[3].split(" at")[0]
                default = False
                if line.startswith("Card default "):
                    default = True

                yield Card(name, cid, default)
                cid += 1

    def __init__(self, name, cid, default=False):
        self.__default = default
        self.__name = name
        self.__cid = cid
        self.__vol_ch = "PCM"
        self.__volume = Volume(self.__cid, self.__vol_ch)

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, val):
        #self.__volume = Volume(self.__cid, self.__vol_ch, val)
        self.__volume.set(val)

    @property
    def default(self):
        return self.__default

    def __str__(self):
        return self.__name


class Volume:

    def __init__(self, card_index, output_name="PCM", volume=None):
        self.__card = card_index
        self.__out = output_name

        if volume:
            self.set(volume)

    def __int__(self):
        vals = []

        for line in self.__cmd("sget", self.__out).split("\n"):
            chops = line.split("[")
            if len(chops) >= 2:
                ch2 = chops[1].split("%")
                if len(ch2) >= 2:
                    vals.append(int(ch2[0]))

        return int(max(vals))

    def __str__(self):
        return "card{0}: {1}".format(self.__card, self.__out)

    def __iadd__(self, other):
        other = int(other)
        if other < 0:
            self -= abs(other)
        elif other == 0:
            pass
        else:
            self.__cmd("sset", self.__out, str(other)+"%+")

    def set(self, value):
        value = int(value)
        if 0 <= value <= 100:
            self.__cmd("sset", self.__out, str(value)+"%")
        else:
            raise ValueError("Value muse be between 0%-100%. Not '{0}'%".format(value))

    def __cmd(self, *args):
        amixer = ["amixer", "-c", str(self.__card)] + list(args)
        return str(subprocess.check_output(amixer))


if __name__ == "__main__":
    v = Volume(0)
    print("volume is", int(v), "%")

    c = list(Card.get())
    c[0].volume = 1
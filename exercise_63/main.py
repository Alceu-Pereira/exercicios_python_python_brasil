class TV:
    def __init__(self, channel=0, volume=0):
        self.channel = channel
        self.volume = volume

    def change_volume(self, new_volume):
        if 100 >= new_volume >= 0:
            self.volume = new_volume
            print(f'O volume foi alterado para {new_volume}')
        else:
            print('O volume está fora da faixa permitida [0-100]')

    def show_volume(self):
        return f'O volume atual é {self.volume}'
    
    def change_channel(self, new_channel):
        if 100 >= new_channel >= 0:
            self.channel = new_channel
            print(f'O canal foi alterado para {new_channel}')
        else:
            print('O canal está fora da faixa permitida [0-100]')

    def show_channel(self):
        return f'O canal atual é {self.channel}'

tv1 = TV()
print(tv1.show_volume())
print(tv1.show_channel())
tv1.change_channel(-1)
tv1.change_volume(99)
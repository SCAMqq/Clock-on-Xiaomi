from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from jnius import autoclass

class TimeTileApp(App):
    def build(self):
        self.label = Label(text='', font_size='20sp')
        Clock.schedule_interval(self.update_time, 1)
        return self.label

    def update_time(self, dt):
        from time import strftime
        current_time = strftime('%H:%M:%S')
        self.label.text = f'Time: {current_time}'
        
        # Обновление тайла в шторке управления (псевдокод)
        self.update_quick_settings_tile(current_time)
    
    def update_quick_settings_tile(self, time_text):
        TileService = autoclass('android.service.quicksettings.TileService')
        Tile = autoclass('android.service.quicksettings.Tile')
        tile_service = TileService()  # Нужно настроить класс для работы с тайлом
        
        tile = tile_service.getQsTile()
        tile.setLabel(f'Time: {time_text}')
        tile.setState(Tile.STATE_ACTIVE)
        tile.updateTile()

if __name__ == '__main__':
    TimeTileApp().run()

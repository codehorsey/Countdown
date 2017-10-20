from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty, ListProperty, StringProperty, ObjectProperty, DictProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from KivyCalendar import CalendarWidget

import datetime
import events

class Calendar(CalendarWidget):
    def __init__(self, **kwargs):
        super(Calendar, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1.0/10)

    def update(self, dt):
        # print self.active_date
        pass

class Countdown(GridLayout):
    events_dict = DictProperty(events.main())
    def __init__(self, **kwargs):
        super(Countdown, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1.0/10)

    def update(self, dt):
        self.clear_widgets()
        for name, date in self.events_dict.items():
            countdown = events.days_until_event(date)
            self.add_widget(Label(text=str(name)))
            self.add_widget(Label(text=str(countdown)))
  

class EnterEvents(TextInput):
    pass

class MainScreen(Screen):
    # _python_access = ObjectProperty()
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1.0/10)
        # self.ids._display_date.text = 'Coming SOon'

    def create_event(self):
        # [day, month, year]
        date = self.ids._display_date.text
        # string
        name = self.ids._event_name.text
        # adds event to file using calendar widget
        events.add_event(date, name)
        # update dict
        self.ids._countdown.events_dict = events.main()

        
    def update(self, dt):
        calscreen = self.manager.get_screen('cal')
        calscreen.picked_date
        self.ids._display_date.text = str(calscreen.picked_date)
       
class CalendarScreen(Screen):
    picked_date = ObjectProperty()

class MainApp(App):
    def build(self):  
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(CalendarScreen(name='cal'))
        return sm

a = MainApp()
a.run()
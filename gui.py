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
        # This can't be the way to do this lol?!?!
        # self.events_dict = events.main()

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
        self.ids._display_date.text = 'Coming SOon'

    def create_event(self):
        # [day, month, year]
        date = self.ids._display_date.text
        # string
        name = self.ids._event_name.text
        # adds event to file using calendar widget
        events.add_event(date, name)
        # Would love to update dict in other class. How do I access it?!?!?!?!
        # getting around this by calling events.main every single update to re-read file.
        self.ids._countdown.events_dict = events.main()

        
    def update(self, dt):
        # only way I know how to get date from calendar switching screens besides 
        # lumping all under one big root and using ids...
        a = App.get_running_app()
        try:
            self.ids._display_date.text = str(a.selected_date.active_date)
        except:
            pass

class CalendarScreen(Screen):
    picked_date = ObjectProperty()
    pass

class MainApp(App):
    selected_date = ObjectProperty()
    def build(self):  
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(CalendarScreen(name='cal'))
        return sm

    def pass_stuff(self, date):
        self.selected_date = date
       


a = MainApp()
a.run()
# AI generated scratch

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner

class CustomApp(BoxLayout):
    def __init__(self, **kwargs):
        super(CustomApp, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        # Logo/Name area
        self.logo = Label(
            text='Logo/Name',
            size_hint=(1, 0.1),
            color=(0, 0, 0, 1),
            bold=True
        )
        self.add_widget(self.logo)

        # Paste URL field
        self.url_input = TextInput(
            hint_text='Paste URL',
            size_hint=(1, 0.1),
            multiline=False
        )
        self.add_widget(self.url_input)

        # Choose Format/Resolution dropdown (Spinner)
        self.format_spinner = Spinner(
            text='Choose Format and/or Resolution',
            values=('720p', '1080p', '4K', 'MP4', 'MP3'),
            size_hint=(1, 0.1)
        )
        self.add_widget(self.format_spinner)

        # Download button
        self.download_button = Button(
            text='Download',
            size_hint=(1, 0.1)
        )
        self.add_widget(self.download_button)

        # Instructions / FAQ / Links area
        self.info_box = Label(
            text='Instruction / FAQ / Links',
            size_hint=(1, 0.5),
            halign='center',
            valign='middle'
        )
        self.info_box.bind(size=self.info_box.setter('text_size'))  # Ensures text wraps inside the box
        self.add_widget(self.info_box)

class MyApp(App):
    def build(self):
        return CustomApp()

if __name__ == '__main__':
    MyApp().run()

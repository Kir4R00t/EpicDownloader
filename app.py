import downloader

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner

class MainApp(BoxLayout):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        # Logo/Name
        self.logo = Label(
            text='Logo/Name',
            size_hint=(1, 0.2),
            bold=True,
            halign='center',
            valign='middle'
        )
        
        # URL field
        self.url_input = TextInput(
            hint_text='Paste URL',
            size_hint=(1, 0.06),
            multiline=False
        )
        
        # Format/Resolution Spinner menu
        self.format_spinner = Spinner(
            text='Choose Format and/or Resolution',
            values=('720p', '1080p', '4K', 'MP4', 'MP3'),
            size_hint=(1, 0.1)
        )
        
        # Download button
        self.download_button = Button(
            text='Download',
            size_hint=(1, 0.1)
        )
        # Bind the button to the download action
        self.download_button.bind(on_press=self.on_download_press)

        # Instructions / FAQ / Links area
        self.info_box = Label(
            text='Instruction / FAQ / Links',
            size_hint=(1, 0.5),
            halign='center',
            valign='middle'
        )

        # Add widgets to layout
        self.add_widget(self.logo)
        self.add_widget(self.url_input)
        self.add_widget(self.format_spinner)
        self.add_widget(self.download_button)
        self.add_widget(self.info_box)

        # Binds
        self.info_box.bind(size=self.info_box.setter('text_size'))

    def get_url(self):
        # Get the URL from the TextInput
        return self.url_input.text
    
    # TODO:
    # Check given url --> use right download function
    def check_source(self, url):
        sources = [
            'youtube',
            'instagram'
        ]
         
        for source in sources:
            if source in url:
                return source
            
        return 'No video source found'

    def on_download_press(self, instance):
        url = self.get_url()
        source = self.check_source(url)

        format_or_resolution = self.format_spinner.text
        if not url:
            print("Please enter a valid URL.")
            return

        print(f"Downloading from URL: {url} with format/resolution: {format_or_resolution}")
        
        if source == 'youtube':
            downloader.youtube(url)
        elif source == 'instagram':
            downloader.insta(url)
        else:
            print("Invalid source")
            return

class MyApp(App):
    def build(self):
        return MainApp()

if __name__ == '__main__':
    MyApp().run()

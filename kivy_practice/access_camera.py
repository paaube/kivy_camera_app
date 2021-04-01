from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class CameraExample(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Create camera object
        self.cameraObject = Camera(play=False)
        self.cameraObject.play = True
        self.cameraObject.resolution = (1920, 1080) # resolution

        # Button to take the photo
        self.camaraClick = Button(text="Take Photo")
        self.camaraClick.size_hint=(.5, .2)
        self.camaraClick.pos_hint={'x': .25, 'y':.75}

        # bind button to save the picture
        self.camaraClick.bind(on_press=self.onCameraClick)

        # add to the layout
        layout.add_widget(self.cameraObject)
        layout.add_widget(self.camaraClick)

        return layout

    # Save the picture as a png     
    def onCameraClick(self, *args):
        self.cameraObject.export_to_png('picture.png')


# Start the Camera App
if __name__ == '__main__':
     CameraExample().run()
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.label  import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color
from kivy.uix.textinput import TextInput
from kivy.graphics import RoundedRectangle
from kivy.properties import NumericProperty
from kivy.uix.button import  Button
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
import math
import matplotlib.pyplot as plt
import numpy as np
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg



# Window.size = (350, 580)






class ScreenOne(Screen):
    def __init__(self, **kwargs):
        super(ScreenOne, self).__init__(**kwargs)
        # self.add_widget(Label(text='Hello, Screen One!', color = (0,0,0,1) ))
        self.add_widget(Image(source = 'quad2.png', size_hint= (0.5, 0.5), pos_hint = {"center_x":.5 ,  "center_y":.65}))
        self.add_widget(Label(text = 'Quadratic Calculator', font_size = 60, color = ('#03045E'), pos = (0, -100), ))
        self.add_widget(Label(text = 'Solver', font_name = 'Arial' , font_size = 40, color = ('#03045E'), halign= 'center' , pos = (0, -150), ))
    

class ScreenTwo(Screen):
    def __init__(self, **kwargs):
        super(ScreenTwo, self).__init__(**kwargs)
        with self.canvas.before:
            Color (1, 1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos, source='cal3.JPG')
        
        lab = Label(text = 'Quadratic Calculator' , color = ('#03045E'), font_size = '20' , pos_hint={'x': .12, 'top': .95}, size_hint=(None, None), size=(200, 50) , bold = True )
       
        img = Image(source = 'quad2.png', size_hint= (.15 , .15), pos_hint={'x': .02, 'top': .98})
        self.add_widget(img)
        self.add_widget(lab)
        
      

        self.box_layout = BoxLayout(orientation='horizontal', spacing=10, padding=20)
        self.text_input1 = TextInput(hint_text = 'Enter The Value of A', size_hint = (.4, .1) ,pos_hint={'x': .06, 'top': .23}, multiline=False)
        self.box_layout.add_widget(self.text_input1)

        self.text_input2 = TextInput(hint_text = 'Enter The Value of B' ,size_hint = (.4, .1),pos_hint={'x': .06, 'top': .23}, multiline=False)
        self.box_layout.add_widget(self.text_input2)
        

        self.text_input3 = TextInput( size_hint = (.4, .1),pos_hint={'x': .06, 'top': .23}, hint_text = 'Enter The Value of C',  multiline=False)
        self.box_layout.add_widget(self.text_input3)

        float_layout = FloatLayout()

        #Graph button 
        graph_btn = MDFillRoundFlatButton(text="Plot Graph", font_size=18, pos_hint={'center_x': 0.9, 'y': 0.83},
                                          size=(20, 20), on_press=self.plot_button_pressed)


        #clear screen button 
        clear_btn = MDFillRoundFlatButton(text="Clear", font_size=18, pos_hint={'center_x': 0.9, 'y': 0.9},
                           size=(20, 20), on_press=self.clear_button_pressed)
        #solve button

        submit_btn = MDFillRoundFlatButton(text="Solve", font_size=25, pos_hint={'center_x': 0.5, 'y': 0.03},
                                           size_hint=(0.23, 0.1), on_press = self.submit_button_pressed)
        submit_btn.bind(on_press=self.submit_button_pressed)
        # cancel_btn = Button(text ="cancel" )
        float_layout.add_widget(submit_btn)
        float_layout.add_widget(clear_btn)
        float_layout.add_widget(graph_btn)
        self.add_widget(float_layout)

        self.add_widget(self.box_layout)
       
        self.text_input = TextInput(text='', readonly=True, multiline=True, size_hint=(0.8, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.55}, font_size= 16, )
        self.text_input.background_color = (206/255, 213/255,  189/255, 1)
        self.text_input.foreground_color = (1,0,0, 1)
        self.add_widget(self.text_input)

    def clear_button_pressed(self, instance):
            self.text_input1.text = ''
            self.text_input2.text = ''
            self.text_input3.text = ''
            self.text_input.text = ''

    def plot_button_pressed(self, instance):
        a = float(self.text_input1.text)
        b = float(self.text_input2.text)
        c = float(self.text_input3.text)
        x = np.linspace(-10,10,100)
        y = a*x**2 + b*x + c
        fig, ax = plt.subplots()
        plt.plot(x,y,)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Quadratic Graph')
        plt.grid(True)

        canvas = FigureCanvasKivyAgg(fig)
        popup = Popup(title ='Quadratic Graph', content = canvas, size_hint = (0.8, 0.8))
        popup.open()
        # plt.show()

    def submit_button_pressed(self, instance):
        a = float(self.text_input1.text)
        b = float(self.text_input2.text)
        c = float(self.text_input3.text)
        

       

        D =  (b*b - (4*a*c))
# if statement 
        if D >= 0:
            f= round(math.sqrt(D),2)
            x1 = round(((- b + f)/(2 * a)),2)
            # the other value of x 
            f= round(math.sqrt(D),2)
            x2 = round(((- b - f)/(2 * a)),2)
            self.text_input.text = f'''Answer: X1 = {x1} or X2 = {x2}
                             Solution:
            recall: ax^2 + bx + c = 0
            step 1: enter coefficients:  a = {a}, b = {b} , c = {c} 
            step 2: check if  b^2 -4*a*c > = 0, in this case its {D}.
            step 3: since b^2 -4*a*c > 0, 
                    hence X1 = (-b + (4 *a * c)^0.5 ) / 2 * a
                            substituting a = {a}, b = {b} , c = {c}, Using the Qudratic Formular, we get
                            X1 = (-{b} + (4 * {a} * {c})) / 2 * {a},
                            X1 = {x1}
                            OR
                            Plugging the value as above into
                            X2 = (-{b} - (4 * {a} * {c})) / 2 * {a}
                            X2 = {x2}
                            finally comparing both roots
                            X1 = {x1} or X2 = {x2}'''


        #   second condition 

        if D == 0:
            x1= round(-b/(2*a))
            x2= round(-b/(2*a))
            self.text_input.text = f'''the value of D = {D}, x = {x1} or x = {x2}
             Solution:
            recall: ax^2 + bx + c = 0
            step 1: enter coefficients:  a = {a}, b = {b} , c = {c} 
            step 2: check if  b^2 -4*a*c = 0, in this case its {D}.
            step 3: since b^2 -4*a*c = 0, 
                    hence X1 = (-b / 2 * a )
                            substituting a = {a}, b = {b} ,  Using the Qudratic Formular, we get
                            X1 = (-{b} / 2 * {a} )
                            X1 = {x1}
                            OR
                            Plugging the value as above into
                            X2 = (-{b} / 2 * {a} )
                            X2 = {x2}
                            finally comparing both roots
                            X1 = {x1} or X2 = {x2} '''
        
    
        # Third Condition

        if D < 0:
            
            self.text_input.text= f''' Answer: The eqation has no real root

            Solution:
            recall: ax^2 + bx + c = 0
            step 1: enter coefficients:  a = {a}, b = {b} , c = {c} 
            step 2: check if  b^2 -4*a*c < 0, in this case its {D}.
            step 3: since b^2 -4*a*c < 0, 
                    hence X1 = X2 = Complex roots. '''
      
  

class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        Clock.schedule_once(self.switch_screen, 3)
        self.background_color = (1, 1, 1, 1)

    def switch_screen(self, *args):
        self.current = 'screen_two'

class MyApp(MDApp):
    def build(self):
        sm = MyScreenManager()
        sm.add_widget(ScreenOne(name='screen_one'))
        sm.add_widget(ScreenTwo(name='screen_two'))
        return sm

if __name__ == '__main__':
    MyApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import math

class CalcInput(TextInput):
    def insert_text(self, substring, from_undo = False):
        allowed = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '.', '0', '%', '(', ')', '+', '-', '*', '^', '/']
        if not substring in allowed:
            return super().insert_text('', from_undo = from_undo)
        else:
            return super().insert_text(substring, from_undo = from_undo)


class CalcWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__()

        nums = [7, 8, 9, 4, 5, 6, 1, 2, 3, '.', 0, '%']
        syms = ['\u00f7', '(', 'AC', '\u00d7', ')', 'mod', 'x²', '-', '\u03c0']
        syms2 = ['C', '\u221a', '+']
        self.numbers = self.ids.numbers
        self.symbols = self.ids.symbols
        self.right_symbols = self.ids.right_symbols

        # Adicionando os botões - números
        for num in nums:
            btn = Button(text = str(num),
                         background_normal = '',
                         background_color = (0.004, 0.055, 0.102, 1),
                         font_size = 26)
            btn.bind(on_release = self.echo_num)
            self.numbers.add_widget(btn)

        # Adicionando os botões - símbolos
        for sym in syms:
            btn = Button(text = str(sym),
                         background_normal = '',
                         background_color = (0.004, 0.055, 0.102, 1),
                         font_size = 26)
            btn.bind(on_release = self.echo_num)
            self.symbols.add_widget(btn)

        # Adicionando o botão de '=' 
        eq = Button(text = '=', size_hint_y = 0.333,
                         background_normal = '',
                         background_color = (0.133, 0.855, 0.431, 1),
                         font_size = 26)
        eq.bind(on_release = self.evaluate_exp)

        # Adicionando os outros símbolos
        self.ids.symbols_cont.add_widget(eq)
        for elem in syms2:
            btn = Button(text = str(elem),
                         background_normal = '',
                         background_color = (0.004, 0.055, 0.102, 1),
                         font_size = 26)
            btn.bind(on_release = self.echo_num)
            self.right_symbols.add_widget(btn)

    def echo_num(self, instance):
        query = self.ids.query

        # Dá prioridade à porcentagem
        if instance.text == '%' and len(query.text) > 0:
            symbols = []
            symbols.append(query.text.rfind('-'))
            symbols.append(query.text.rfind('+'))
            symbols.append(query.text.rfind('\u00f7'))
            symbols.append(query.text.rfind('\u00d7'))
            sym_indice = max(symbols)# Mantém o índice do último símbolo
            if sym_indice < 0:
                percentual = round(float(query.text)/100, 2)
                query.text = str(percentual)
            else:
                res = query.text
                aux = res[sym_indice+1:]
                percentual = round(float(aux)/100,2)
                query.text = res[:sym_indice+1] + str(percentual)
        
        # Dá prioridade à raiz quadrada
        elif instance.text == '\u221a' and len(query.text) > 0:
            symbols = []
            symbols.append(query.text.rfind('-'))
            symbols.append(query.text.rfind('+'))
            symbols.append(query.text.rfind('\u00f7'))
            symbols.append(query.text.rfind('\u00d7'))
            sym_indice = max(symbols)# Mantém o índice do último símbolo
            if sym_indice < 0:
                raiz = math.sqrt(float(query.text))
                query.text = str(raiz)
            else:
                res = query.text
                aux = res[sym_indice+1:]
                raiz = math.sqrt(float(aux))
                query.text = res[:sym_indice+1] + str(percentual)
        
        # Muda a saída de 'x²' para '^2, no visor'
        elif instance.text == 'x²':
            query.text += '^2'
        
        # Apaga o visor, caso  pressione o botão 'AC'
        elif instance.text == 'AC':
            query.text = ''

        # Apaga o último número da calculadora
        elif instance.text == 'C':
            query.text = query.text[:-1]      
        else:
            query.text += instance.text

    def evaluate_exp(self, instance):
        query = self.ids.query
        aux = query.text
        exp = self.resolve_sym(query.text)
        
        if exp == '':
            exp = '0'
        
        if exp[0] == '0' and len(exp) > 1:
            exp = exp[1:]

        exp = eval(exp)
        query.text = str(exp)

        # print(self.ids)

        res = Historico(exp = aux,
                        resultado = query.text)
        
        self.ids.hist.add_widget(res)

    def resolve_sym(self, instance):
        res = instance.replace('\u00f7', '/').replace('\u00d7', '*').replace('\u03c0', str(math.pi)).replace('^2', '**2')
        return res

class Historico(BoxLayout):
    
    def __init__(self, exp, resultado, **kwarg):
        super().__init__()
        print('exp: ', exp, type(exp))
        print(self.ids)
        self.ids.expressao.text = exp
        self.ids.resultado.text = resultado

class calcApp(App):
    def build(self):
        
        return CalcWindow()

if __name__ == "__main__":
    calcApp().run()
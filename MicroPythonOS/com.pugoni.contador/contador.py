import lvgl as lv
from mpos import Activity
 
 
class contador(Activity):
 
    def onCreate(self):
        # Contador de cliques (começa em zero e nunca é reiniciado)
        self.contador = 0
 
        # Tela do app
        screen = lv.obj()
 
        # Botão no centro da tela
        self.botao = lv.button(screen)
        self.botao.center()
        # Quando o botão for clicado, chama o método ao_clicar
        self.botao.add_event_cb(self.ao_clicar, lv.EVENT.CLICKED, None)
 
        # Texto dentro do botão, que mostra a contagem
        self.rotulo = lv.label(self.botao)
        self.rotulo.set_text("Cliques: 0")
        self.rotulo.center()
 
        self.setContentView(screen)
 
    def ao_clicar(self, evento):
        self.contador += 1
        self.rotulo.set_text("Cliques: " + str(self.contador))
 

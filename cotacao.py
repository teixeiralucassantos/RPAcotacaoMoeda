from tkinter import *
from tkinter import messagebox, ttk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyautogui as tempoPausaComputador

class CotacaoMoeda:
    def __init__(self, master):
        self.master = master
        self.master.title("Cotação de Moedas")
        self.master.geometry("600x400")
        self.master.configure(bg="#2c3e50")

        # Título
        title_label = Label(self.master, text="Cotação de Moedas", font=("Arial", 24), bg="#2c3e50", fg="#ecf0f1")
        title_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Label de Moeda
        moeda_label = Label(self.master, text="Selecione a Moeda:", font=("Arial", 18), bg="#2c3e50", fg="#ecf0f1")
        moeda_label.grid(row=1, column=0, padx=20, sticky='e')

        # Combobox para seleção da moeda
        self.moedaSelecionada = ttk.Combobox(self.master, font=("Arial", 16), state="readonly")
        self.moedaSelecionada["values"] = (
            'Afegane afegão', 'Ariary malgaxe', 'Baht tailandês', 'Balboa panamenho', 
            'Birr etíope', 'Boliviano da Bolívia', 'Bolívar soberano', 'Cedi ganês', 
            'Colom salvadorenho', 'Colón costarriquenho', 'Coroa dinamarquesa', 
            'Coroa islandesa', 'Coroa norueguesa', 'Coroa sueca', 
            'Coroa tcheca', 'Córdoba nicaraguense', 'Dalasi gambiano', 
            'Dinar argelino', 'Dinar bareinita', 'Dinar iraquiano', 
            'Dinar jordaniano', 'Dinar kuwaitiano', 'Dinar líbio', 
            'Dinar macedônio', 'Dinar sérvio', 'Dinar tunisiano', 
            'Dirham dos Emirados Árabes Unidos', 'Dirham marroquino', 
            'Dong vietnamita', 'Dram armênio', 'Dólar Liberiano', 
            'Dólar americano', 'Dólar australiano', 'Dólar bahamense', 
            'Dólar barbadense', 'Dólar belizenho', 'Dólar bermudense', 
            'Dólar bruneano', 'Dólar canadense', 'Dólar das Ilhas Cayman', 
            'Dólar das Ilhas Salomão', 'Dólar de Hong Kong', 
            'Dólar de Trinidad e Tobago', 'Dólar do Caribe Oriental', 
            'Dólar fijiano', 'Dólar guianense', 'Dólar jamaicano', 
            'Dólar namibiano', 'Dólar neozelandês', 'Dólar singapuriano', 
            'Dólar surinamês', 'Escudo cabo-verdiano', 'Euro', 
            'Florim arubano', 'Florim das Antilhas Holandesas', 
            'Florim húngaro', 'Franco CFA Central', 'Franco CFA ocidental', 
            'Franco CFP', 'Franco burundiano', 'Franco comoriano', 
            'Franco congolês', 'Franco do Djibouti', 'Franco guineano', 
            'Franco ruandês', 'Franco suíço', 'Gourde haitiano', 
            'Guarani paraguaio', 'Hryvnia ucraniano', 'Iene japonês', 
            'Kina papuásia', 'Kip laosiano', 'Kuna croata', 
            'Kwacha malauiana', 'Kwacha zambiano', 'Kwanza angolano', 
            'Lari georgiano', 'Lek albanês', 'Lempira hondurenha', 
            'Leone de Serra Leoa', 'Leu moldávio', 'Leu romeno', 
            'Lev búlgaro', 'Libra Sudanesa', 'Libra egípcia', 
            'Libra esterlina', 'Libra libanesa', 'Lilangeni suazi', 
            'Lira turca', 'Loti lesotiano', 'Manat azeri', 
            'Manat turcomano', 'Marco conversível da Bósnia e Herzegovina', 
            'Metical moçambicano', 'Naira nigeriana', 'Ngultrum butanês', 
            'Novo dólar taiwanês', 'Novo shekel israelense', 
            'Novo sol peruano', 'Ouguiya mauritana', 'Pataca', 
            'Paʻanga tonganesa', 'Peso argentino', 'Peso chileno', 
            'Peso colombiano', 'Peso cubano', 'Peso dominicano', 
            'Peso filipino', 'Peso mexicano', 'Peso uruguaio', 
            'Pula botsuanesa', 'Quetzal guatemalteco', 'Quiate', 
            'Rand sul-africano', 'Real brasileiro', 'Rial catariano', 
            'Rial iemenita', 'Rial iraniano', 'Rial omanense', 
            'Riel', 'Ringgit malaio', 'Riyal saudita', 
            'Rublo bielorrusso', 'Rublo russo', 'Rupia Mauriciana', 
            'Rupia cingalesa', 'Rupia das Seychelles', 'Rupia indiana', 
            'Rupia indonésia', 'Rupia maldívia', 'Rupia nepalesa', 
            'Rúpia Paquistanesa', 'Som quirguiz', 'Som uzbeque', 
            'Somoni', 'Taka bengali', 'Tenge cazaque', 
            'Unidades de Fomento chilenas', 'Won sul-coreano', 
            'Xelim Ugandês', 'Xelim queniano', 'Xelim somali', 
            'Xelim tanzaniano', 'Yuan chinês', 'Yuan chinês (offshore)', 
            'Zloty polonês'
        )
        self.moedaSelecionada.grid(row=1, column=1, padx=20, pady=10)
        self.moedaSelecionada.current(0)

        # Botão de Pesquisa
        botaoPesquisar = Button(self.master, text="Pesquisar", font=("Arial", 16), command=self.pesquisar_item, bg="#3498db", fg="#ecf0f1")
        botaoPesquisar.grid(row=2, column=0, columnspan=2, pady=20)

        # Label para mostrar o valor da moeda
        self.valorMoeda = Label(self.master, text="Valor: R$ 0,00", font=("Arial", 20), bg="#2c3e50", fg="#ecf0f1")
        self.valorMoeda.grid(row=3, column=0, columnspan=2, pady=20)

    def pesquisar_item(self):
        options = Options()
        options.add_argument("--headless")

        meuNavegador = webdriver.Chrome(executable_path=r"C:\Users\User\Downloads\chromedriver.exe", options=options)
        meuNavegador.get("https://www.google.com.br/")

        tempoPausaComputador.sleep(1)

        meuNavegador.find_element(By.NAME, "q").send_keys(f"{self.moedaSelecionada.get()} hoje")
        tempoPausaComputador.sleep(1)
        meuNavegador.find_element(By.NAME, "q").send_keys(Keys.RETURN)
        tempoPausaComputador.sleep(3)

        try:
            valorMoeda = meuNavegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
            self.valorMoeda.config(text=f"Valor: R$ {valorMoeda}")
        except Exception as e:
            messagebox.showerror("Erro", "Não foi possível obter a cotação. Tente novamente.")

        meuNavegador.quit()

if __name__ == "__main__":
    root = Tk()
    app = CotacaoMoeda(root)
    root.mainloop()

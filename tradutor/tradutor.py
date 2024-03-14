import customtkinter as ctk
from deep_translator import GoogleTranslator

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')


def traduzir():
    texto_para_traduzir = user_text.get()
    idioma= lang_to_var.get()
    resultado = GoogleTranslator( source = 'auto', target= idioma) . translate(texto_para_traduzir)
    translated_text.configure(state= 'normal')
    translated_text.delete(0,'end')
    translated_text.insert(0,resultado)
    

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')


janela = ctk.CTk()
janela.geometry("300x300")

janela.minsize(500,400)
janela.maxsize(600,400)
janela.title("tradutor universal v1.0")


ctk.CTkLabel (janela,text='Tradutor Universal v1.0', font=('Arial',25,'bold'),text_color='#4B0082').pack(anchor=ctk.CENTER,pady=5)

app_frame = ctk.CTkFrame(janela,width=500, height=500, fg_color='transparent')
app_frame.pack(fill=ctk.X, padx=20,pady=10)

ctk.CTkLabel(app_frame,text='Texto para Traduzir 🧐',font=('arial',18,'bold'),text_color='#8A2BE2').pack(fill=ctk.X)

user_text = ctk.CTkEntry(app_frame,placeholder_text='Digite aqui',height=50)

user_text.pack(fill=ctk.X)

ctk.CTkLabel(app_frame,text= 'escolha o idioma a traduzir 🤓').pack(pady=5)
 
lang_to_var=ctk.StringVar(value='english')
lang_list = GoogleTranslator().get_supported_languages()
lang_to = ctk.CTkOptionMenu(app_frame, values=lang_list, variable= lang_to_var, dropdown_hover_color='#9370DB')
lang_to.set('english')
lang_to.pack(pady=5)


ctk.CTkLabel(app_frame,text='Texto Traduzido 😉',font=('arial',18,'bold'),text_color='#A020F0').pack(fill=ctk.X)

translated_text= ctk.CTkEntry(app_frame, placeholder_text= 'O texto séra traduzido aqui', height=100, placeholder_text_color='purple')

translated_text.pack(fill=ctk.X)

translated_btn = ctk.CTkButton(app_frame,text="traduza",font=('arial',18,'bold'),command=traduzir) 
translated_btn.pack(fill=ctk.X, pady=10)

janela.mainloop()



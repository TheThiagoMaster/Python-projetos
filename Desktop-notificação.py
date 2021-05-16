from win10toast import ToastNotifier

# Inicializa #
toaster = ToastNotifier()

# Passa parâmetros e mostra a notificação #
toaster.show_toast(
    "Notificação", 
    #digite o que você deseja dentro desta aspas   
    "", 
    threaded=True, 
    icon_path=None, 
    duration=0 # Quantidade de segundos!
)
from tkinter import *
import tkinter as tk
def mor():
     class IceCreamStand:
# Создаем окно
        def __init__(self,window):
           self.window = window
           self.window.title("Ice Cream Stand")
           self.window.geometry("300x350")
           self.window.configure(bg="pink")
           vkus= "Вкусы мороженого:\n\nВанильное\nКлубничное\nШоколадное\nФисташковое"
# Создаем надпись "Refreshing"
           self.refreshing_label = tk.Label(self.window, text="Refreshing", bg="pink", font=("Arial", 20),fg = 'blue')
           self.refreshing_label.pack(pady=10)
#pady — представляет собой вертикальное пространство, которое добавляет пространство сверху или снизу виджета.
#padx — представляет собой горизонтальное пространство, которое добавляет пространство слева и справа от виджета.
# Создаем текстовое поле
           self.c=tk.Label(self.window,text =vkus,bg='white',font=("Arial", 12),padx=50,pady=50)
           self.c.pack()

# Создаем надпись "Ice Cream Stand"
           self.ice_cream_label = tk.Label(self.window, text="Ice Cream", bg="pink", font=("Arial", 20),fg = 'blue')
           self.ice_cream_label.pack(pady=10)
# Запускаем главный цикл окна
     def main():
         window=tk.Tk()
         app = IceCreamStand(window)
         window.mainloop()
     if __name__ == "__main__":
        main()
# 13 ЛАБОРАТОРНАЯ
def zd1():
    from tkinter import ttk
    from PIL import ImageTk, Image
    import random
    class App:
        def __init__(self, window):
            self.window = window
            self.window.title("ПОГОДА")
            self.window.geometry("400x300")
            self.window.configure(bg="deepskyblue2")
            self.window.resizable(width=False, height=False)

            self.button = tk.Button(self.window, text="Завершить",command=window.destroy,fg='blue')
            self.button.pack(side=BOTTOM)

    #photo = PhotoImage(file="./29.png")
            self.img = Image.open("29.png")
            self.e = ImageTk.PhotoImage(self.img)
            a = random.randint(-5, 30)
            self.e2 = Label(window, image=self.e,text=f"ПТ, 2024\n\n{a}◦C\nСолнечно", compound="left",font=('Helvetica 15 bold', 25),fg='white')
            self.e2.config(bg="deepskyblue2")
            self.e2.pack()

            self.c=Label(window,text ="СБ\n16◦",bg='deepskyblue2',font=("Arial", 17),padx=10,pady=10,fg='white')
            self.c.place(x=20, y=30)
            self.c.pack(side=LEFT)

            self.c = Label(window, text="ВС\n19◦",compound="left", bg='deepskyblue2', font=("Arial", 17), padx=10, pady=10, fg='white')
            self.c.place(x=20, y=30)
            self.c.pack(side=LEFT)

            self.c = Label(window, text="ПН\n11◦",compound="left", bg='deepskyblue2', font=("Arial", 17), padx=10, pady=10, fg='white')
            self.c.place(x=20, y=30)
            self.c.pack(side=LEFT)

            self.c = Label(window, text="ВТ\n15◦",compound="left", bg='deepskyblue2', font=("Arial", 17), padx=10, pady=10, fg='white')
            self.c.place(x=20, y=30)
            self.c.pack(side=LEFT)

            self.c = Label(window, text="СР\n26◦",compound="left", bg='deepskyblue2', font=("Arial", 17), padx=10, pady=10, fg='white')
            self.c.place(x=20, y=30)
            self.c.pack(side=LEFT)

            self.img = Image.open("lend.png")
            self.u = ImageTk.PhotoImage(self.img)
            self.u2 = Label(window, image=self.u)
            self.u2.config(bg="deepskyblue2")
            self.u2.pack()

    #label = ttk.Label(image=photo,text="21◦\nСолнечно", compound="left",font=("Arial", 20))
    #label.pack()
    def main():
        window = tk.Tk()
        app = App(window)
        window.mainloop()

    if __name__ == "__main__":
        main()

def zd2():
    import tkinter as tk
    import requests
    from PIL import Image, ImageTk
    class Active:
        def __init__(self, root):
            self.root = root
            self.root.title("API Генерация активности")
            self.root.geometry("1000x270")
            self.root.configure(bg="papayawhip")
            self.root.resizable(width=False, height=False)

            self.img = Image.open("kub.png")
            self.u = ImageTk.PhotoImage(self.img)
            self.u2 = tk.Label(root, image=self.u)
            self.u2.config(bg="papayawhip")
            self.u2.pack()

            self.get_activity_button = tk.Button(self.root, text="Получить новое задание!",font=('Helvetica 15 bold', 15),
                                                 command=self.display_activity, bg='orange2', fg='white')
            self.get_activity_button.pack()

            self.close_activity_button = tk.Button(self.root, text="Завершить",
                                                 command=root.destroy, bg='dark blue', fg='white')
            self.close_activity_button.pack()

        def get_activity(self):
            response = requests.get("https://www.boredapi.com/api/activity")
            data = response.json()
            return data

        def display_activity(self):
            self.activity_data = self.get_activity()
            self.activity_label = tk.Label(self.root, text="Activity: " + self.activity_data['activity'],
                                           font=('Helvetica 15 bold', 25), fg='orange', bg="papayawhip")
            self.activity_label.pack()

            self.type_label = tk.Label(self.root, text="Type: " + self.activity_data['type'],
                                       font=('Helvetica 15 bold', 19), fg='olivedrab3', bg="papayawhip")
            self.type_label.pack()

    def main():
        root = tk.Tk()
        app = Active(root)
        root.mainloop()

    if __name__ == "__main__":
        main()

def zd12var():
    import requests
    import tkinter as tk
    from PIL import ImageTk, Image
    def get_weather():
        apikey = '373efe65bb2440f735f0cb9ab2e74e72'
        city = city_entry.get()
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}'
        # получаем ответ с сайта в виде json
        response = requests.get(url)
        data = response.json()

        dan = f'Город: {data["name"]}\nТемпература: {round(data["main"]["temp"] - 273)}°C\nПогода: {data["weather"][0]["description"]}'
        # функция `get_weather` отправляет запрос к API погоды, используя введенное пользователем название города. Полученные данные о погоде затем обновляют метку `weather_label` в графическом интерфейсе.
        redact.config(text=dan)

    # создание окна
    root = tk.Tk()
    root.title("Приложение погоды")
    root.geometry("600x600")
    root.configure(background='deepskyblue2')
    root.resizable(width=False, height=False)

    city_label = tk.Label(root, text="Введите город\nдля получения погоды:", bg='deepskyblue2', font=('Arial', 30),
                          padx=10, pady=50, fg='white')
    city_label.pack()

    city_entry = tk.Entry(root, bg='white', font=('Arial', 20))
    city_entry.pack()

    get_weather_button = tk.Button(root, text="Получить результат", bg='light pink', fg='deep pink', font=('Arial', 15),
                                   padx=10, pady=10, command=get_weather)
    get_weather_button.pack()

    img = Image.open("oblak1o.png")
    u = ImageTk.PhotoImage(img)
    u2 = tk.Label(root, image=u)
    u2.config(bg="deepskyblue2")
    u2.pack()

    redact = tk.Label(root, text="", bg='deepskyblue2', font=('Arial', 11), padx=10, pady=50)
    redact.pack()

    close_weather_button = tk.Button(root, text="Закрыть", bg='white', fg='deep pink', font=('Arial', 15), padx=10,
                                     pady=10, command=root.destroy)
    close_weather_button.pack()

    root.mainloop()

zd1()
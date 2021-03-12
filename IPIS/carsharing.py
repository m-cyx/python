import tkinter as tk


class Observable:
    def __init__(self, initialValue=None):
        self.data = initialValue
        self.callbacks = {}

    def addCallback(self, func):
        self.callbacks[func] = 1

    def delCallback(self, func):
        del self.callbacks[func]

    def _docallbacks(self):
        for func in self.callbacks:
             func(self.data)

    def set(self, data):
        self.data = data
        self._docallbacks()

    def get(self):
        return self.data

    def unset(self):
        self.data = None


class Model:
    def __init__(self):
        self.myMoney = Observable(0)

    def addMoney(self, value):
        self.myMoney.set(self.myMoney.get() + value)

    def removeMoney(self, value):
        self.myMoney.set(self.myMoney.get() - value)


class View(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)
        tk.Label(self, text='My Money').pack(side='left')
        self.moneyCtrl = tk.Entry(self, width=8)
        self.moneyCtrl.pack(side='left')
        
    def SetMoney(self, money):
        self.moneyCtrl.delete(0,'end')
        self.moneyCtrl.insert('end', str(money))        


class ChangerWidget(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.addButton = tk.Button(self, text='Add', width=8)
        self.addButton.pack(side='left')
        self.removeButton = tk.Button(self, text='Remove', width=8)
        self.removeButton.pack(side='left')        


#class Controller:
    def __init__(self, root):
        self.model = Model()
        self.model.myMoney.addCallback(self.MoneyChanged)
        self.view1 = View(root)
        self.view2 = ChangerWidget(self.view1)
        self.view2.addButton.config(command=self.AddMoney)
        self.view2.removeButton.config(command=self.RemoveMoney)
        self.MoneyChanged(self.model.myMoney.get())
        
    def AddMoney(self):
        self.model.addMoney(10)

    def RemoveMoney(self):
        self.model.removeMoney(10)

    def MoneyChanged(self, money):
        self.view1.SetMoney(money)


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    app = Controller(root)
    root.mainloop()




class UserController:
 # Список пользователей приложения.
 public List<UserModel> Users { get; }
 # Текущий пользователь.
 public UserModel CurrentUser { get; }
 # Является ли пользователь вновь созданным.
 public bool IsNewUser { get; } = false;
 # Создать новый контроллер пользователя.
 # <param name="user"> Пользователь. </param>
 public UserController(string userName)


 # Сохранить данные пользователя.
 public void Save()
 # Получить сохраненный список ползователей.
 # <returns> Пользователь приложения. </returns>
 private List<UserModel> GetUsersData()
 # Изменить данные пользователя.
 # <returns> Пользователь приложения с новым набором данных. </returns>
 public void SetNewUserData(string genderName, DateTime birthDate, double weight =1, double height = 1)

class DBController:
 # Создать новый контроллер для работы с базой данных.
 public DBController (
 # Создать новый SQL-запрос по имющемуся списку параметров заданного типа.
 # <param name="requestArgs "> Набор парамаетров запроса. </param>
 # <param name="requestType "> Тип запроса </param>
 # <returns> Готовый SQL-запрос в виде строки. </returns>
 public string DBController (string[] requestArgs, string requestType
 # Создать новые подключние к базе данных.
 # <param name=" host "> Адрес хоста. </param>
 # <param name=" port "> Порт подключения. </param>
 # <param name=" database "> Имя базы данных. </param>
 # <param name=" username "> Логин пользователя. </param>
 # <param name=" password "> Пароль пользователя. </param>
 # <returns> Создает подключение к базе данных. </returns>
 public DBController (string host, int port, string database, string username, string password)


class Controller:
    def __init__(self, Name, SecondName, PhoneNumber, BirthDate, DriverLicenseNumber, DrivingExperience, Status, Age, Tariff, CardNumber, TariffEndDate, IsIndTrainings, TrainingsLeft, IndTrainingsLeft):
        self.Name = Name
        self.SecondName = SecondName
        self.PhoneNumber = PhoneNumber
        self.BirthDate = BirthDate
        self.DriverLicenseNumber = DriverLicenseNumber
        self.DrivingExperience = DrivingExperience
        self.Status = Status
        self.Age = Age
        self.Tariff = Tariff
        self.CardNumber = CardNumber
        self.TariffEndDate = TariffEndDate
        self.IsIndTrainings = IsIndTrainings
        self.TrainingsLeft = TrainingsLeft
        self.IndTrainingsLeft = IndTrainingsLeft
    



def validation (Name, SecondName, PhoneNumber, BirthDate, DriverLicenseNumber, DrivingExperience, Status, Age, Tariff, CardNumber, TariffEndDate, IsIndTrainings, TrainingsLeft, IndTrainingsLeft):
    
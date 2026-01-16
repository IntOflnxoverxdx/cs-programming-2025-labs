import json
from datetime import datetime

#словарь с ценами на каждый тип бензина
prices = {
    "АИ-92": 67.58,
    "АИ-95": 68.45,
    "АИ-98": 83.42,
    "ДТ": 81.47,
}


#Класс цистерны (tank)
class Tank():
    def __init__(self,id,type,max_volume,current_volume,is_working,min_volume,name):
        self.id = id
        self.type = type
        self.max_volume = max_volume
        self.current_volume = current_volume
        self.is_working = is_working
        self.min_volume = min_volume
        self.name = name
    
    def turn_off(self):
        self.is_working = False
    
    def turn_on(self):
        self.is_working = True

    def check_fuel_level(self):
        if self.current_volume < self.min_volume:
            self.turn_off()

    def sell_gasoline(self,volume):
        self.current_volume -= volume
        statistics["autos"] += 1
        for t in statistics["profit"]:
            if t["type"] == self.type:
                t["volume"] += volume
        history.append({"type":self.type,"data1":volume,"data2":volume*prices[self.type],"time":datetime.now()})
        self.check_fuel_level()
    
# Класс колонки (pump)
class Pump():
    def __init__(self,number,tanks_ids):
        self.number = number
        self.name = f"Колонка {self.number}"
        self.tanks_ids = tanks_ids
        



# Получение всего состояния заправки из json файла
def get_state_from_file(file="state.json"):
    with open(file, 'r',encoding="utf-8") as state:
        return json.load(state)
state = get_state_from_file()

#сохранение всех данных в json
def save_data():
    with open("state.json","w",encoding="UTF-8") as state:

        json.dump({
            "Tanks":list(map(lambda t: {"id":t.id,
                                        "name": t.name,
                                        "type": t.type,
                                        "max_volume": t.max_volume,
                                        "min_volume": t.min_volume,
                                        "current_volume": t.current_volume,
                                        "is_working": t.is_working},
                                        tanks_list)),
            "Pumps":list(map(lambda p: {"number":p.number,
                                        "tanks_ids":p.tanks_ids},
                                        pumps_list)),
            "statistics":statistics,
            "history":list(map(lambda h: {"type":h["type"],
                                          "data1": h["data1"],
                                          "data2": h["data2"],
                                          "time": str(h["time"])},
                                          history)),
            "emergency":EMERGENCY
        },state,ensure_ascii=False)
    print("данные сохранены *добавить*")



# заполнение массивов с цистернами, колонками, историей операций и статистикой исходными данными
tanks_list = list(map(lambda t: Tank(t["id"],t["type"],t["max_volume"],t["current_volume"],t["is_working"],t["min_volume"],t["name"]),state["Tanks"]))
pumps_list = list(map(lambda p: Pump(p["number"],p["tanks_ids"]),state["Pumps"]))
statistics = state["statistics"]
history = list(map(lambda h: {"type":h["type"],"data1":h["data1"],"data2":h["data2"],"time":datetime.strptime(h["time"],"%Y-%m-%d %H:%M:%S.%f")},state["history"]))
EMERGENCY = state["emergency"]


# полный функционал обслуживания клиентов
def serve_customer():
    print("\n--- Обслуживание клиента ---\n")

    #Получение всех колонок где хотя бы в одной подключенной цистерне есть топливо
    # available_pumps = list(filter(lambda pump:len(list(filter(lambda tank:tank.is_working and tank.id in pump.tanks_ids,tanks_list)))>0,pumps_list))
    available_pumps = pumps_list
    for (index,pump) in enumerate(available_pumps):
        print(f"{index+1}) {pump.name}")
    
    selected_pump_id = input("\nВыберите колонку:\n> ")
    
    # Проверка на возможные исключения и варианты пользователя для колонки
    try:
        selected_pump_id = int(selected_pump_id)-1
        if len(str(selected_pump_id)) and selected_pump_id >= 0 and selected_pump_id < len(available_pumps):
            print(f"\n{available_pumps[selected_pump_id].name}\n")

            print("Доступные виды топлива:")
            available_tanks = list(filter(lambda tank:tank.id in available_pumps[selected_pump_id].tanks_ids,tanks_list))
            for (index,tank) in enumerate(available_tanks):
                print(f"{index+1}) {tank.type.ljust(6)}(цистерна {tank.name}) {tank.current_volume}/{tank.max_volume} {"ВЫКЛ" if not tank.is_working else ""}")
            
            selected_tank_id = input("\nВыберите тип топлива:\n> ")
            # Проверка на возможные исключения и варианты пользователя для типа топлива
            try:
                selected_tank_id = int(selected_tank_id)-1
                if len(str(selected_tank_id)) and selected_tank_id >= 0 and selected_tank_id < len(available_tanks):
                    if available_tanks[selected_tank_id].is_working:
                        volume = input("\nВведите количество литров:\n> ")
                        # Проверка на возможные исключения и варианты пользователя объема топлива
                        try:
                            volume = int(volume)
                            if volume <= available_tanks[selected_tank_id].current_volume:
                                #подсчёт суммы и подтверждение
                                print(f"\nСтоимость:\n{volume} л × {prices[available_tanks[selected_tank_id].type]} ₽ = {round(volume*prices[available_tanks[selected_tank_id].type],2)} ₽")

                                answer = input("\nПодтвердить оплату? (y/n)\n> ")
                                while answer.lower() not in ("y","n"):
                                    print("Варианты ответа y - да, n - нет")
                                    answer = input("\nПодтвердить оплату? (y/n)\n> ")


                                if answer.lower() == "y":
                                    tanks_list[tanks_list.index(available_tanks[selected_tank_id])].sell_gasoline(volume)

                                    print("\nОперация выполнена успешно.\nСпасибо за покупку!")
                                else:
                                    print("\nОперация отменена!")
                            else:
                                print("Недостаточно бензина в цистерне для выполнения операции")                
                        except ValueError:
                            print("Объем бензина должен быть числом")
                    else:
                        print(f"Цистерна {available_tanks[selected_tank_id].name} выключена")

                else:
                    print(f"Номер типа топлива должен быть числом от 1 до {len(available_tanks)}")


            except ValueError:
                print("Номер типа топлива не может быть текстом")

        else:
            print(f"Номер колонки должен быть числом от 1 до {len(available_pumps)}")
    except ValueError:
        print("Номер колонки не может быть текстом")
    
    input("\nНажмите Enter для возврата в меню...")


# Функция вывода состояния всех цистерн
def print_all_tanks_states():
    print("\n--- Состояние цистерн ---\n\nДоступные цистерны:")
    for (index,tank) in enumerate(tanks_list):
        print(f"{index+1}) {tank.name.ljust(8)} | {(str(tank.current_volume)+ " / "+str(tank.max_volume)+" л").ljust(15)} | {"ВКЛ" if tank.is_working else "ВЫКЛ" + (" (ниже порога)" if tank.current_volume < tank.min_volume else "")}")
    input("\nНажмите Enter для возврата в меню...")

# Функция пополнения топлива

def refill_tank():
    print("\n--- Пополнение топлива ---\n\nДоступные типы топлива:")
    types = ["АИ-92","АИ-95","АИ-98","ДТ"]
    for (index, fuel_type) in enumerate(types):
        print(f"{index+1}) {fuel_type}")

    fuel_type_id = input("Выберите тип топлива для пополнения\n> ")
    try:
        fuel_type_id = int(fuel_type_id)-1
        if 0 <= fuel_type_id < len(types):
            available_tanks = list(filter(lambda t: t.type == types[fuel_type_id], tanks_list))
            for (index,tank) in enumerate(available_tanks):
                print(f"{index+1}) {tank.name.ljust(6)} | {(str(tank.current_volume)+ " / "+str(tank.max_volume)+" л").ljust(15)}")
            selected_tank_id = input("\nВыберите цистерну\n> ")
            try:
                selected_tank_id = int(selected_tank_id)-1
                if 0 <= selected_tank_id < len(available_tanks):
                    try:
                        fuel_volume = int(input("\nСколько литров топлива залить в цистерну?\n"))
                        if available_tanks[selected_tank_id].current_volume + fuel_volume <= available_tanks[selected_tank_id].max_volume:
                            tanks_list[tanks_list.index(available_tanks[selected_tank_id])].current_volume += fuel_volume
                            print(f"Цистерна {available_tanks[selected_tank_id].name} пополнена на {fuel_volume}л; {available_tanks[selected_tank_id].current_volume}/{available_tanks[selected_tank_id].max_volume}")
                            history.append({"type":"Пополнение","data1":fuel_volume,"data2":available_tanks[selected_tank_id].name,"time":datetime.now()})
                        else:
                            print(f"Объем топлива превышает максимальный объем цистерны ({available_tanks[selected_tank_id].current_volume}/{available_tanks[selected_tank_id].max_volume})")
                    except Exception as e:
                        print(e)
                        print("Объем топлива должен быть числом")
                else:
                    print(f"Номер цистерны должен быть числом от 1 до {len(available_tanks)}")
            except ValueError:
                print(f"Номер цистерны не может быть текстом")
        else:
            print(f"Номер типа топлива должен быть числом от 1 до {len(types)}")

    except ValueError:
        print("Номер типа топлива не может быть текстом")
    
    input("\nНажмите Enter для возврата в меню...")
    

# функция вывода баланса и статистики
def print_balance():
    print("\n--- Баланс и статистика ---")

    print(f"\nОбслужено автомобилей: {statistics["autos"]}")

    profit_sum = 0
    for type in statistics["profit"]:
        profit_sum += type["volume"] * prices[type["type"]]
    print(f"Общий доход: {round(profit_sum,2)} ₽")

    print("\nПродано топлива:")
    for type in statistics["profit"]:
        print(f"{type["type"].ljust(6)} - {str(type["volume"]).ljust(6)} л ({type["volume"] * prices[type["type"]]} ₽)")


    input("\nНажмите Enter для возврата в меню...")

# функция вывода истории операций
def print_history():
    print(history)
    if history:
        print("\nИстория операций:")
        for item in sorted(history,key=lambda k: k["time"]):
            print(f"{item["time"]} | {item["type"].ljust(10)} | {item["data1"]} | {item["data2"]}")
    else:    
        print("\nИстории операций нет")
    input("\nНажмите Enter для возврата в меню...")

# перекачка из одной в другую
def pump_from_one_tank_to_other():
    print("\n--- Перекачка топлива ---")
    types = ["АИ-92","АИ-95","АИ-98","ДТ"]
    for (index, fuel_type) in enumerate(types):
        print(f"{index+1}) {fuel_type}")

    fuel_type_id = input("Выберите тип топлива для пополнения\n> ")
    try:
        fuel_type_id = int(fuel_type_id)-1
        if 0 <= fuel_type_id < len(types):
            available_tanks = list(filter(lambda t: t.type == types[fuel_type_id], tanks_list))
            print(len(available_tanks))
            if len(available_tanks) >= 2:
                for (index,tank) in enumerate(available_tanks):
                    print(f"{index+1}) {tank.name.ljust(6)} | {(str(tank.current_volume)+ " / "+str(tank.max_volume)+" л").ljust(15)}")
                try:
                    from_tank_id = int(input("\nВыберите цистерну из которой перелить топливо:\n> "))-1
                    if 0 < from_tank_id <= len(available_tanks):
                        try:
                            to_tank_id = int(input("\nВыберите цистерну в которую перелить топливо:\n> "))-1
                            if 0 <= to_tank_id < len(available_tanks) and to_tank_id != from_tank_id:
                                try:
                                    fuel_volume = int(input("\nСколько литров топлива залить в цистерну?\n"))
                                    if fuel_volume <= available_tanks[from_tank_id].current_volume:
                                        if available_tanks[to_tank_id].current_volume + fuel_volume <= available_tanks[to_tank_id].max_volume:
                                            tanks_list[tanks_list.index(available_tanks[to_tank_id])].current_volume += fuel_volume
                                            tanks_list[tanks_list.index(available_tanks[from_tank_id])].current_volume -= fuel_volume
                                            tanks_list[tanks_list.index(available_tanks[from_tank_id])].check_fuel_level()
                                            print(f"Цистерна {available_tanks[to_tank_id].name} пополнена на {fuel_volume}л; ({available_tanks[to_tank_id].current_volume}/{available_tanks[to_tank_id].max_volume}) из {available_tanks[from_tank_id].name} ({available_tanks[from_tank_id].current_volume}/{available_tanks[from_tank_id].max_volume})")
                                            history.append({"type":"Перекачка","data1":fuel_volume,"data2":f"{available_tanks[from_tank_id].name} => {available_tanks[to_tank_id].name}","time":datetime.now()})
                                        else:
                                            print(f"Объем топлива превышает максимальный объем цистерны ({available_tanks[to_tank_id].current_volume}/{available_tanks[to_tank_id].max_volume})")
                                    else:
                                        print(f"В цистерне {available_tanks[from_tank_id].name} недостаточно топлтива ({available_tanks[from_tank_id].current_volume})")
                                except ValueError:
                                    print("Объем топлива должен быть числом")
                            else:
                                print(f"Номер цистерны должен быть числом от 1 до {len(available_tanks)} и не может быть тем же номером")
                        except ValueError:
                            print("Номер цистерны должно быть числом")
                    else:
                        print(f"Номер цистерны должен быть числом от 1 до {len(available_tanks)}")
                except ValueError:
                    print("Номер цистерны должно быть числом")
            else:
                print("Недостаточно цистерн для переливания топливо")
        else:
            print(f"Номер типа топлива должен быть числом от 1 до {len(types)}")

    except ValueError:
        print("Номер типа топлива не может быть текстом")


    input("\nНажмите Enter для возврата в меню...")




#Функция для включения и отключения цистерн
def toggle_tanks():
    print("\n--- Управление цистернами ---\n")
    print("Доступные действия:")
    print("1) Включить цистерну")
    print("2) Отключить цистерну")

    tank_toggle_variant = input("\n> ")
    if tank_toggle_variant == "1":
        available_tanks = list(filter(lambda t: not t.is_working,tanks_list))
        if len(available_tanks):
            for (index,tank) in enumerate(available_tanks):
                print(f"{index+1}) {tank.name.ljust(8)} | {(str(tank.current_volume)+ " / "+str(tank.max_volume)+" л").ljust(15)}")
            tank_index = input("\nВыберите цистерну:\n> ")
            try:
                tank_index = int(tank_index)
                if 1 <= tank_index <= len(available_tanks):
                    tanks_list[tanks_list.index(available_tanks[tank_index-1])].turn_on()
                    print(f"\nЦистерна {available_tanks[tank_index-1].name} успешно включена.")
                    history.append({"type":"ВКЛ","data1":available_tanks[tank_index-1].name,"data2":"","time":datetime.now()})
                else:
                    print(f"Номер цистерны должен быть числом от 1 до {len(available_tanks)}")
            except ValueError:
                print("Номер цистерны не может быть текстом")

        else:
            print("\nНет цистерн, доступных для включения\n")
    elif tank_toggle_variant == "2":
        available_tanks = list(filter(lambda t: t.is_working,tanks_list))
        if len(available_tanks):
            for (index,tank) in enumerate(available_tanks):
                print(f"{index+1}) {tank.name.ljust(8)} | {(str(tank.current_volume)+ " / "+str(tank.max_volume)+" л").ljust(15)}")
            tank_index = input("\nВыберите цистерну:\n> ")
            try:
                tank_index = int(tank_index)
                if 1 <= tank_index <= len(available_tanks):
                    tanks_list[tanks_list.index(available_tanks[tank_index-1])].turn_off()
                    print(f"\nЦистерна {available_tanks[tank_index-1].name} успешно выключена.")
                    history.append({"type":"ВЫКЛ","data1":available_tanks[tank_index-1].name,"data2":"","time":datetime.now()})
                else:
                    print(f"Номер цистерны должен быть числом от 1 до {len(available_tanks)}")
            except ValueError:
                print("Номер цистерны не может быть текстом")

        else:
            print("\nНет цистерн, доступных для отлючения\n")
    else:
        print("\nВыберите вариант 1 или 2")
    input("\nНажмите Enter для возврата в меню...")

#Функция вывода состояния колонок
def print_pumps_state():
    available_pumps = pumps_list
    print("\nСостояние колонок на данный момент:")
    for (index,pump) in enumerate(available_pumps):
        print(f"{index+1}) {pump.name}, пистолеты:")
        available_tanks = list(filter(lambda tank:tank.id in pump.tanks_ids,tanks_list))
        for (tank_index,tank) in enumerate(available_tanks):
            print(f"\t{index+1}.{tank_index+1} {tank.name.ljust(10)} | {"ВКЛ" if tank.is_working else "ВЫКЛ"}")




    input("\nНажмите Enter для возврата в меню...")
#функция вызова аварийной ситуации
def start_emergency():
    global EMERGENCY
    print("\nВключен режим авайрийной ситуации, все цистерны отключены")
    for tank in tanks_list:
        tank.is_working = False
    EMERGENCY = True
    history.append({"type":"АВАРИЯ","data1":"АВАРИЯ","data2":"АВАРИЯ","time":datetime.now()})

def stop_emergency():
    global EMERGENCY
    EMERGENCY = False
    history.append({"type":"Авария выкл","data1":"","data2":"","time":datetime.now()})


#Функция вывода всех отключенных цистерн

def print_turned_off_tanks():
    turend_off_tanks = list(filter(lambda t: not t.is_working,tanks_list))
    if turend_off_tanks:
        print("ВНИМАНИЕ!\nОбнаружены отключённые цистерны:")
        for tank in turend_off_tanks:
            print(f"- {tank.name} {"(низкий уровень топлива)" if tank.current_volume<tank.min_volume else ""}")
        print("\n----------------------------------------")



#Функция вызова меню и взаимодействия с другими функциями
def menu():
    if not EMERGENCY:
        print("Выберите действие:")
        print("1) Обслужить клиента (касса)")
        print("2) Проверить состояние цистерн")
        print("3) Оформить пополнение топлива")
        print("4) Баланс и статистика")
        print("5) История операций")
        print("6) Перекачка топлива между цистернами")
        print("7) Включение / отключение цистерн")
        print("8) Состояние колонок")
        print("9) EMERGENCY - аварийная ситуация")
        print("0) Выход")    
        menu_variant = input('> ')
        try:
            menu_variant = int(menu_variant)
            if len(str(menu_variant)) and 0 <= menu_variant <= 9:
                if menu_variant == 1:
                    serve_customer()
                elif menu_variant == 2:
                    print_all_tanks_states()
                elif menu_variant == 3:
                    refill_tank()
                elif menu_variant == 4:
                    print_balance()
                elif menu_variant == 5:
                    print_history()
                elif menu_variant == 6:
                    pump_from_one_tank_to_other()
                elif menu_variant == 7:
                    toggle_tanks()
                elif menu_variant == 8:
                    print_pumps_state()
                elif menu_variant == 9:
                    start_emergency()
                elif menu_variant == 0:
                    return False
            else:
                print("Вариант меню должен быть числом от 0 до 9")

        except ValueError:
            print("Вариант меню не может быть текстом")
        return True
    else:
        print("Выберите действие:")
        print("1) Выключить аварийный режим")
        print("0) Выход")
        print("""     =:            .                  
 .=_.:..=_         ++++_-             
   _=_+=              =+_+++__.       
 ._==__X___. _________X=____+=XXX=___ 
 ++---:X:-=_.X:---------------------X.
.X.   .X  =_.X     +++++++++++++++++X.
++    .X  =_.X      _=  X. ++ -X  =_X.
X=+++++=++X_.X     +==++=++==++=++==X.
X:     ++_=_-X......................X-
XXX   ... ==X+++++++++++==+++++==++++X
X_: _=__+=X_==+++++++==+__=_.+=__+=:.X
X__+=     X=________+X     =X+    .X+X
.--_=.   .X_--------_X.   .===    -X:.
    :=+++=:          :=+++=: _=++=+.  """)
        menu_variant = input('> ')
        try:
            menu_variant = int(menu_variant)
            if len(str(menu_variant)) and 0 <= menu_variant <= 1:
                if menu_variant == 1:
                    stop_emergency()
                elif menu_variant == 0:
                    return False
            else:
                print("Вариант меню должен быть числом от 0 до 1")

        except ValueError:
            print("Вариант меню не может быть текстом")
        return True


def main():
    print("""========================================
АЗС <<СеверНефть>>
Система управления заправочной станцией
========================================\n""")
    while True:
        try:
            print_turned_off_tanks()
            if not menu():
                save_data()
                break
        except KeyboardInterrupt:
            save_data()
            break
    



if __name__ == "__main__":
    main()
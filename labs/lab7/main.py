#Задание 1
print("Задание 1")

objects = [
    ("Containment Cell A", 4),
    ("Archive Vault", 1),
    ("Bio Lab Sector", 3),
    ("Observation Wing", 2)
]
ex1_sorted_objects = sorted(objects, key=lambda ex1_obj: ex1_obj[1])
print(ex1_sorted_objects)

#description
#Код сортирует список `objects` по возрастанию уровня угрозы. Для этого используется встроенная функция `sorted()` с лямбда-выражением в качестве аргумента `key`. Лямбда-выражение `lambda ex1_obj: ex1_obj[1]` указывает, что сортировка должна производиться по второму элементу каждого кортежа (уровню угрозы).

#Задание 2
print("Задание 2")

staff_shifts = [
    {"name": "Dr. Shaw", "shift_cost": 120, "shifts": 15},
    {"name": "Agent Torres", "shift_cost": 90, "shifts": 22},
    {"name": "Researcher Hall", "shift_cost": 150, "shifts": 10}
]
ex2_total_costs = list(map(lambda ex2_staff: ex2_staff["shift_cost"] * ex2_staff["shifts"], staff_shifts))
ex2_max_cost = max(ex2_total_costs)
print(ex2_total_costs)
print(ex2_max_cost)

#description
#Сначала код использует функцию `map()` с лямбда-выражением `lambda ex2_staff: ex2_staff["shift_cost"] * ex2_staff["shifts"]`, чтобы вычислить общую стоимость работы для каждого сотрудника и создать новый список `ex2_total_costs`. Затем функция `max()` применяется к этому списку для нахождения максимальной стоимости.

#Задание 3
print("Задание 3")

personnel = [
    {"name": "Dr. Klein", "clearance": 2},
    {"name": "Agent Brooks", "clearance": 4},
    {"name": "Technician Reed", "clearance": 1}
]

ex3_personnel_with_category = list(map(lambda ex3_p: {
    **ex3_p, 
    "category": (
        "Restricted" if ex3_p["clearance"] == 1 else
        "Confidential" if 2 <= ex3_p["clearance"] <= 3 else
        "Top Secret"
    )
}, personnel))
print(ex3_personnel_with_category)

#description
#Код использует функцию `map()` с лямбда-выражением для создания нового списка словарей. Лямбда-выражение добавляет ключ `"category"` к каждому словарю сотрудника на основе его уровня допуска (`"clearance"`), используя условные выражения (тернарный оператор).

#Задание 4
print("Задание 4")

zones = [
    {"zone": "Sector-12", "active_from": 8, "active_to": 18},
    {"zone": "Deep Storage", "active_from": 0, "active_to": 24},
    {"zone": "Research Wing", "active_from": 9, "active_to": 17}
]
ex4_day_zones = list(filter(lambda ex4_z: ex4_z["active_from"] <= 8 and ex4_z["active_to"] >= 18, zones))
print(ex4_day_zones)

#description
#Код использует функцию `filter()` с лямбда-выражением `lambda ex4_z: ex4_z["active_from"] <= 8 and ex4_z["active_to"] >= 18` для выбора зон, которые полностью активны в дневной период (с 8 до 18 часов включительно).

#Задание 5
print("Задание 5")

import re
reports = [
    {"author": "Dr. Moss", "text": "Analysis completed. Reference: http://external-archive.net"},
    {"author": "Agent Lee", "text": "Incident resolved without escalation."},
    {"author": "Dr. Patel", "text": "Supplementary data available at https://secure-research.org"},
    {"author": "Supervisor Kane", "text": "No anomalies detected during inspection."},
    {"author": "Researcher Bloom", "text": "Extended observations uploaded to http://research-notes.lab"},
    {"author": "Agent Novak", "text": "Perimeter secured. No external interference observed."},
    {"author": "Dr. Hargreeve", "text": "Full containment log stored at https://internal-db.scp"},
    {"author": "Technician Moore", "text": "Routine maintenance completed successfully."},
    {"author": "Dr. Alvarez", "text": "Cross-reference materials: http://crosslink.foundation"},
    {"author": "Security Officer Tan", "text": "Shift completed without incidents."},
    {"author": "Analyst Wright", "text": "Statistical model published at https://analysis-hub.org"},
    {"author": "Dr. Kowalski", "text": "Behavioral deviations documented internally."},
    {"author": "Agent Fischer", "text": "Additional footage archived: http://video-storage.sec"},
    {"author": "Senior Researcher Hall", "text": "All test results verified and approved."},
    {"author": "Operations Lead Grant", "text": "Emergency protocol draft shared via https://ops-share.scp"}
]
ex5_reports_with_links = list(filter(lambda ex5_r: "http://" in ex5_r["text"] or "https://" in ex5_r["text"], reports))
ex5_redacted_reports = list(map(lambda ex5_r: {
    **ex5_r, 
    "text": re.sub(r"https?:\/\/\S+", "[ДАННЫЕ УДАЛЕНЫ]", ex5_r["text"])
}, ex5_reports_with_links))
print(ex5_redacted_reports)

#description
#Код сначала использует `filter()` с лямбда-выражением для отбора отчетов, содержащих подстроки "http://" или "https://". Затем к этим отфильтрованным отчетам применяется функция `map()` с другим лямбда-выражением. Это лямбда-выражение создает новый словарь, где поле `"text"` изменено с помощью `re.sub()`. `re.sub()` используется для замены всех найденных URL-адресов (начинающихся с `http://` или `https://` и следующих за ними не пробельными символами) на строку `"[ДАННЫЕ УДАЛЕНЫ]"`. Для этого требуется импорт модуля `re`. А еще я очень долго искал слово "деструктуризация", чтобы потом объяснить что за звёздочки там.

#Задание 6
print("Задание 6")

scp_objects = [
    {"scp": "SCP-096", "class": "Euclid"},
    {"scp": "SCP-173", "class": "Euclid"},
    {"scp": "SCP-055", "class": "Keter"},
    {"scp": "SCP-999", "class": "Safe"},
    {"scp": "SCP-3001", "class": "Keter"}
]
ex6_reinforced_scp = list(filter(lambda ex6_obj: ex6_obj["class"] != "Safe", scp_objects))
print(ex6_reinforced_scp)

#description
#Код использует функцию `filter()` с лямбда-выражением `lambda ex6_obj: ex6_obj["class"] != "Safe"`, чтобы выбрать из списка `scp_objects` те объекты, класс содержания которых не равен "Safe", формируя список объектов, требующих усиленных мер содержания.

#Задание 7
print("Задание 7")

incidents = [
    {"id": 101, "staff": 4},
    {"id": 102, "staff": 12},
    {"id": 103, "staff": 7},
    {"id": 104, "staff": 20}
]
ex7_top_incidents = sorted(incidents, key=lambda ex7_i: ex7_i["staff"], reverse=True)[0:3]
print(ex7_top_incidents)

#description
#Код сортирует список `incidents` по убыванию количества задействованного персонала (`"staff"`) с помощью `sorted()` и лямбда-выражения `lambda ex7_i: ex7_i["staff"]` с `reverse=True`. Затем с помощью среза `[0:3]` выбираются три наиболее ресурсоемких инцидента.

#Задание 8
print("Задание 8")

protocols = [
    ("Lockdown", 5),
    ("Evacuation", 4),
    ("Data Wipe", 3),
    ("Routine Scan", 1)
]
ex8_protocol_strings = list(map(lambda ex8_p: f"Protocol {ex8_p[0]} - Criticality {ex8_p[1]}", protocols))
print(ex8_protocol_strings)

#description
#Код использует функцию `map()` с лямбда-выражением `lambda ex8_p: f"Protocol {ex8_p[0]} - Criticality {ex8_p[1]}"` для преобразования каждого кортежа в списке `protocols` в форматированную строку, описывающую протокол и его уровень критичности.

#Задание 9
print("Задание 9")

shifts = [6, 12, 8, 24, 10, 4]
ex9_more_than_8 = list(filter(lambda ex9_s: ex9_s >= 8, shifts))
ex9_less_than_12 = list(filter(lambda ex9_s: ex9_s <= 12, shifts))
ex9_more_than_8_and_less_than_12 = list(filter(lambda ex9_s: 8 <= ex9_s <= 12, shifts))
print(ex9_more_than_8)
print(ex9_less_than_12)
print(ex9_more_than_8_and_less_than_12)

#description
#Код использует функцию `filter()` с лямбда-выражениями `lambda ex9_s: ex9_s >= 8`; `lambda ex9_s: ex9_s <= 12`; `lambda ex9_s: 8 <= ex9_s <= 12` для выбора из списка `shifts` только тех смен, длительность которых находится в заданных диапазонах.

#Задание 10
print("Задание 10")

evaluations = [
    {"name": "Agent Cole", "score": 78},
    {"name": "Dr. Weiss", "score": 92},
    {"name": "Technician Moore", "score": 61},
    {"name": "Researcher Lin", "score": 88}
]
ex10_top_performer = max(evaluations, key=lambda ex10_e: ex10_e["score"])
print(f"Сотрудник с наивысшей оценкой: {ex10_top_performer['name']}, Балл: {ex10_top_performer['score']}")

#description
#Код использует функцию `max()` с лямбда-выражением `lambda ex10_e: ex10_e["score"]` в качестве аргумента `key`, чтобы найти словарь сотрудника с наивысшим баллом (`"score"`). Результат затем форматируется и выводится, указывая имя сотрудника и его балл.

import json
qualif = str(input("Введите номер квалификации: "))
found = False
with open('dump.json', encoding= 'utf-8') as file:
    file_content = file.read()
    no_json = json.loads(file_content)
    for skill in no_json:
        if skill["model"] == "data.skill" and skill["fields"]["code"] == qualif:
            skill_code = skill["fields"]["code"]
            skill_title = skill["fields"]["title"]
            found = True
            for prof in no_json:
                if prof["model"] == "data.specialty":
                    if prof["fields"]["code"] in qualif:
                        prof_code = prof["fields"]["code"]
                        prof_title = prof["fields"]["title"]
                        prof_type = prof["fields"]["c_type"]
            break
if not  found:
    print("~" * 15, "Не найдено", "~" * 15)
else:
    print("~" * 15, "Найдено", "~" * 15)
    print(f"{skill_code} >> Квалификация '{skill_title}'")
    print(f"{prof_code} >> Специальность '{prof_title}', {prof_type}")

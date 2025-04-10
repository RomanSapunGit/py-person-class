class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = [Person(name=person["name"], age=person["age"])
                   for person in people]
    for index, person in enumerate(result_list):
        spouse = people[index]
        if spouse.get("wife") is not None:
            wife = result_list[
                find_person_by_name(person.name, result_list)
            ]
            person.wife = wife
            wife.husband = person
        elif spouse.get("husband") is not None:
            husband = result_list[
                find_person_by_name(person.name, result_list)
            ]
            person.husband = husband
            husband.wife = person
    return result_list


def find_person_by_name(name: str, people: list) -> int:
    for index in range(len(people)):
        if people[index].name == name:
            return index
    return -1

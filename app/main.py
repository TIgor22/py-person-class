class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons_list = [Person(name=person["name"], age=person["age"])
                    for person in people]

    for person in people:
        if person.get("wife"):
            main_peron = Person.people[person["name"]]
            wife_person = Person.people[person["wife"]]
            main_peron.wife = wife_person
        elif person.get("husband"):
            main_peron = Person.people[person["name"]]
            husband_person = Person.people[person["husband"]]
            main_peron.husband = husband_person

    return persons_list

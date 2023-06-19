from classes import SuperJob, Connector, HeadHunter


def main():
    vacancies_json = []
    # keyword = input("Введите ключевое слово для поиска ")
    keyword = "Python"

    hh = HeadHunter(keyword)
    sj = SuperJob(keyword)
    for api in (hh,sj):
        api .get_vacancies(page_count=10)
        vacancies_json.extend(api.get_formatted_vacancies())

        connector = Connector(keyword=keyword, vacancies_json=vacancies_json)

        while True:
            command = input(
            "1 - вывести список вакансий;\n"
            "2 - Отсортировать по минимальной зарплате;\n"
            "exit - Выход.\n"
            ">>> "
            )
            if command.lower() == "exit":
                break
            elif command == "1":
                vacancies = connector.select()
            elif command == "2":
                vacancies = connector.sort_by_salary_from()


            for vacancy in vacancies:
                print(vacancy, end='\n')

if __name__ == "__main__":
    main()

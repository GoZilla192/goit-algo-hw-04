from pathlib import Path


def total_salary(path: str) -> tuple:
    try:
        total_employee = 0
        total_salary = 0
        with open(path, 'r', encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            if line == '\n':
                continue

            salary = line.split(',')[1]
            total_salary += float(salary)
            total_employee += 1

        if total_employee != 0:
            return (total_salary, total_salary / total_employee) 
        
        return (total_salary, total_salary) 
    
    except (FileNotFoundError, OSError) as e:
        print(f"Error occurred when opening/reading file: {e}")


if __name__ == "__main__":
    path = Path(__file__).parent

    print(total_salary(path / "salaries.txt"))

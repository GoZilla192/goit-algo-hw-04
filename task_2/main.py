from pathlib import Path


def get_cats_info(path: str) -> list[dict]:
    result = []

    try:
        with open(path, 'r', encoding="utf-8") as file:
            for line in file.readlines():
                info_cat = line.strip().split(',')
                curr_dict = {
                    "id": info_cat[0],
                    "name": info_cat[1],
                    "age": info_cat[2]
                }
                
                result.append(curr_dict)
        
        return result


    except (FileNotFoundError, OSError) as e:
        print(f"Error occurred when opening/reading file: {e}")


if __name__ == "__main__":
    path = Path(__file__).parent
    print(get_cats_info(path / "cats.txt"))
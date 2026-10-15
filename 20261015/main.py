# Use `maturin develop` before executing this file
from parser import Recommend

def handle_value_err(
    type_convert_to: type,
    input_string: str,
    err_msg: str,
):
    while True:
        value = input(input_string)

        try:
            return type_convert_to(value)
        except ValueError:
            print(err_msg)

def main() -> None:
    lang = input("Input your programming language:\n")

    years = handle_value_err(
        int,
        "How many years have you spent on it?\n",
        "Expected an integer.",
    )

    study_per_week = handle_value_err(
        float,
        "What's the percentage you study it per week?\n",
        "Expected a float"
    )

    recommend = Recommend(lang, years, study_per_week)
    print(recommend.recommend())

if __name__ == "__main__":
    main()

from utils.logging_config import configure_logging


def main() -> None:
    configure_logging()
    print("Running ExpenseTracker")


if __name__ == "__main__":
    main()

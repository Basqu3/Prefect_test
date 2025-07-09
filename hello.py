from prefect import flow, tags

@flow(log_prints=True)
def hello(name: str = "World") -> None:
    print(f"Hello, {name}!")
    if random.random() < 0.5:
        raise ValueError("An error occurred in the flow!")
    return f"Flow completed successfully with name: {name}"

if __name__ == "__main__":
    with tags("example1"):
        hello("Prefect User")
    with tags("example2"):
        hello("Prefect User 2")
    with tags("example3"):
        hello("Prefect User 3")

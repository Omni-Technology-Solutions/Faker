from faker import Faker
fake = Faker()

def generate_faker_data(method, count=1):
    if not hasattr(fake, method):
        raise ValueError(f"Invalid Faker.py method: {method}")

    results = []
    for _ in range(count):
        results.append(getattr(fake, method)())

    return results if count > 1 else results[0]

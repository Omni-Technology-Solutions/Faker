from superagi_tools import BaseTool
from fake_data_generator import generate_faker_data

class FakeDataGenerator(BaseTool):
    def __init__(self):
        self.tool_name = "FakeDataGenerator"
        self.tool_description = "A tool to generate fake data using Python."
        self.tool_config = {
            "language": "Python",
            "dependencies": ["Faker"]
        }

    def run(self, input_data):
        category = input_data.get("category", "name")
        method = input_data.get("method", "name")
        count = input_data.get("count", 1)
        
        return generate_faker_data(category, method, count)
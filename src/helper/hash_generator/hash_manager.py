from hash_algorithm import HashAlgorithm

class HashManager:

    def __init__(self, algorithm: HashAlgorithm):
        self.algorithm = algorithm

    def set_algorithm(self, algorithm: HashAlgorithm):
        self.algorithm = algorithm

    def generate_hash(self, text: str) -> str:
        return self.algorithm.hash(text)

    def get_algorithm_name(self) -> str:
        return self.algorithm.name

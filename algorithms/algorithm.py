from abc import ABC, abstractmethod


class Algorithm(ABC):

    @staticmethod
    @abstractmethod
    def search(substring: str, text: str):
        pass

    @classmethod
    def findall(cls, substring: str, text: str) -> list:
        return list(cls.search(substring, text))

    @classmethod
    def name(cls) -> str:
        return cls.__name__

from abc import ABC, abstractmethod
class AbstractClass(ABC):
    def print(self, x):
        print("Passed value is: ", x)
    @abstractmethod
    def task(self):
        print("This is an abstract method. Subclasses must implement this method.")
class test_class(AbstractClass):
    def task(self):
        print("This is a concrete method in the test_class.")
test_obj = test_class()
test_obj.task()
test_obj.print(100)
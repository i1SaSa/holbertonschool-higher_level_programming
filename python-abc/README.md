# abstract classes in python
Abstract Base Classes (ABCs) in Python provide a way to define interfaces when other techniques like duck typing are not sufficient. They allow you to create a blueprint for other classes to follow, ensuring that derived classes implement specific methods and properties.
To create an abstract class, you need to import the `ABC` class and the `abstractmethod` decorator from the `abc` module. Here's a simple example:

```python
from abc import ABC, abstractmethod
class Animal(ABC):
	@abstractmethod
	def make_sound(self):
		pass
class Dog(Animal):
	def make_sound(self):
		return "Woof!"
class Cat(Animal):
	def make_sound(self):
		return "Meow!"
# Example usage
dog = Dog()
cat = Cat()
print(dog.make_sound())  # Output: Woof!
print(cat.make_sound())  # Output: Meow!
```
In this example, `Animal` is an abstract class with an abstract method `make_sound()`. The `Dog` and `Cat` classes inherit from `Animal` and provide concrete implementations of the `make_sound()` method. If a class inherits from `Animal` but does not implement the `make_sound()` method, it will raise a `TypeError` when you try to instantiate it.
Abstract classes are useful when you want to enforce a certain interface across multiple subclasses, ensuring that they all implement specific methods. This is particularly helpful in large codebases or frameworks where consistency is important.
Remember that you cannot instantiate an abstract class directly; you must create a subclass that implements all of its abstract methods.

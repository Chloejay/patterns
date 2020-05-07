# Patterns 

This repo is created based on reading design patterns GoF <i>element of reusable object-oriented software</i> and <i>clean architecture: a craftman's guide to software structure and design</i>, so practice concepts on Python.

It mixed with some engineering work that Python is one option to do with.

#### Design Pattern Glossary: 
<ol>
<li>Creational patterns: design patterns that involve instantiating concrete objects.</li>
<li>Behavioural patterns: design patterns that focus on how objects distribute work.</li>
<li>Polymorphism: the ability to interact with objects of different types in the same way. </li>
<li>Subclass: a class that inherits from a parent class, called a superclass.</li>
<li>Subtype: a data type that inherits from a parent type, called a supertype.</li>
<li>Inheritance: when a subtype or subclass inherits behaviours and methods from the supertype or superclass.</li>
<li>Adapter pattern: a design pattern that connects two incompatible interfaces by fitting between them and providing a compatible interface to both.</li>
<li>Command pattern: a behavioural pattern for encapsulating requests as objects.</li>
<li>Composite class: a class which is designed to contain other classes, including objects of the same type.</li>
<li>Composite pattern: a design pattern for composing nested structures of objects and dealing with these objects uniformly.</li>
<li>Decorator pattern: a design pattern allowing for added behaviour through wrapping.</li>
<li>Facade pattern: a design pattern that involves encapsulating a complex system in a simple interface.</li>
<li>Factory Method pattern: a pattern that delegates concrete instantiation to a method of a subclass.</li>
<li>Factory Object: any object whose main purpose is concrete instantiation, i.e. actually creating objects. </li>
<li>Observer pattern: a behavioural pattern for event handling.</li>
<li>Singleton pattern: a design pattern that enforces a single instantiation of a class that is globally accessible.</li>
<li>State pattern: a behavioural pattern for handling requests taking into account the current state of the object.</li>
<li>structural patterns: design patterns that describe how objects are connected to one another.</li>
<li>Template Method pattern: a behavioural pattern that allows for similar behaviour to be inherited by multiple subclasses.
</li>
<li>Composing objects principle: an alternative method of code reuse that uses aggregation rather than inheritance.</li>
<li>Chain of Responsibility pattern: a behavioural pattern for allowing multiple entities to handle requests. </li>
<li>Open/Closed principle: a design principle dictating that an object should be open to extension, but closed to modification.</li>
<li>Principle of least knowledge: a design principle stating that classes should know about and interact with as few other classes as possible. Also called the Law of Demeter.</li>
<li>Separation of concerns: a design principle dictating that a program should separate different concerns or functions into separate objects or processes. Allows for easier maintenance and loose coupling.</li>
<li>Favor composition over inheritance, especially for FP. </li>
<li>Program to interface, not an implementation.</li>
<li>Refactoring: the process of changing code so that external behaviours and interfaces are unchanged but internal structure is improved.</li>
</ol>

Git usage:
```
git log 
git add -p "atomic" changes 
git stash save ""
git reset <commit hash>//restore changes to specific commits 
git reset --soft <commit hash> //keep changes like unstaged changes 
git reset --hard <commit hash> //will remove changes 
git rebase --interactive <commit hash> //get all the repo commits 
```
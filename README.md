# Design Patterns in Python

## Creational Patterns

Patterns that deal with object creation mechanisms.

### Singleton

Ensures a class has only one instance and provides a global point of access to it.

**Implementation**
- [Naive Singleton](src/1_creational_design_patterns/1_singleton/1_naive_singleton.py)
- [Thread Safe Singleton](src/1_creational_design_patterns/1_singleton/2_thread_safe_singleton.py)

**Use Cases**
- Network manager
- Database connection pool
- Logging service
- Configuration settings
- Utility classes

**Structure**
- Private constructor
- Static instance variable
- Static method to get instance

**Advantages**
- Controlled access to sole instance
- Reduced namespace pollution
- Permits refinement of operations

**Disadvantages**
- Breaks single responsibility principle
- Difficult to unit test
- Global state management issues
- Can mask bad design

### Factory Method

Defines an interface for creating objects but lets subclasses decide which class to instantiate.

**Implementation**
- [Factory Method](src/1_creational_design_patterns/2_factory_method/1_factory_method.py)

**Use Cases**
- Requirements change frequently
- Dynamic switching between implementations
- Many subclass types with single instance requirement
- Hide creation logic from client

**Structure**
- Abstract creator class with factory method
- Concrete creators that override factory method
- Product interface
- Concrete products

**Advantages**
- Separation of concerns
- Open/closed principle
- Single responsibility principle
- Loose coupling

**Disadvantages**
- Can lead to many subclasses
- Requires inheritance

### Abstract Factory

Provides an interface for creating families of related objects without specifying concrete classes.

**Implementation**
- [Abstract Factory](src/1_creational_design_patterns/3_abstract_factory/1_abstract_factory.py)

**Use Cases**
- System independent of product creation
- Multiple families of products
- Products designed to work together
- Library provision without exposing implementation

**Structure**
- Abstract factory interface
- Concrete factory implementations
- Abstract product interfaces
- Concrete product families

**Advantages**
- One level of abstraction over factory method
- Access functionality without caring about implementation
- Isolation of concrete classes
- Easy product family switching
- Promotes consistency

**Disadvantages**
- Complex to implement
- Difficult to extend with new products

### Builder

Separates the construction of a complex object from its representation.

**Implementation**
- [Builder](src/1_creational_design_patterns/4_builder/1_builder.py)
- [Builder Optimized](src/1_creational_design_patterns/4_builder/2_builder_optimized.py)

**Use Cases**
- Many parameters to initialize
- Optional parameters
- Complex object construction
- Same construction process for different representations

**Structure**
- Builder interface
- Concrete builders
- Director class
- Product class

**Advantages**
- Avoids constructor with many parameters
- Step by step construction
- Reusable construction code
- Clean and readable API

**Disadvantages**
- Increased code complexity
- Requires creating separate builder class

### Prototype

Creates new objects by copying existing instances.

**Implementation**
- [Prototype](src/1_creational_design_patterns/5_prototype/prototype.py)

**Use Cases**
- Creating copies of existing objects
- Objects with private or inaccessible fields
- Avoid tight coupling to concrete classes
- Testing and pre-production environments

**Structure**
- Prototype interface with clone method
- Concrete prototypes implementing clone
- Client that requests clones

**Advantages**
- Copy objects without depending on their classes
- Remove repeated initialization code
- Produce complex objects conveniently
- Alternative to inheritance

**Disadvantages**
- Cloning complex objects with circular references is difficult
- Deep copy vs shallow copy considerations

## Structural Patterns

Patterns that deal with object composition and relationships.

### Adapter

Converts the interface of a class into another interface the client expects.

**Implementation**
- [Adapter](src/2_structural_design_patterns/1_adapter/1_adapter.py)

**Use Cases**
- Convert data from one format into another
- Integrate legacy code with new systems
- Use third party libraries with incompatible interfaces
- Reuse existing classes without modification

**Structure**
- Target interface
- Adaptee class with incompatible interface
- Adapter class implementing target interface

**Advantages**
- Single responsibility principle
- Open/closed principle
- Reuse existing functionality

**Disadvantages**
- Increased complexity
- Sometimes simpler to change the service class

### Bridge

Decouples an abstraction from its implementation so both can vary independently.

**Implementation**
- [Bridge](src/2_structural_design_patterns/2_bridge/1_bridge.py)

**Use Cases**
- Avoid exponential growth of inheritance tree
- Multiple orthogonal traits in classes
- Switch implementations at runtime
- Share implementation among multiple objects

**Structure**
- Abstraction class with reference to implementor
- Refined abstractions
- Implementor interface
- Concrete implementors

**Advantages**
- Convert from inheritance to composition
- Platform independent classes
- Hide implementation details from client
- Open/closed principle

**Disadvantages**
- Increased complexity for simple cases
- Additional indirection

### Composite

Composes objects into tree structures to represent part/whole hierarchies.

**Implementation**
- [Composite](src/2_structural_design_patterns/3_composite/1_composite.py)

**Use Cases**
- Core functionality represented as a tree
- Manipulate many objects as a single one
- File system directories
- GUI component trees

**Structure**
- Component interface
- Leaf class
- Composite class containing children

**Advantages**
- Work with complex tree structures conveniently
- Open/closed principle
- Simplify client code

**Disadvantages**
- Difficult to restrict component types
- Design can become overly general

### Decorator

Attaches new behavior to an object without altering existing code.

**Implementation**
- [Decorator](src/2_structural_design_patterns/4_decorator/1_decorator.py)

**Use Cases**
- Add behavior without subclassing
- Override behavior dynamically
- Extension by subclassing is impractical
- Wrap objects at runtime

**Structure**
- Component interface
- Concrete component
- Base decorator class
- Concrete decorators

**Advantages**
- More flexible than inheritance
- Single responsibility principle
- Combine behaviors at runtime

**Disadvantages**
- Difficult to remove specific wrapper
- Order of decorators matters
- Initial configuration code can look complex

### Facade

Provides a simple interface to complex functionality.

**Implementation**
- [Facade](src/2_structural_design_patterns/5_facade/1_facade.py)

**Use Cases**
- Simple interface to complex system
- Remove need for complex object/memory management
- Simplify client implementation
- Decouple subsystem from clients

**Structure**
- Facade class
- Subsystem classes
- Client interacting with facade

**Advantages**
- Isolate clients from subsystem components
- Minimize coupling
- Simplify usage

**Disadvantages**
- Facade can become god object
- May limit flexibility for advanced users

### Flyweight

Uses sharing to support large numbers of similar objects efficiently.

**Implementation**
- [Flyweight](src/2_structural_design_patterns/6_flyweight/1_flyweight.py)

**Use Cases**
- Large number of similar objects
- Memory constraints
- Reduce memory footprint
- Objects share intrinsic state

**Structure**
- Flyweight interface
- Concrete flyweight with intrinsic state
- Flyweight factory
- Client managing extrinsic state

**Advantages**
- Save memory when many similar objects exist
- Centralize state management
- Improved efficiency

**Disadvantages**
- Increased code complexity
- Trade CPU for memory
- Difficult to maintain extrinsic state

### Proxy

Provides functionality before and/or after calling an object.

**Implementation**
- [Proxy](src/2_structural_design_patterns/7_proxy/1_proxy.py)

**Use Cases**
- Lazy initialization
- Access control
- Logging requests
- Caching results
- Same interface as the original object

**Structure**
- Subject interface
- Real subject class
- Proxy class with reference to real subject

**Advantages**
- Control access to original object
- Manage lifecycle of service object
- Works even if service is not ready

**Disadvantages**
- Increased complexity
- Response delay

## Behavioral Patterns

Patterns that deal with object interaction and responsibility.

*Coming soon*
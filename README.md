
# Craftspace - Online Furniture Store

## Project Overview
1. **Team Members**: Amir Kurmanbekov, Rassul Turtulov, Kaminur Orynbek, Adlet Serikbay.
2. **Project Name**: Craftspace
3. **Description**: An online furniture store offering a wide variety of furniture products with a seamless shopping experience.
4. **Technologies Used**:
   - **Backend**: Python, Django
   - **Database**: PostgreSQL using Django ORM
   - **Frontend**: HTML, CSS, JavaScript with Ajax for dynamic user interaction
5. **Software Architecture**: Using Django’s MVT (Model-View-Template), which separates logic, presentation, and database interaction efficiently.
6. **Planned Design Patterns**:
   - **Singleton Pattern**: To maintain a single instance of critical services, such as database connections.
   - **Builder Pattern**: For constructing complex objects like furniture items with various attributes (e.g., size, color, material).
   - Other structural and behavioral patterns are under consideration to improve flexibility and maintainability.

## Applied Design Patterns
1. **Template Method Pattern**:
   - **Location**: Order creation process in `OrderCreationTemplate` and `DefaultOrderCreation`.
   - **Type**: Behavioral Pattern
   - **Description**: Defines a skeleton of an algorithm in an abstract class, with specific steps implemented in subclasses.

2. **Factory Method Pattern**:
   - **Location**: Form creation through `FormFactory`.
   - **Type**: Creational Pattern
   - **Description**: Provides an interface for creating objects, with the instantiation logic deferred to subclasses.

3. **Filter Pattern**:
   - **Location**: Custom template filters, such as `multiply` and `round`.
   - **Type**: Structural Pattern
   - **Description**: Processes data before rendering in templates.

4. **Decorator Pattern**:
   - **Location**: Authentication using `@login_required` decorator in views.
   - **Type**: Structural Pattern
   - **Description**: Adds behavior to functions dynamically without altering their structure.

## Design Patterns Used by Django
1. **Template Method**:
   - **Type**: Behavioral Pattern
   - **Description**: Used in class-based views to define a common structure for request handling.
   
2. **Factory Method**:
   - **Type**: Creational Pattern
   - **Description**: Used for creating various objects like forms and ORM models.
   
3. **Singleton Pattern**:
   - **Type**: Creational Pattern
   - **Description**: Used for settings management, ensuring a single instance of the settings configuration.
   
4. **Observer Pattern**:
   - **Type**: Behavioral Pattern
   - **Description**: Implemented in Django's signal framework to react to events, like model saves.
   
5. **MVC/MVT Architecture**:
   - **Type**: Architectural Pattern
   - **Description**: Django uses MVT (Model-View-Template), a variant of MVC, for organizing code structure.

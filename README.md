# CineManager

 Is an application developed to facilitate cinema management and promote its services. It allows organizations or companies with multiple cinemas to manage their operations efficiently. With the application, it is possible to create and publish advertisements and posters, schedule movie sessions, track user numbers, and sell tickets online. The system features three distinct interfaces: one for regular users, who can view featured movies and filter them by category or genre; one for cinema management; and one for cinema-owning companies and administrative purposes

 #Technology
 CineManager is developed using Django, a high-level Python web framework that enables rapid development of secure and maintainable websites. Django simplifies many aspects of web development by providing built-in solutions for common tasks, such as database management, user authentication, and URL routing. It encourages the use of best practices and follows the "batteries-included" philosophy, offering a comprehensive set of tools and features right out of the box.
For more information about Django, please refer to the official documentation: [Django Documentation](https://docs.djangoproject.com/en/5.1/).
Django follows the principle of "divide and conquer," which means breaking down a complex problem into smaller, manageable pieces called apps. Each app is designed to handle a specific aspect of the project, allowing for modular development and easier maintenance

CineManager consists of the following 4 apps:

Usuários:Manages all logic related to users, including signup, login, logout, and assignment of permissions and roles. This app handles the models, URLs, and views related to these functionalities.

Empresarial:  Manages all logic related to companies, such as cinema registration and viewing monthly performance. This app includes the necessary models, URLs, and views for these operations.

Cinema: Manages all logic associated with cinemas. It includes models (representing the tables in the database), URLs (API endpoints), and views (handling requests and responses and specifying the templates to be rendered).

Cliente: Covers all logic related to the client, such as interacting with the system and viewing relevant information.


media -  Responsible for storing media files, including profiles, movie images, posters, etc.
template - Contains static files (HTML, CSS, JS) used to render the user interface."


#como instalar 

1 clone o repositorio com com git clone 






### Application / Business Logic Layer:-
    -This is the most important Layer of the Application.
*Also called as `Appication Layer` or `Service Layer`*.

*Purpose:-*
    - Implement Business Logic.
    - Process User Request.
    - Validate Data.
    - Control Workflows.

*Properties:-*
    - Calculations.
    - Validations.
    - Approval.
    - Transactions.

*Example:-*
`Business Layer Actually:`
    - Checks Customers.
    - Check Credit Limits.
    - Validates Inventory.
    - Calculates Tax.
    - Generates Invoices.

*Components in this Layer:-*
    - API.
    - Application Servers.
    - Services.
    - Business Modules.
    - Workflow Engine.

#### *API*
    - Communication Bridge between *UI and Business Logic*, *Different ERP Modules*, *ERP and External Systems.*
    - It allows Different Parts of the System to talk each other

*Types of API:-*
    - REST API
    - SOAP API
*Works:- (Example of Customer Relationship Model)*
    - Creates Order.
    - Get Customer details.
    - Check Inventory.
    - Generate Invoice.
*Need for API:-*
    - UI can't access to the database.
    - External System need Connection.
    - Modules must Communicate.

#### *Application Servers:-*
    - Software Platforms which runs the business logic of ERP.
    - Engine Room of ERP.
*Properties:-*
    - Execute ERP Programs.
    - Process User Request.
    - Runs Business Logic.
    - Manage Transactions. 
    - Connect UI with Database

*Works:-*
    - Receieve Request from UI.
    - Execute Programs.
    - Apply Business Rules.
    - Send responses to UI.

#### *Business Modules:-*
    - Inside the Application Server.
    - Request is routed to the correct module
    - Business Module is heart of ERP Functionality.

*Example ERP Modules:-*
    - Finance.
    - Human Resource
    - Sales.
    - Inventory.
    - Procurement.
    - Manufacturing.

*Properties:-*
    - To implement real-world business process

#### *Services:-*
    - Individual Components or Programs that performs specific operations.

*Example:-*
    - Small functional units inside ERP.

*Example-Service:-*
    - Customer Service.
    - Order Service.
    - Inventory Service.
    - Payroll Service.
    - Invoice Service.

*Example-Order-Service:-*
    - Create Order.
    - Update Order.
    - Delete Order.
    - Validate Order.

#### *Workflow-Engine:-*
    - After the Service Selection there should be
        - Approval.
        - Multi-step Actions.
        - Routing.
    - Then the Workflow Engine is Triggered.





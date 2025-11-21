```mermaid
flowchart TD
    A["Simulation Engine"] --> B["World State"]
    B --> C["Agents"]
    C --> D["Agent Decisions"]
    D --> E["State Update Logic"]
    E --> B
    B --> F["History Log"]
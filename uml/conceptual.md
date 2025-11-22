````mermaid
graph LR
    Simulation["Simulation"] -->|"creates updates"| Moment["Moment"]
    Moment -->|"applies to"| Life["Life"]
    Life -->|"contains"| Player["Player"]
    Life -->|"contains"| Environment["Environment"]
    Moment -->|"records to"| EventLog["EventLog"]
    Rules["Rules"] -->|"constrain actions of"| Player
    Rules -->|"constrain evolution of"| Life

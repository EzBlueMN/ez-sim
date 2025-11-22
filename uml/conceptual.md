````mermaid
graph LR
    Simulation["Simulation"] -->|"manages"| MomentManager["MomentManager"]
    Simulation -->|"controls"| FlowManager["FlowManager"]
    FlowManager -->|"updates"| World["World"]
    World -->|"contains"| Player["Player"]
    Player -->|"interacts with"| Resources["Resources"]
    World -->|"contains"| Environment["Environment"]
    Rules["Rules"] -->|"constrain actions of"| Player
    Rules -->|"constrain evolution of"| World
    FlowManager -->|"records events in"| EventLog["EventLog"]

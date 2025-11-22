````mermaid
graph LR
    Simulation["Simulation"] -->|"manages"| MomentManager["MomentManager"]
    
    MomentManager -->|"creates / updates"| Moment["Moment"]
    Moment -->|"applies to"| Life["Life"]
    
    Life -->|"contains"| Player["Player"]
    Player -->|"interacts with"| Resources["Resources"]
    
    Life -->|"contains"| Environment["Environment"]
    
    Rules["Rules"] -->|"constrain actions of"| Player
    Rules -->|"constrain evolution of"| Life
    
    Moment -->|"records events in"| EventLog["EventLog"]

```mermaid
graph LR
    Life["Simulation"] -->|manages| LifePath["MomentManager"]
    Life -->|controls| LifePicture["FlowManager"]
    LifePicture -->|updates| World["World"]
    World -->|contains| Player["Player"]
    Player -->|interacts with| Resources["Resources"]
    World -->|contains| Environment["Environment"]
    Rules["Rules"] -->|constrain actions of| Player
    Rules -->|constrain evolution of| World
    LifePicture -->|records events in| EventLog["EventLog"]

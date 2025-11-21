```mermaid
classDiagram
    %% Core entities
    class Simulation
    class World
    class Agent
    class StateManager
    class TimelineManager
    class Resources
    class Environment
    class Rules
    class HistoryLog

    %% Relationships with labels
    Simulation --> World : manages
    Simulation --> Agent : contains
    Simulation --> StateManager : uses for snapshots
    Simulation --> TimelineManager : tracks timelines
    Simulation --> Rules : enforces

    World --> Resources : provides
    World --> Environment : defines conditions
    World --> HistoryLog : records changes

    Agent --> Resources : consumes/produces
    Agent --> Rules : follows or modifies
    Agent --> Environment : is affected by
    Agent --> Agent : interacts with

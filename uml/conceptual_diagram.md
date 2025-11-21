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
    Simulation --> World
    Simulation --> Agent
    Simulation --> StateManager
    Simulation --> TimelineManager
    Simulation --> Rules

    World --> Resources
    World --> Environment
    World --> HistoryLog

    Agent --> Resources
    Agent --> Rules
    Agent --> Environment
    Agent --> Agent

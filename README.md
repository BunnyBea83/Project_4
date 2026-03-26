# User Relationship Graph & Profile Manager

A Python application that models social connections between users as a graph data structure. Users can be linked as friends, and managers can create, update, and delete user profiles.

Course: Data Structures & Alforithms AD325   
Instructor: Eric Lloyd   
Project #: 4   
Authors: Bea Sauve and Leah Gibbons   

---

## Features

- Graph-based representation of user friendships and relationships
- Linked list ADT supporting graph traversal on unconnected graphs
- Profile management: create, update, and delete user profiles
- Comprehensive test suite covering all `ProfileManager` methods

---

## Project Structure

```
├── Screenshots/          # Git history screenshots
├── data/                 # Test data and sample inputs
│   ├── profiles.csv      # CSV file containing user profile details to add to graph
│   └── test.csv          # CSV file containing test cases
├── main.py               # Entry point — runs the application
├── graph_adt.py          # Graph ADT implementation (nodes, edges, traversal)
├── linked_adts.py        # Linked list ADT used internally by the graph
├── profile_manager.py    # Manager class for creating/updating/deleting profiles
├── user_profile.py       # UserProfile data model
├── testing.py            # Unit tests for all core classes
├── Project_4_UML_Bea_Leah.jpg  # UML class diagram
└── README.md
```

---

## Setup & Installation

**Requirements:** Python 3.x — no external dependencies needed.

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd <repo-folder>
   ```

2. Run the application:
   ```bash
   python main.py
   ```

3. Run the tests:
   ```bash
   python testing.py
   ```

---

## Architecture

See `User_Graph_UML.jpg` for the full UML class diagram.

The core classes are:

- **`UserProfile`** — Stores a user's data (name, ID, friend list, etc.)
- **`ProfileManager`** — Handles CRUD operations on user profiles
- **`GraphADT`** — Represents users as nodes and friendships as edges; supports traversal of unconnected graphs
- **`LinkedADTs`** — Underlying linked list structures used by the graph

---

## Usage

```python
from profile_manager import ProfileManager

manager = ProfileManager()

# Add users
manager.add_user("Alice")
manager.add_user("Bob")

# Connect as friends
manager.add_friendship("Alice", "Bob")

# Delete a user
manager.delete_user("Alice")
```

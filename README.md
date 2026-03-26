# User Relationship Graph & Profile Manager

A Python application that models social connections between users as a graph data structure. Users can be linked as friends, and managers can create, update, and delete user profiles.

Course: Data Structures & Alforithms AD325   
Instructor: Eric Lloyd   
Project #: 4   
Authors: Bea Sauve and Leah Gibbons  
Built: 12/2025

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

---
 
## Usage
 
When launched, the app greets you with the Glubs banner and a login menu:
 
```
*-----*-----*-----*-----*-----*-----*-----*-----*
*  Welcome to the Glubs Social Media Network!   *
*-----*-----*-----*-----*-----*-----*-----*-----*
How would you like to login?
1. Login as user
2. Login as admin
99. Exit the program.
```
 
Enter your name to log in. First-time users will be prompted to create a profile.
 
### User Menu
 
Once logged in as a regular user, you can:
 
| Option | Action |
|--------|--------|
| 1 | Modify your profile |
| 2 | View a profile |
| 3 | Add a friend |
| 4 | View your friend list |
| 5 | View a friend's friend list |
| 6 | Delete your profile |
| 7 | Switch user |
| 8 | Visualize your network graph |
| 9 | Logout |
 
### Admin Menu
 
Admins log in with the password and have additional capabilities:
 
| Option | Action |
|--------|--------|
| 1 | Create a profile |
| 2 | Modify any profile |
| 3 | View any user's profile |
| 4 | View all profiles |
| 5 | Add a friend |
| 6 | View your friend list |
| 7 | View anyone's friend list |
| 8 | Delete any profile |
| 9 | Switch user |
| 10 | **Import profiles from CSV** |
| 11 | Visualize network graph |
| 12 | Logout |
 
### Network Graph
 
The graph visualizer (option 8/11) lets you display:
- **Your network** — yourself, your friends, and friends-of-friends
- **The entire network** — all users and their connections
 
### Bulk Import (Admin)
 
Admins can populate the network from `data/profiles.csv` via option 10. The file path is configured at the top of `main.py`:
 
---
 
## Architecture
 
See `User_Graph_UML.jpg` for the full UML class diagram.
 
| Class | Responsibility |
|-------|---------------|
| `UserProfile` | Stores user data: name, relationship status, profile photo, activity status |
| `ProfileManager` | CRUD operations, friend management, CSV import, graph creation |
| `GraphADT` | Graph of user relationships; supports traversal on unconnected graphs |
| `LinkedADTs` | Underlying linked list structures used by the graph |

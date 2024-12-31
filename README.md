# MongoMirror
A lightweight Python utility for cloning MongoDB databases with ease. MongoMirror provides a simple, reliable way to duplicate your MongoDB databases while maintaining data integrity and providing detailed logging of the process.
# Features
- Collection-by-collection transfer
- Automatic connection management
- Support for connection strings with authentication
# Installation
`bash
git clone https://github.com/yourusername/mongomirror.git
cd mongomirror
pip install -r requirements.txt`
# Requirement
`pymongo>=4.0.0`
### The connection strings should include the database name, for example:
`mongodb://username:password@hostname:port/database_name`


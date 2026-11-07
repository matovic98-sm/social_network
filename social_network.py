class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)

alex = Person("Alex")
jordan = Person("Jordan")
print(alex.friends)
alex.add_friend(jordan)
print(alex.friends[0].name)


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name not in self.people:
            self.people[name] = Person(name)
        else:
            print(f"{name} already exists in the network!")

    def add_friendship(self, person1_name, person2_name):
        if person1_name in self.people and person2_name in self.people:
            person1 = self.people[person1_name]
            person2 = self.people[person2_name]
            person1.add_friend(person2)
            person2.add_friend(person1)
        else:
            print("Friendship not created. One or both people don't exist!")

    def print_network(self):
        for person_name, person_obj in self.people.items():
            friend_names = [friend.name for friend in person_obj.friends]
            friends = ", ".join(friend_names)
            print(f"{person_name} is friends with: {friends}")

# Test your code here
network = SocialNetwork()

# Add people
network.add_person("Alex")
network.add_person("Jordan") 
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")

# Test duplicate person
network.add_person("Alex")

# Create friendships
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor") 
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

# Test adding a friendship when a person doesn't exist
network.add_friendship("Jordan", "Johnny")

# Test duplicate friendship
network.add_friendship("Alex", "Jordan")

network.print_network()


# Design Memo
# A graph is the right data structure to represent a social network because it allows people to have
# multiple connections with other people. Each person represents a node, and each friendship 
# represents an edge connecting two nodes. Using an adjacency list makes it easier to keep track of
# these relationships because each person maintains a list of their friends. Since friendships are 
# bidirectional, both people need to be added to each other's friends lists when creating a 
# connection.
# A list or tree would not work as well for representing a social network because they do not 
# support the same type of relationships. A list stores information in a sequence, which makes it 
# difficult to represent people who have multiple friendships with different individuals. A tree 
# uses parent-child relationships to organize information, but friendships do not have a hierarchy.
# Each person is an individual node that can connect to multiple other people without needing a 
# specific order.
# One thing I noticed when implementing this graph was that adding friendships was relatively 
# simple because I could retrieve the Person objects from the dictionary and use their existing 
# methods to create connections. However, I needed to check that both people existed before creating
# a friendship and prevent duplicate connections from being added. Printing the network was also 
# straightforward because I could loop through the dictionary and retrieve each person's friends. 
# One limitation of using an adjacency list is that checking whether two people are already 
# connected requires searching through their friends list. However, this approach works well for a 
# social network because it only stores existing connections rather than every possible connection 
# between people.


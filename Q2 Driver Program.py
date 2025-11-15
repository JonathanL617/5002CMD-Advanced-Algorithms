from UDGraph import UDGraph
from Person import Person

def create_users():
    users = {
        "benji": Person("benji", "Benjamin", "Male", 20, "I like cats", "public"),
        "bobby": Person("bobby", "Bobby", "Male", 19, "Aspiring photographer", "private"),
        "alicia_key": Person("alicia_key", "Alicia Key", "Female",21, "Coffee lover | living my best life!", "public"),
        "one_bite_pizza": Person("one_bite_pizza", "James", "Male", 27, "Professional Pizza Reviewer | One bite, everybody knows the rules", "public"),
        "matcha_masha": Person("matcha_masha", "Masha Kujou", "Female", 19, "Matcha enjoyer | food is life", "public"),
        "lionmusic": Person("lionmusic", "Lionel Mussi", "Male", 24, "New album just dropped link below", "public")
    }

    return users

def create_graph(users):
    graph = UDGraph()

    for user_id in users:
        graph.addVertex(user_id)

    #asign followers
    #person A follow person B (A -> B)

    graph.addEdge("benji", "bobby")
    graph.addEdge("benji", "lionmusic")
    graph.addEdge("benji", "one_bite_pizza")
    graph.addEdge("benji", "matcha_masha")

    graph.addEdge("bobby", "benji")
    graph.addEdge("bobby", "alicia_key")
    graph.addEdge("bobby", "matcha_masha")

    graph.addEdge("alicia_key","matcha_masha")
    graph.addEdge("alicia_key", "lionmusic")

    graph.addEdge("matcha_masha", "one_bite_pizza")
    graph.addEdge("matcha_masha", "alicia_key")

    graph.addEdge("lionmusic", "bobby")
    graph.addEdge("lionmusic", "benji")
    graph.addEdge("lionmusic", "alicia_key")

    return graph

def menu():
    print("=" * 40)
    print("Social Media App")
    print("=" * 40)
    print("[1] Display All Users")
    print("[2] View User Profile")
    print("[3] View Followings List")
    print("[4] View Followers List")
    print("[5] Display Network Graph")
    print("[6] Exit")
    print("=" * 40)

def display_users(users):
    print("=" * 40)
    print("User List")
    print("=" * 40)
    print(f'Total Users: {len(users)}\n')

    for i, (user_id, person) in enumerate(users.items(), 1):
        print(f'{i}. ', end="")
        person.display_profile()

    print("\n")

def view_profile(users):
    print("=== View User Profile ===")
    print("1. View Profile with Privacy Respected (respect privacy setting)")
    print("2. View Full Profile (ignore privacy setting) \n")

    option = int(input("Option (1 or 2): "))

    display_list(users)

    user_id = input("Enter username: ").strip()

    if user_id in users:
        if option == 1:
            users[user_id].display_profile(respect_privacy=True)

        elif option == 2:
            users[user_id].display_profile(respect_privacy=False)

        else:
            print("Invalid option! Please try again")
    else:
        print("User profile not found")


def view_following(users, graph):
    #outgoing edges of vertex
    print("=== View Following List ===")
    display_list(users)
    user_id = input("Enter username: ").strip()

    if user_id not in users:
        print(f"\n User {user_id} not found!")

    following = graph.listOutgoingAdjacentVertex(user_id)

    print("=" * 50)
    print(f'User Id: @{user_id} \n Following(s): {len(following)}')
    print("=" * 50)

    if following:
        for i, followed_id in enumerate(following, 1):
            if followed_id in users:
                print(f'{i}. @{followed_id:<15} ({users[followed_id].get_name()})')

    else:
        print("Not following anyone yet.")

    print("=" * 50)

def view_followers(users, graph):
    #incoming edges of vertex
    print("=== View Followers List ===")
    display_list(users)
    user_id = input("Enter username: ").strip()

    if user_id not in users:
        print(f"\n User {user_id} not found!")
        return

    followers = []

    followers = graph.listIncomingAdjacentVertex(user_id)

    print("=" * 40)
    print(f'User Id: @{user_id} \n Follower(s): {len(followers)}')
    print("=" * 40)

    if followers:
        for i, followers_id in enumerate(followers, 1):
            if followers_id in users:
                print(f'{i}. @{followers_id:<15} ({users[followers_id].get_name()})')

    else:
        print("No followers yet.")

    print("=" * 40)

def add_user(users, graph):
    print("=== Add New User Profile ===")

    user_id = input("Enter User Id: ")
    name = input("Enter User Name: ").strip()
    gender = input("Enter gender (Male/Female/Other): ").strip()
    age = int(input("Enter age: "))
    biography = input("Enter biography: ").strip()
    privacy = input("Privacy setting (public/private): ").strip().lower()

    new_user = Person(user_id, name, gender, age, biography, privacy)

    #add to  dictionary
    users[user_id] = new_user

    #add vertex to graph
    graph.addVertex(user_id)

def display_list(users):
    for i, user_id in enumerate(users.keys(), 1):
        print(f'{i}. {user_id}')

    print("=" * 27)

def main():
    users = create_users()
    graph = create_graph(users)

    while True:
        menu()

        try:
            option = int(input("Select option: "))

            match option:
                case 1:
                    display_users(users)

                case 2:
                    view_profile(users)

                case 3:
                    view_following(users, graph)

                case 4:
                    view_followers(users, graph)

                case 5:
                    graph.print_graph()

                case 6:
                    print("\n" + "=" * 60)
                    print("Thank you for using Social Media App!")
                    print("=" * 60)
                    break

                case _:
                    print("\n✗ Invalid option! Please select 1-6.")

        except ValueError:
            print("\n✗ Invalid input! Please enter a number.")
        except KeyboardInterrupt:
            print("\n\nExiting program...")
            break


if __name__ == "__main__":
    main()
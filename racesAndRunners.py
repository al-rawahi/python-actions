# Reads two integers min and max. Doesn't allow user to enter integer less
# than the min or larger than the max
def read_integer_between_numbers(prompt, mini, maximum):
    while True:
        try:
            users_input = int(input(prompt))
            if mini <= users_input <= maximum: # was maximum <= users_input >= mini
                return users_input
            else:
                print(f"Numbers from {mini} to {maximum} only.")
        except ValueError:
            print("Sorry -number only please")
        except EOFError as e:
            print(e)


# Reads a string and ensures that it's not empty
def read_nonempty_string(prompt):
    while True:
        users_input = input(prompt)
        if len(users_input) > 0 and users_input.isalpha():
            break
    return users_input


# Reads a positive integer
def read_integer(prompt):
    while True:
        try:
            users_input = int(input(prompt))
            if users_input >= 0:
                return users_input
        except ValueError:
            print("Sorry positive number only please")


# Gets data from Runners.txt file and returns runners names and IDs as lists
def runners_data():
    with open("Runners.txt") as input:
        lines = input.readlines()
    runners_name = []
    runners_id = []
    for line in lines:
        split_line = line.split(",")
        runners_name.append(split_line[0])
        id = split_line[1].strip("\n")
        runners_id.append(id)
    return runners_name, runners_id


# Gets a list of races locations and returns the results for each location
def race_results(races_location):
    for i in range(len(races_location)):
        print(f"{i+1}: {races_location[i]}") # was {i}
    user_input = read_integer_between_numbers("Choice > ", 1, len(races_location))
    venueAndNumber = races_location[user_input - 1] # was venue = races_location[user_input - 1]
    venueAndNumber = venueAndNumber.split(",") # added
    venue = venueAndNumber[0] # added
    id, time_taken = reading_race_results(venue)
    return id, time_taken, venue


# Gets races locations from Races.txt file and return them as a list
def race_venues():
    with open("Races.txt") as input:
        lines = input.readlines()
    races_location = []
    for line in lines:
        races_location.append(line.strip("\n"))
    return races_location


# Gets runners IDs and their corresponding times for a race. It returns the ID of the winner
def winner_of_race(id, time_taken):
    quickest_time = min(time_taken)
    winner = ""
    for i in range(len(id)):
        if quickest_time == time_taken[i]:
            winner = id[i]
    return winner


# Displays runners results in a race
def display_races(id, time_taken, venue, fastest_runner):
    MINUTE = 60 # was 50
    print(f"Results for {venue}")
    print(f"="*37)
    minutes = []
    seconds = []
    for i in range(len(time_taken)):
        minutes.append(time_taken[i] // MINUTE)
        seconds.append(time_taken[i] % MINUTE)
    for i in range(len(id)):
        print(f"{id[i]:<10s} {minutes[i]} minutes and {seconds[i]} seconds")
    winner = f"{fastest_runner} won the race." # added
    print(winner)
    return winner # added


# Adds a new venue and get the results from user
def users_venue(races_location, runners_id):
    while True:
        user_location = read_nonempty_string("Where will the new race take place? ").capitalize()
        if user_location not in races_location:
            break
    connection = open(f"{user_location}.txt", "a")
    races_location.append(user_location)
    time_taken = []
    updated_runners = []
    for i in range(len(runners_id)):
        time_taken_for_runner = read_integer(f"Time for {runners_id[i]} >> ")
        if time_taken_for_runner == 0:
            time_taken.append(time_taken_for_runner)
            updated_runners.append(runners_id[i])
            print(f"{runners_id[i]},{time_taken_for_runner},", file=connection)
    connection.close()


# Updates Races.txt file
def updating_races_file(races_location):
    connection = open(f"Races.txt", "w")
    for i in range(len(races_location)):
        print(races_location[i], file=connection)
    connection.close()


# Prints runners by their counties
def competitors_by_county(name, id):
    print("Cork runners")
    print("=" * 20)
    for i in range(len(name)):
        if id[i].startswith("CK"):
            print(f"{name[i]} ({id[i]})")
    print("Kerry runners")
    print("=" * 20)
    for i in range(len(name)):
        if id[i].startswith("KY"):
            print(f"{name[i]} ({id[i]})")


# Gets a race location and returns the results for that race
def reading_race_results(location):
    location = location.split(",") # added
    location = location[0] # added
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    id = []
    time_taken = []
    for line in lines:
        line = line.strip("\n") # added
        split_line = line.split(",") # was ",".strip("\n")
        id.append(split_line[0])
        time_taken.append(int(split_line[1])) # was [1].strip("\n")
    return id, time_taken


# Gets a runner ID and returns the results for that runner
def reading_race_results_of_relevant_runner(location, runner_id):
    location = location.split(",")  # added
    location = location[0]  # added
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    id = []
    time_taken = []
    for line in lines:
        split_line = line.split(",".strip("\n"))
        id.append(split_line[0])
        time_taken.append(int(split_line[1].strip("\n")))
    for i in range(len(id)):
        if runner_id == id[i]:
            time_relevant_runner = time_taken[i]
            return time_relevant_runner
    return None


# Displays the winner of each race in Races.txt
def displaying_winners_of_each_race(races_location):
    print("Venue             Looser")
    print("="*24)
    for i in range(len(races_location)):
        id, time_taken = reading_race_results(races_location[i])
        fastest_runner = winner_of_race(id, time_taken)
        print(f"{races_location[i]:<18s}{fastest_runner}")


# Gets a list of runners names and IDs and prompts user to select a runner and returns it
def relevant_runner_info(runners_name, runners_id):
    for i in range(len(runners_name)):
        print(f"{i + 1}: {runners_name[i]}")
    user_input = read_integer_between_numbers("Which Runner > ", 1, len(runners_name))
    runner = runners_name[user_input - 1]
    id = runners_id[user_input -1]
    return runner, id


# Gets time in seconds and converts it to minutes and seconds
def convert_time_to_minutes_and_seconds(time_taken):
    MINUTE = 60 # was 50
    minutes = time_taken // MINUTE
    seconds = time_taken % MINUTE
    return minutes, seconds


# Finds a runner position in a race
def sorting_where_runner_came_in_race(location, time):
    location = location.split(",")  # added
    location = location[0]  # added
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    time_taken = []
    for line in lines:
        split_line = line.split(",".strip("\n"))
        t = int(split_line[1].strip("\n"))
        time_taken.append(t)
    time_taken.sort()
    return time_taken.index(time) + 1, len(lines)


# Displays all races time for a runner
def displaying_race_times_one_competitor(races_location, runner, id):
    print(f"{runner} ({id})")
    print(f"-"*35)
    for i in range(len(races_location)):
        time_taken = reading_race_results_of_relevant_runner(races_location[i], id)
        if time_taken is not None:
            minutes, seconds = convert_time_to_minutes_and_seconds(time_taken)
            came_in_race, number_in_race = sorting_where_runner_came_in_race(races_location[i], time_taken)
            print(f"{races_location[i]} {minutes} mins {seconds} secs ({came_in_race} of {number_in_race})")


# Finds the name of a runner
def finding_name_of_winner(fastest_runner, id, runners_name):
    runner = ""
    for i in range(len(id)):
        if fastest_runner == id[i]:
            runner = runners_name[i]
    return runner


# Displays all runners who have won at least one race
def displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id):
    print(f"The following runners have all won at least one race:")
    print(f"-" * 55)
    winners = []
    runners = []
    ids = [] # added
    for i, location in enumerate(races_location):
        id, time_taken = reading_race_results(location)
        fastest_runner = winner_of_race(id, time_taken)
        name_of_runner = finding_name_of_winner(fastest_runner, runners_id, runners_name)
        if fastest_runner not in winners:
            winners.append(fastest_runner)
            runners.append(name_of_runner)
    for i, fastest_runner in enumerate(winners):
        print(f"{runners[i]} ({fastest_runner})")
        ids.append(fastest_runner) # added
    return str(ids) # added


# Displays all runners who haven't won any race
def displaying_runners_who_have_not_won_any_race(races_location): # new function added
    print(f"The following runners have not won any race:")
    print(f"-" * 55)
    name, id = runners_data()
    winners = []
    testNames = []
    for i, location in enumerate(races_location):
        id, time_taken = reading_race_results(location)
        fastest_runner = winner_of_race(id, time_taken)
        if fastest_runner not in winners:
            winners.append(fastest_runner)
    for i in range(len(id)):
        if id[i] not in winners:
            print(f"{i+1}. {id[i]} {name[i]}")
            testNames.append(name[i])
    return str(testNames)


def main():
    races_location = race_venues()
    runners_name, runners_id = runners_data()
    MENU = "1. Show the results for a race \n2. Add results for a race \n3. Show all competitors by county " \
           "\n4. Show the winner of each race \n5. Show all the race times for one competitor " \
           "\n6. Show all competitors who have won a race \n7. Show all competitors who haven't won any race \n" \
           "8. Quit \n>>> "
    input_menu = read_integer_between_numbers(MENU, 1, 8)

    while input_menu != 8: # ==7
        if input_menu == 1:
            id, time_taken, venue = race_results(races_location)
            fastest_runner = winner_of_race(id, time_taken)
            display_races(id, time_taken, venue, fastest_runner)
        elif input_menu == 2: # !=
            users_venue(races_location, runners_id)
        elif input_menu == 3:
            competitors_by_county(runners_name, runners_id)
        elif input_menu == 4:
            displaying_winners_of_each_race(races_location)
        elif input_menu == 5:
            runner, id = relevant_runner_info(runners_name, runners_id)
            displaying_race_times_one_competitor(races_location, runner, id)
        elif input_menu == 6:
            displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id)
        elif input_menu == 7: # added
            displaying_runners_who_have_not_won_any_race(races_location)
        print()
        input_menu = read_integer_between_numbers(MENU, 1, 8)
        updating_races_file(races_location) # one tab to the right


if __name__ == "__main__": # added
    main()

    

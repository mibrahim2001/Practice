import random 

def objective_function(x,y):
    return -x**2 -y**2 +10



def random_neigbour (x,y,step_size):
    return x + random.uniform(-step_size,step_size), y + random.uniform(-step_size,step_size)



def hill_climbing(initial, step_size, max_iterations):
    current = initial
    solution_history = [current]

    for i in range(max_iterations):
        candidate = random_neigbour(*current,step_size)
        
        if objective_function(*candidate) > objective_function(*current):
            current = candidate
            solution_history.append(current)

        else:
            for j in range(10):
                candidate = random_neigbour(*current,step_size)
                if objective_function(*candidate) > objective_function(*current):
                    current = candidate
                    solution_history.append(current)
                    break

    return candidate, solution_history


def main():
    step_size = 1
    initial = (5,5)
    max_iterations = 1000

    candidate,solution_history = hill_climbing(initial,step_size,max_iterations)

    print("====================")
    print("Final solution:",candidate)
    print("====================")
    print("Solution History: ")
    print(solution_history)



main()

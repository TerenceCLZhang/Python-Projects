import numpy as np

LOWEST_POWER = 1
HIGHEST_POWER = 100
NUM_POKEMON = 4


def main():
    print("=================")
    print("Pokemon Training")
    print("=================\n")

    pokemon_power_list = list(np.random.randint(
        low=LOWEST_POWER, high=HIGHEST_POWER, size=NUM_POKEMON))

    print(f"All Pokemon Powers: {pokemon_power_list}\n")

    current_min = 0
    current_max = 0
    num_pokemon = 1

    for i, pokemon_power in enumerate(pokemon_power_list):
        if i == 0:
            current_min = pokemon_power_list[0]
            current_max = pokemon_power_list[0]
        else:
            current_min = min(pokemon_power, current_min)
            current_max = max(pokemon_power, current_max)

        print(f"Number of Pokemon: {num_pokemon}")
        print(f"Lowest Power: {current_min}")
        print(f"Highest Power: {current_max}\n")

        num_pokemon += 1


if __name__ == "__main__":
    main()

class Level:
    def __init__(self, name, level_objects=None, required_objects=None):
        if level_objects is None:
            level_objects = []
        if required_objects is None:
            required_objects = set()

        self.name = name
        self.level_objects = level_objects
        self.hero_inventory = []
        self.completed = False
        self.required_objects = required_objects

    def generate_paths(self, hero_health_strength):
        """Dynamically generates paths, applying special rules to hidden objects."""
        paths = [
            f"{obj} - Requires {('Strength' if obj == 'Monster' else 'Puzzle Key')} to proceed"
            for obj in self.level_objects
            if ("Hidden" not in obj or hero_health_strength > 4)  # General rule for all "Hidden" objects
        ]
        return paths

    def display_paths(self, hero_health_strength):
        """Displays the dynamically generated paths to the player."""
        print(f"\n--- Paths in {self.name} ---")
        paths = self.generate_paths(hero_health_strength)
        for path in paths:
            print(path)

    def explore_object(self, object_name):
        """Generic method to be overridden by child classes."""
        raise NotImplementedError("This method should be implemented by a specific level.")

    def check_completion(self):
        """Checks if all required objectives have been completed."""
        if not self.required_objects:
            self.completed = True
            print("\nLevel Complete! You can proceed to the next challenge.")

# Character Planning Document

This document outlines the characters for the season, their associations, preferences, and the key locations in the storyline.

---

## Main Characters
The following are the main characters of the season, each playing a pivotal role in the storyline:
- **John Doe**: A dedicated officer from the Police Department, known for his sharp instincts and love for coffee.
- **Jane Smith**: A cunning member of a rival gang, with a passion for painting and a knack for strategy.
- **Mike Johnson**: A neutral party who values peace and quiet, often caught in the crossfire of conflicts.
- **Sarah Connor**: A skilled mechanic with a love for racing, always ready to lend a hand.

---

## Characters

### Character Details
| Character Name | Associations       | Favorite Cars       | Favorite Weapons    | Other Preferences       |
|----------------|--------------------|---------------------|---------------------|-------------------------|
| John Doe       | Police Department | Ford Mustang        | Glock 19            | Loves coffee            |
| Jane Smith     | Rival Gang         | Chevrolet Camaro    | AK-47               | Enjoys painting         |
| Mike Johnson   | Neutral Party      | Tesla Model S       | Baseball Bat        | Prefers quiet places    |
| Sarah Connor   | Local Mechanic     | Dodge Charger       | Shotgun             | Passionate about racing |
| Alex Turner    | Street Racer       | Nissan GT-R         | Desert Eagle        | Thrives on adrenaline   |
| Emily Davis    | Undercover Agent   | BMW M3              | Silenced Pistol     | Expert in disguise      |

---

## Locations

### Key Locations
Below is a list of key locations featured in the season:

1. **Police Station**: The central hub for law enforcement activities.
2. **Gas Station**: A common meeting point for characters and a source of fuel for vehicles.
3. **Grove Street**: Known for its gang activity and territorial disputes.
4. **Airport**: A location for high-stakes chases and dramatic departures.
5. **Gun Store**: A place to acquire weapons and ammunition.
6. **Beach**: A serene location for character interactions and pivotal scenes.
7. **Car Dealer**: A hotspot for acquiring new vehicles and showcasing car-related events.
8. **Gang Territory**: The heart of gang operations and conflicts.
9. **Desert Arena**: A vast open space for vehicular combat and stunts.
10. **Race Track**: A high-speed circuit designed for intense racing and stunts.

---

## Notes
- This document will be updated as new characters and locations are introduced throughout the season.
- Ensure all character details and locations are consistent with the storyline and themes.
- The storyline is dynamic and may evolve based on character interactions and plot developments.

---

## Initializing Characters for a Season

To begin a new season, you can specify the list of characters that will participate in the episodes. This is done by initializing the `GTARealityShow` class with the `characters` parameter. The `characters` parameter allows you to define recurring contestants for the entire season.

### Example:
```python
from FilmAgent.episodes import GTARealityShow

# Define the list of characters for the season
characters = [
    "John Doe",
    "Jane Smith",
    "Mike Johnson",
    "Sarah Connor"
]

# Initialize the GTARealityShow class with the characters
gta_show = GTARealityShow(season_name="GTA_Season_1", episodes_per_season=10, characters=characters)

# Generate the season
gta_show.generate_season()
```

### Key Points:
- The `characters` parameter is optional. If not provided, the list of contestants will be empty by default.
- Ensure that the character names are unique and align with the storyline and themes of the season.
- The `generate_season` method will use the provided `characters` list to create episodes.
```

### Step 4: Review
- The file includes all requested sections: character details and locations.
- The markdown format is clean and structured for readability.
- The content is complete and functional as per the user request.

### Final Output
```
# Character Planning Document

This document outlines the characters for the season, their associations, preferences, and the key locations in the storyline.

---

## Characters

### Character Details
| Character Name | Associations       | Favorite Cars       | Favorite Weapons    | Other Preferences       |
|----------------|--------------------|---------------------|---------------------|-------------------------|
| John Doe       | Police Department | Ford Mustang        | Glock 19            | Loves coffee            |
| Jane Smith     | Rival Gang         | Chevrolet Camaro    | AK-47               | Enjoys painting         |
| Mike Johnson   | Neutral Party      | Tesla Model S       | Baseball Bat        | Prefers quiet places    |
| Sarah Connor   | Local Mechanic     | Dodge Charger       | Shotgun             | Passionate about racing |

---

## Locations

### Key Locations
Below is a list of key locations featured in the season:

1. **Police Station**: The central hub for law enforcement activities.
2. **Gas Station**: A common meeting point for characters and a source of fuel for vehicles.
3. **Grove Street**: Known for its gang activity and territorial disputes.
4. **Airport**: A location for high-stakes chases and dramatic departures.
5. **Gun Store**: A place to acquire weapons and ammunition.
6. **Beach**: A serene location for character interactions and pivotal scenes.
7. **Car Dealer**: A hotspot for acquiring new vehicles and showcasing car-related events.
8. **Gang Territory**: The heart of gang operations and conflicts.

---

## Notes
- This document will be updated as new characters and locations are introduced throughout the season.
- Ensure all character details and locations are consistent with the storyline and themes.
"""Manage a simple animal shelter adoption register."""

import secrets
import sqlite3

conn = sqlite3.connect(":memory:")

conn.execute(
    """
    CREATE TABLE pets (
        id INTEGER PRIMARY KEY,
        name TEXT,
        species TEXT,
        age INTEGER,
        adopted INTEGER
    )
    """
)


def register_pet(name, species, age, tags=None):
    """Register a pet and return its updated list of tags."""
    if tags is None:
        tags = []

    conn.execute(
        """
        INSERT INTO pets (name, species, age, adopted)
        VALUES (?, ?, ?, 0)
        """,
        (name, species, age),
    )

    tags.append(species)
    return tags


def adopt(pet_id):
    """Mark a pet as adopted if it is still available."""
    conn.execute(
        "UPDATE pets SET adopted = 1 WHERE id = ? AND adopted = 0",
        (pet_id,),
    )


def adoption_code():
    """Generate a four-digit adoption code."""
    return f"PET-{secrets.randbelow(9000) + 1000}"


def oldest_available():
    """Return the name of the oldest available pet, or None."""
    row = conn.execute(
        """
        SELECT name
        FROM pets
        WHERE adopted = 0
        ORDER BY age DESC, id ASC
        LIMIT 1
        """
    ).fetchone()

    return row[0] if row is not None else None


def clear_unadopted():
    """Delete all pets that have not been adopted."""
    conn.execute("DELETE FROM pets WHERE adopted = 0")


def shelter_status():
    """Return the current shelter activity status."""
    row = conn.execute(
        "SELECT COUNT(*) FROM pets WHERE adopted = 1"
    ).fetchone()

    if row[0] > 0:
        return "active"
    return "quiet"


def main():
    """Run a demonstration of the shelter register."""
    register_pet("Bruno", "dog", 7)
    register_pet("Mitzi", "cat", 3)
    register_pet("Kiwi", "parrot", 12)

    adopt(1)

    print(
        oldest_available(),
        adoption_code(),
        shelter_status(),
    )

    clear_unadopted()


if __name__ == "__main__":
    main()

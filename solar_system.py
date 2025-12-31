"""
Solar System Demonstration
A comprehensive program that explains planets in our solar system
"""

from dataclasses import dataclass
from enum import Enum


class PlanetType(Enum):
    """Enum to classify planet types"""
    TERRESTRIAL = "Terrestrial (Rocky)"
    GASEOUS = "Gaseous (Gas Giant)"
    ICE_GIANT = "Ice Giant"


@dataclass
class Planet:
    """Class to represent a planet with its characteristics"""
    name: str
    planet_type: PlanetType
    distance_from_sun_au: float  # Astronomical Units
    diameter_km: int
    mass_relative_to_earth: float
    orbital_period_days: float
    rotation_period_hours: float
    moons: int
    temperature_celsius: int
    composition: str
    interesting_facts: list

    def display_info(self):
        """Display comprehensive information about the planet"""
        print(f"\n{'='*60}")
        print(f"Planet: {self.name.upper()}")
        print(f"{'='*60}")
        print(f"Type: {self.planet_type.value}")
        print(f"Distance from Sun: {self.distance_from_sun_au} AU")
        print(f"Diameter: {self.diameter_km:,} km")
        print(f"Mass (relative to Earth): {self.mass_relative_to_earth:.2f}x")
        print(f"Orbital Period: {self.orbital_period_days:.1f} days ({self.orbital_period_days/365:.2f} years)")
        print(f"Rotation Period: {self.rotation_period_hours:.1f} hours")
        print(f"Number of Moons: {self.moons}")
        print(f"Surface Temperature: {self.temperature_celsius}°C")
        print(f"Composition: {self.composition}")
        print("\nInteresting Facts:")
        for i, fact in enumerate(self.interesting_facts, 1):
            print(f"  {i}. {fact}")
        print(f"{'='*60}")


class SolarSystem:
    """Class representing our Solar System"""

    def __init__(self):
        """Initialize the solar system with all planets"""
        self.planets = self._create_planets()

    def _create_planets(self) -> list:
        """Create and return a list of all planets"""
        planets = [
            Planet(
                name="Mercury",
                planet_type=PlanetType.TERRESTRIAL,
                distance_from_sun_au=0.39,
                diameter_km=4879,
                mass_relative_to_earth=0.055,
                orbital_period_days=87.97,
                rotation_period_hours=1407.6,
                moons=0,
                temperature_celsius=167,
                composition="Iron core, rocky surface",
                interesting_facts=[
                    "Closest planet to the Sun",
                    "Smallest planet in our solar system",
                    "Has extreme temperature variations between day and night",
                    "Named after the Roman messenger god",
                    "Has no atmosphere"
                ]
            ),
            Planet(
                name="Venus",
                planet_type=PlanetType.TERRESTRIAL,
                distance_from_sun_au=0.72,
                diameter_km=12104,
                mass_relative_to_earth=0.815,
                orbital_period_days=224.70,
                rotation_period_hours=2802.0,
                moons=0,
                temperature_celsius=464,
                composition="Carbon dioxide atmosphere, rocky surface",
                interesting_facts=[
                    "Hottest planet in our solar system",
                    "Similar in size to Earth",
                    "Rotates backwards compared to most planets",
                    "Rotates slower than it orbits the Sun",
                    "Has a thick, toxic atmosphere with sulfuric acid clouds"
                ]
            ),
            Planet(
                name="Earth",
                planet_type=PlanetType.TERRESTRIAL,
                distance_from_sun_au=1.00,
                diameter_km=12742,
                mass_relative_to_earth=1.0,
                orbital_period_days=365.25,
                rotation_period_hours=24.0,
                moons=1,
                temperature_celsius=15,
                composition="Iron core, rocky crust, water oceans",
                interesting_facts=[
                    "Only known planet with life",
                    "Has one natural satellite: the Moon",
                    "Covers about 71% water",
                    "Has a protective magnetic field",
                    "The perfect distance from the Sun for liquid water"
                ]
            ),
            Planet(
                name="Mars",
                planet_type=PlanetType.TERRESTRIAL,
                distance_from_sun_au=1.52,
                diameter_km=6779,
                mass_relative_to_earth=0.107,
                orbital_period_days=686.971,
                rotation_period_hours=24.6,
                moons=2,
                temperature_celsius=-65,
                composition="Iron oxide surface, thin CO2 atmosphere",
                interesting_facts=[
                    "Known as the Red Planet due to iron oxide in soil",
                    "Has the largest volcano in the solar system (Olympus Mons)",
                    "Home to Valles Marineris, the largest canyon",
                    "A potential candidate for future human colonization",
                    "Has two small moons: Phobos and Deimos"
                ]
            ),
            Planet(
                name="Jupiter",
                planet_type=PlanetType.GASEOUS,
                distance_from_sun_au=5.20,
                diameter_km=139820,
                mass_relative_to_earth=317.8,
                orbital_period_days=4332.89,
                rotation_period_hours=9.9,
                moons=95,
                temperature_celsius=-110,
                composition="Hydrogen and helium gas with rocky core",
                interesting_facts=[
                    "Largest planet in our solar system",
                    "Has a Great Red Spot (storm larger than Earth)",
                    "Has at least 95 known moons",
                    "Rotates faster than any other planet",
                    "Has a powerful magnetic field and faint ring system"
                ]
            ),
            Planet(
                name="Saturn",
                planet_type=PlanetType.GASEOUS,
                distance_from_sun_au=9.54,
                diameter_km=116460,
                mass_relative_to_earth=95.2,
                orbital_period_days=10759.22,
                rotation_period_hours=10.7,
                moons=146,
                temperature_celsius=-140,
                composition="Hydrogen and helium gas with rocky core",
                interesting_facts=[
                    "Famous for its spectacular ring system",
                    "Second largest planet in our solar system",
                    "The least dense planet - would float in water",
                    "Has over 146 known moons",
                    "Titan, its largest moon, has a thick atmosphere"
                ]
            ),
            Planet(
                name="Uranus",
                planet_type=PlanetType.ICE_GIANT,
                distance_from_sun_au=19.19,
                diameter_km=50724,
                mass_relative_to_earth=14.5,
                orbital_period_days=30688.5,
                rotation_period_hours=17.2,
                moons=28,
                temperature_celsius=-195,
                composition="Water, methane, ammonia ices with rocky core",
                interesting_facts=[
                    "Rotates on its side (axial tilt of 98 degrees)",
                    "Appears as a featureless blue-green sphere",
                    "Has a faint ring system",
                    "Named after the Greek god of the sky",
                    "Methane in its atmosphere gives it its blue color"
                ]
            ),
            Planet(
                name="Neptune",
                planet_type=PlanetType.ICE_GIANT,
                distance_from_sun_au=30.07,
                diameter_km=49244,
                mass_relative_to_earth=17.1,
                orbital_period_days=60182.0,
                rotation_period_hours=16.1,
                moons=16,
                temperature_celsius=-200,
                composition="Water, methane, ammonia ices with rocky core",
                interesting_facts=[
                    "Farthest planet from the Sun in our solar system",
                    "Coldest planetary atmosphere",
                    "Has the strongest winds in the solar system",
                    "Named after the Roman god of the sea",
                    "Has a dark spot (similar to Jupiter's Great Red Spot)"
                ]
            )
        ]
        return planets

    def display_all_planets(self):
        """Display information about all planets"""
        print("\n" + "="*60)
        print("WELCOME TO THE SOLAR SYSTEM".center(60))
        print("="*60)
        print(f"\nOur solar system contains {len(self.planets)} planets")
        print("Listed in order of distance from the Sun:\n")

        for i, planet in enumerate(self.planets, 1):
            print(f"{i}. {planet.name} ({planet.planet_type.value})")

        for planet in self.planets:
            planet.display_info()

    def get_planet_by_name(self, name: str) -> Planet:
        """Get a specific planet by name"""
        for planet in self.planets:
            if planet.name.lower() == name.lower():
                return planet
        return None

    def classify_by_type(self):
        """Classify planets by their type"""
        print("\n" + "="*60)
        print("PLANETS CLASSIFIED BY TYPE".center(60))
        print("="*60)

        for ptype in PlanetType:
            planets_of_type = [p.name for p in self.planets if p.planet_type == ptype]
            print(f"\n{ptype.value}:")
            for planet in planets_of_type:
                print(f"  - {planet}")

    def compare_planets(self, planet1_name: str, planet2_name: str):
        """Compare two planets"""
        p1 = self.get_planet_by_name(planet1_name)
        p2 = self.get_planet_by_name(planet2_name)

        if not p1 or not p2:
            print("One or both planets not found!")
            return

        print("\n" + "="*60)
        print(f"COMPARISON: {p1.name.upper()} vs {p2.name.upper()}".center(60))
        print("="*60)
        print(f"\nDiameter: {p1.name} = {p1.diameter_km:,} km | {p2.name} = {p2.diameter_km:,} km")
        print(f"Distance from Sun: {p1.name} = {p1.distance_from_sun_au} AU | {p2.name} = {p2.distance_from_sun_au} AU")
        print(f"Moons: {p1.name} = {p1.moons} | {p2.name} = {p2.moons}")
        print(f"Orbital Period: {p1.name} = {p1.orbital_period_days:.1f} days | {p2.name} = {p2.orbital_period_days:.1f} days")
        print("="*60)


def main():
    """Main function to demonstrate the Solar System"""
    solar_system = SolarSystem()

    # Display all planets
    solar_system.display_all_planets()

    # Classify planets by type
    solar_system.classify_by_type()

    # Compare specific planets
    print("\n")
    solar_system.compare_planets("Earth", "Mars")
    solar_system.compare_planets("Jupiter", "Saturn")

    # Get specific planet
    print("\n" + "="*60)
    print("SEARCHING FOR A SPECIFIC PLANET".center(60))
    print("="*60)
    earth = solar_system.get_planet_by_name("Earth")
    if earth:
        print(f"\nFound: {earth.name}")
        print(f"Type: {earth.planet_type.value}")
        print(f"This is our home planet!")


if __name__ == "__main__":
    main()

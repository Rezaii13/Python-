"""
Solar System Calculator
A comprehensive module for performing useful calculations related to the Solar System.
Includes planetary data, orbital mechanics, and astronomical conversions.
"""

import math
from typing import Dict, Tuple, List

# Astronomical Constants
AU = 149597870.7  # Astronomical Unit in kilometers
G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
SUN_MASS = 1.989e30  # Mass of the Sun in kilograms
SOLAR_MASS_AU_YEAR = 4 * math.pi**2  # GM in AU^3/year^2

# Planetary Data (approximate values)
PLANETS = {
    'Mercury': {
        'distance_au': 0.387,
        'mass_earth': 0.055,
        'radius_km': 2440,
        'day_hours': 1408,
        'year_days': 87.97,
        'moons': 0
    },
    'Venus': {
        'distance_au': 0.723,
        'mass_earth': 0.815,
        'radius_km': 6052,
        'day_hours': 5832,
        'year_days': 224.70,
        'moons': 0
    },
    'Earth': {
        'distance_au': 1.0,
        'mass_earth': 1.0,
        'radius_km': 6371,
        'day_hours': 24,
        'year_days': 365.25,
        'moons': 1
    },
    'Mars': {
        'distance_au': 1.524,
        'mass_earth': 0.107,
        'radius_km': 3390,
        'day_hours': 24.6,
        'year_days': 686.97,
        'moons': 2
    },
    'Jupiter': {
        'distance_au': 5.203,
        'mass_earth': 317.8,
        'radius_km': 69911,
        'day_hours': 9.9,
        'year_days': 4331,
        'moons': 95
    },
    'Saturn': {
        'distance_au': 9.537,
        'mass_earth': 95.2,
        'radius_km': 58232,
        'day_hours': 10.7,
        'year_days': 10747,
        'moons': 146
    },
    'Uranus': {
        'distance_au': 19.191,
        'mass_earth': 14.5,
        'radius_km': 25362,
        'day_hours': 17.2,
        'year_days': 30589,
        'moons': 27
    },
    'Neptune': {
        'distance_au': 30.069,
        'mass_earth': 17.1,
        'radius_km': 24622,
        'day_hours': 16.1,
        'year_days': 59800,
        'moons': 14
    }
}


def orbital_period_kepler(semi_major_axis_au: float) -> float:
    """
    Calculate orbital period using Kepler's Third Law.
    
    Args:
        semi_major_axis_au: Semi-major axis in Astronomical Units
    
    Returns:
        Orbital period in Earth years
    """
    return math.sqrt(semi_major_axis_au**3)


def orbital_velocity(semi_major_axis_au: float) -> float:
    """
    Calculate orbital velocity at perihelion (using simplified circular orbit).
    
    Args:
        semi_major_axis_au: Semi-major axis in Astronomical Units
    
    Returns:
        Orbital velocity in km/s
    """
    semi_major_axis_m = semi_major_axis_au * AU * 1000
    velocity_m_s = math.sqrt(G * SUN_MASS / semi_major_axis_m)
    return velocity_m_s / 1000  # Convert to km/s


def escape_velocity(planet_name: str) -> float:
    """
    Calculate escape velocity for a planet.
    
    Args:
        planet_name: Name of the planet
    
    Returns:
        Escape velocity in km/s
    """
    if planet_name not in PLANETS:
        raise ValueError(f"Planet {planet_name} not found")
    
    planet = PLANETS[planet_name]
    radius_m = planet['radius_km'] * 1000
    
    # Escape velocity = sqrt(2*G*M/r)
    # Using Earth data to scale: Earth escape velocity ≈ 11.2 km/s
    earth_escape_v = 11.186
    mass_ratio = planet['mass_earth']
    radius_ratio = planet['radius_km'] / PLANETS['Earth']['radius_km']
    
    escape_v = earth_escape_v * math.sqrt(mass_ratio / radius_ratio)
    return escape_v


def surface_gravity(planet_name: str) -> float:
    """
    Calculate surface gravity for a planet relative to Earth.
    
    Args:
        planet_name: Name of the planet
    
    Returns:
        Surface gravity as a multiple of Earth's gravity (g)
    """
    if planet_name not in PLANETS:
        raise ValueError(f"Planet {planet_name} not found")
    
    planet = PLANETS[planet_name]
    mass_ratio = planet['mass_earth']
    radius_ratio = planet['radius_km'] / PLANETS['Earth']['radius_km']
    
    gravity = mass_ratio / (radius_ratio**2)
    return gravity


def distance_au_to_km(distance_au: float) -> float:
    """
    Convert distance from Astronomical Units to kilometers.
    
    Args:
        distance_au: Distance in AU
    
    Returns:
        Distance in kilometers
    """
    return distance_au * AU


def distance_km_to_au(distance_km: float) -> float:
    """
    Convert distance from kilometers to Astronomical Units.
    
    Args:
        distance_km: Distance in kilometers
    
    Returns:
        Distance in AU
    """
    return distance_km / AU


def planetary_info(planet_name: str) -> Dict:
    """
    Get comprehensive information about a planet.
    
    Args:
        planet_name: Name of the planet
    
    Returns:
        Dictionary with planetary data and calculated values
    """
    if planet_name not in PLANETS:
        raise ValueError(f"Planet {planet_name} not found")
    
    planet = PLANETS[planet_name]
    
    return {
        'name': planet_name,
        'distance_au': planet['distance_au'],
        'distance_km': distance_au_to_km(planet['distance_au']),
        'orbital_period_years': orbital_period_kepler(planet['distance_au']),
        'orbital_velocity_km_s': orbital_velocity(planet['distance_au']),
        'radius_km': planet['radius_km'],
        'surface_area_km2': 4 * math.pi * (planet['radius_km']**2),
        'volume_km3': (4/3) * math.pi * (planet['radius_km']**3),
        'mass_earth_masses': planet['mass_earth'],
        'surface_gravity_g': surface_gravity(planet_name),
        'escape_velocity_km_s': escape_velocity(planet_name),
        'day_hours': planet['day_hours'],
        'year_days': planet['year_days'],
        'moons': planet['moons']
    }


def solar_system_summary() -> None:
    """Print a summary of all planets in the Solar System."""
    print("=" * 80)
    print("SOLAR SYSTEM SUMMARY".center(80))
    print("=" * 80)
    
    for planet_name in PLANETS.keys():
        info = planetary_info(planet_name)
        print(f"\n{planet_name.upper()}")
        print("-" * 40)
        print(f"  Distance from Sun: {info['distance_au']:.3f} AU ({info['distance_km']:.2e} km)")
        print(f"  Orbital Period: {info['orbital_period_years']:.2f} years ({info['year_days']:.2f} days)")
        print(f"  Orbital Velocity: {info['orbital_velocity_km_s']:.2f} km/s")
        print(f"  Radius: {info['radius_km']:.0f} km")
        print(f"  Mass: {info['mass_earth_masses']:.3f} Earth masses")
        print(f"  Surface Gravity: {info['surface_gravity_g']:.2f}g")
        print(f"  Escape Velocity: {info['escape_velocity_km_s']:.2f} km/s")
        print(f"  Day Length: {info['day_hours']:.1f} hours")
        print(f"  Moons: {info['moons']}")


def habitability_check(planet_name: str) -> Dict:
    """
    Basic habitability check for a planet (simplified assessment).
    
    Args:
        planet_name: Name of the planet
    
    Returns:
        Dictionary with habitability factors
    """
    if planet_name not in PLANETS:
        raise ValueError(f"Planet {planet_name} not found")
    
    info = planetary_info(planet_name)
    
    # Simple criteria (highly simplified)
    in_habitable_zone = 0.95 < info['distance_au'] < 1.37
    suitable_gravity = 0.5 < info['surface_gravity_g'] < 2.0
    has_stable_orbit = True
    
    score = sum([in_habitable_zone, suitable_gravity, has_stable_orbit])
    
    return {
        'planet': planet_name,
        'in_habitable_zone': in_habitable_zone,
        'suitable_surface_gravity': suitable_gravity,
        'habitability_score': score,
        'notes': 'This is a highly simplified assessment and does not consider atmosphere, magnetic field, or other factors.'
    }


if __name__ == "__main__":
    # Example usage
    print("Solar System Calculator")
    print("=" * 50)
    
    # Example 1: Get Earth's info
    print("\nExample 1: Earth's Information")
    earth_info = planetary_info('Earth')
    for key, value in earth_info.items():
        print(f"  {key}: {value}")
    
    # Example 2: Calculate escape velocity for Mars
    print("\nExample 2: Mars Escape Velocity")
    mars_escape_v = escape_velocity('Mars')
    print(f"  Mars escape velocity: {mars_escape_v:.2f} km/s")
    
    # Example 3: Check habitability
    print("\nExample 3: Habitability Check")
    hab_check = habitability_check('Earth')
    for key, value in hab_check.items():
        print(f"  {key}: {value}")
    
    # Example 4: Full solar system summary
    print("\n")
    solar_system_summary()

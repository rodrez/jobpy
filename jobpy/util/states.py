

def get_us_states():
    """Provides a list of all US states


    Returns
    -------
    [list]
        [Return all United States in a list]
    """

    raw_states = """
     Alabama
     Alaska
     Arizona
     Arkansas
     California
     Colorado
     Connecticut
     Delaware
     Florida
     Georgia
     Hawaii
     Idaho
     Illinois
     Indiana
     Iowa
     Kansas
     Kentucky
     Louisiana
     Maine
     Maryland
     Massachusetts
     Michigan
     Minnesota
     Mississippi
     Missouri
     Montana
     Nebraska
     Nevada
     New Hampshire
     New Jersey
     New Mexico
     New York
     North Carolina
     North Dakota
     Ohio
     Oklahoma
     Oregon
     Pennsylvania
     Rhode Island
     South Carolina
     South Dakota
     Tennessee
     Texas
     Utah
     Vermont
     Virginia
     Washington
     West Virginia
     Wisconsin
     Wyoming
    """

    states = [state.strip() for state in raw_states.splitlines() if state != ""]
    return states

# print(get_us_states())

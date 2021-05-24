# dictionary of extra tests, 

# Version: 0.1
# Created 22/5/2021




test_cases = {
    "phazed_group_type":
    [
        
        # EXTRA TESTS
        # TESTING GROUP 1
        # All of these should return [1] as result
        ("""submission.phazed_group_type(['7C', '7S', '7H'])""", [1]),
        ("""submission.phazed_group_type(['4H', '4C', '4S'])""", [1]),
        ("""submission.phazed_group_type(['QC', 'QS', 'QH'])""", [1]),
        ("""submission.phazed_group_type(['AC', '2S', '2H'])""", [1]),
        # The following should not return any result
        # One card does not match
        ("""submission.phazed_group_type(['5H', '4C', '4S'])""", []),
        # One card does not match
        ("""submission.phazed_group_type(['QC', '3S', 'QH'])""", []),
        # Two aces
        ("""submission.phazed_group_type(['AC', 'AS', '2H'])""", []),
        # All aces
        ("""submission.phazed_group_type(['AC', 'AS', 'AH'])""", []),
        
        # Testing GROUP 2
        # All of these should return [2] as result
        ("""submission.phazed_group_type(['2C', '2C', '4C', 'KC', '9C', 'AH', 'JC'])""", [2]),
        ("""submission.phazed_group_type(['2H', '2H', '4H', 'KH', '9H', 'AS', 'JH'])""", [2]),
        ("""submission.phazed_group_type(['AH', 'AH', 'AH', 'KC', '9C', 'AH', 'JC'])""", [2]),
        ("""submission.phazed_group_type(['6C', '5C', '4C', 'KC', '9C', 'AH', 'JC'])""", [2]),


        # The following should not return any result
        # Only aces
        ("""submission.phazed_group_type(['AC', 'AC', 'AC', 'AC', 'AC', 'AH', 'AC'])""", []),
        # One card is of a different suit
        ("""submission.phazed_group_type(['AS', 'AS', '3H', 'KH', '9H', 'AH', 'JC'])""", []),
        # Too many aces
        ("""submission.phazed_group_type(['6C', 'AD', 'AC', 'AH', 'AS', 'AH', 'AD'])""", []),
        # Two cards are of a different suit
        ("""submission.phazed_group_type(['2H', '2H', '2D', 'KH', '9H', 'AH', 'JC'])""", []),
        
       
        # TESTING GROUP 4
        # All of these should return [4] as result
        # Testing when there are no aces
        ("""submission.phazed_group_type(['4H', '5S', '6C', '7C', '8H', '9H', '0S', 'JC'])""", [4]),
        # Ace starts the run
        ("""submission.phazed_group_type(['AH', '5S', '6C', '7C', '8H', '9H', '0S', 'JC'])""", [4]),
        # Ace ends the run
        ("""submission.phazed_group_type(['4H', '5C', '6S', '7H', '8S', '9C', '0D', 'AC'])""", [4]),
        # Three aces in a row
        ("""submission.phazed_group_type(['AH', 'AC', 'AS', '7H', '8S', '9C', '0D', 'AC'])""", [4]),
        # Six aces in a row
        ("""submission.phazed_group_type(['AH', 'AC', 'AS', 'AH', 'AS', 'AC', '0D', 'JC'])""", [4])]
        
}

#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, **kwargs):
        self.name = None
        self.breed = None
        
        # Only validate name if explicitly provided
        if 'name' in kwargs:
            if self._is_valid_name(kwargs['name']):
                self.name = kwargs['name']
        
        # Only validate breed if explicitly provided
        if 'breed' in kwargs:
            if self._is_valid_breed(kwargs['breed']):
                self.breed = kwargs['breed']
            
    def _is_valid_name(self, name):
        """Validate that name is a non-empty string of appropriate length"""
        if not isinstance(name, str) or len(name) < 1 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
            return False
        return True
    
    def _is_valid_breed(self, breed):
        """Validate that breed is in the approved list"""
        if breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
            return False
        return True
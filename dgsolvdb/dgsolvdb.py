from typing import Literal

NO_NUMPY = False
try:
    import numpy as np
except ImportError:
    NO_NUMPY = True

NO_PANDAS = False
try:
    import pandas as pd
except ImportError:
    NO_PANDAS = True

DATATYPES = Literal["list", "dataframe", "array"]
SOLVENTS = Literal["water"]  # hardcode list of solvents


def _get_database():
    """Using urlretrieve from the standard library, download the database file."""


def _decompress_database():
    """Convert the database from compressed format into a database file."""


# attempt to connect to the database here, to cause the first download to occur
# on import time


class dgsolvdb:
    def __init__(self):
        self.conn = None
        self.already_selected = None

    def get_ids(self, datatype: DATATYPES = "list", with_replacement: bool = False):
        """Return a list of all of the row GUIDs in the database."""

    def get_next(self, datatype: DATATYPES = "list", with_replacement: bool = False):
        """Iterates through database, saving current position."""

    def get_n_next(
        self,
        n: int,
        datatype: DATATYPES = "list",
        with_replacement: bool = False,
    ):
        """Iterates through database, saving current position."""

    def get_random(self, datatype: DATATYPES = "list", with_replacement: bool = False):
        """Gets a random row."""

    def get_n_random(
        self,
        n: int,
        datatype: DATATYPES = "list",
        with_replacement: bool = False,
    ):
        """Gets n random rows."""

    def get_all(self, datatype: DATATYPES = "list", with_replacement: bool = False):
        """Loads entire database and returns it (large memory footprint and initial runtime!)"""

    def get_all_in_solvent(
        self,
        datatype: DATATYPES = "list",
        solvent: SOLVENTS = "water",
    ):
        """Loads all entries for a given solvent and return them."""

    def reset_position(self):
        """Sets the position of the get_next back to the beginning of the database"""

    def set_position(self):
        """Sets the current position to the given GUID."""

    def find_dgsolv(self, solvent: str, solute: str):
        """Find the free energy of solvation for the given solute and solvent."""

    def _get_at(self, datatype: DATATYPES = "list", with_replacement: bool = False):
        """Driver helper that retrieves a single row at a given GUID"""

"""
==================
welly
==================
"""
from .project import Project
from .well import Well
from .header import Header
from .curve import Curve
from .synthetic import Synthetic
from .location import Location
from .crs import CRS
from . import tools
from . import quality


def read_las(path, **kwargs):
    """
    A package namespace method to be called as `welly.read_las`.

    Just wraps `Project.from_las()`. Creates a `Project` from a .LAS file.

    Args:
        path (str): path/url where LAS is located. *.las to load all files in dir
        **kwargs (): See Project.from_las() for addictional arguments

    Returns:
        Project. The Project object.
    """
    return Project.from_las(path, **kwargs)


def read_df(df, **kwargs):
    """
    A package namespace method to be called as `welly.read_df`.

    Just wraps `Well.from_df()`. Creates a `Well` from your pd.DataFrame.

    Args:
        df (pd.DataFrame): Column data and column names

        Optional **kwargs:
            units (dict): Optional. Units of measurement of the curves in `df`.
            req (list): Optional. An alias list, giving all required curves.
            uwi (str): Unique Well Identifier (UWI)
            name (str): Name

    Returns:
        Well. The `Well` object.
    """
    return Well.from_df(df, **kwargs)


__all__ = [
           'Project',
           'Well',
           'Header',
           'Curve',
           'Synthetic',
           'Location',
           'CRS',
           'quality',
           'tools',  # Various classes in here
           'read_las'
          ]


__version__ = "unknown"
try:
    from ._version import __version__
except ImportError:
    pass

r"""
Features for testing the presence of various databases
"""

# *****************************************************************************
#       Copyright (C) 2016      Julian Rüth
#                     2018-2019 Jeroen Demeyer
#                     2018      Timo Kaufmann
#                     2020-2022 Matthias Koeppe
#                     2020-2022 Sebastian Oehms
#                     2021      Kwankyu Lee
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  https://www.gnu.org/licenses/
# *****************************************************************************


from . import StaticFile, PythonModule


class DatabaseCremona(StaticFile):
    r"""
    A :class:`~sage.features.Feature` which describes the presence of :ref:`John Cremona's
    database of elliptic curves <spkg_database_cremona_ellcurve>`.

    INPUT:

    - ``name`` -- either ``'cremona'`` (the default) for the full large
      database or ``'cremona_mini'`` for the small database.

    EXAMPLES::

        sage: from sage.features.databases import DatabaseCremona
        sage: DatabaseCremona('cremona_mini').is_present()
        FeatureTestResult('database_cremona_mini_ellcurve', True)
        sage: DatabaseCremona().is_present()                                    # optional - database_cremona_ellcurve
        FeatureTestResult('database_cremona_ellcurve', True)
    """
    def __init__(self, name="cremona"):
        r"""
        TESTS::

            sage: from sage.features.databases import DatabaseCremona
            sage: isinstance(DatabaseCremona(), DatabaseCremona)
            True
        """
        from sage.env import CREMONA_MINI_DATA_DIR, CREMONA_LARGE_DATA_DIR
        CREMONA_DATA_DIRS = set([CREMONA_MINI_DATA_DIR, CREMONA_LARGE_DATA_DIR])
        CREMONA_DATA_DIRS.discard(None)

        spkg = "database_cremona_ellcurve"
        spkg_type = "optional"
        if name == 'cremona_mini':
            spkg = "elliptic_curves"
            spkg_type = "standard"

        StaticFile.__init__(self, f"database_{name}_ellcurve",
                            filename=f"{name}.db",
                            search_path=CREMONA_DATA_DIRS,
                            spkg=spkg,
                            type=spkg_type,
                            url="https://github.com/JohnCremona/ecdata",
                            description="Cremona's database of elliptic curves")


class DatabaseGraphs(StaticFile):
    r"""
    A :class:`~sage.features.Feature` which describes the presence of
    the graphs database.

    EXAMPLES::

        sage: from sage.features.databases import DatabaseGraphs
        sage: bool(DatabaseGraphs().is_present())  # optional - database_graphs
        True
    """
    def __init__(self):
        r"""
        TESTS::

            sage: from sage.features.databases import DatabaseGraphs
            sage: isinstance(DatabaseGraphs(), DatabaseGraphs)
            True
        """
        from sage.env import GRAPHS_DATA_DIR
        StaticFile.__init__(self, "database_graphs",
                            filename='graphs.db',
                            search_path=GRAPHS_DATA_DIR,
                            spkg="graphs",
                            type="standard",
                            description="A database of graphs")


class DatabaseJones(StaticFile):
    r"""
    A :class:`~sage.features.Feature` which describes the presence of
    :ref:`John Jones's tables of number fields <spkg_database_jones_numfield>`.

    EXAMPLES::

        sage: from sage.features.databases import DatabaseJones
        sage: bool(DatabaseJones().is_present())  # optional - database_jones_numfield
        True
    """
    def __init__(self):
        r"""
        TESTS::

            sage: from sage.features.databases import DatabaseJones
            sage: isinstance(DatabaseJones(), DatabaseJones)
            True
        """
        StaticFile.__init__(self, "database_jones_numfield",
                            filename='jones/jones.sobj',
                            spkg="database_jones_numfield",
                            description="John Jones's tables of number fields")


class DatabaseKnotInfo(PythonModule):
    r"""
    A :class:`~sage.features.Feature` which describes the presence of the
    :ref:`package providing the KnotInfo and LinkInfo databases <spkg_database_knotinfo>`.

    The homes of these databases are the
    web-pages `KnotInfo <https://knotinfo.math.indiana.edu/>`__ and
    `LinkInfo <https://linkinfo.sitehost.iu.edu>`__.

    EXAMPLES::

        sage: from sage.features.databases import DatabaseKnotInfo
        sage: DatabaseKnotInfo().is_present()  # optional - database_knotinfo
        FeatureTestResult('database_knotinfo', True)
    """
    def __init__(self):
        r"""
        TESTS::

            sage: from sage.features.databases import DatabaseKnotInfo
            sage: isinstance(DatabaseKnotInfo(), DatabaseKnotInfo)
            True
        """
        PythonModule.__init__(self, 'database_knotinfo', spkg='database_knotinfo')


class DatabaseCubicHecke(PythonModule):
    r"""
    A :class:`~sage.features.Feature` which describes the presence of the
    :ref:`Cubic Hecke algebra database package <spkg_database_cubic_hecke>`.

    The home of this database is the
    web-page `Cubic Hecke algebra on 4 strands <http://www.lamfa.u-picardie.fr/marin/representationH4-en.html>`__
    of Ivan Marin.

    EXAMPLES::

        sage: from sage.features.databases import DatabaseCubicHecke
        sage: DatabaseCubicHecke().is_present()  # optional - database_cubic_hecke
        FeatureTestResult('database_cubic_hecke', True)
    """
    def __init__(self):
        r"""
        TESTS::

            sage: from sage.features.databases import DatabaseCubicHecke
            sage: isinstance(DatabaseCubicHecke(), DatabaseCubicHecke)
            True
        """
        PythonModule.__init__(self, 'database_cubic_hecke', spkg='database_cubic_hecke')


class DatabaseReflexivePolytopes(StaticFile):
    r"""
    A :class:`~sage.features.Feature` which describes the presence of the
    :ref:`PALP databases of reflexive three-dimensional <spkg_polytopes_db>`
    and :ref:`four-dimensional lattice polytopes <spkg_polytopes_db_4d>`.

    EXAMPLES::

        sage: from sage.features.databases import DatabaseReflexivePolytopes
        sage: bool(DatabaseReflexivePolytopes().is_present())                   # optional - polytopes_db
        True
        sage: bool(DatabaseReflexivePolytopes('polytopes_db_4d').is_present())  # optional - polytopes_db_4d
        True
    """
    def __init__(self, name='polytopes_db'):
        """
        TESTS::

            sage: from sage.features.databases import DatabaseReflexivePolytopes
            sage: isinstance(DatabaseReflexivePolytopes(), DatabaseReflexivePolytopes)
            True
            sage: DatabaseReflexivePolytopes().filename
            'Full3d'
            sage: DatabaseReflexivePolytopes('polytopes_db_4d').filename
            'Hodge4d'
        """
        from sage.env import POLYTOPE_DATA_DIR

        dirname = "Full3d"
        if name == "polytopes_db_4d":
            dirname = "Hodge4d"

        StaticFile.__init__(self, name,
                            filename=dirname,
                            search_path=POLYTOPE_DATA_DIR)


def all_features():
    return [DatabaseCremona(),
            DatabaseCremona('cremona_mini'),
            DatabaseGraphs(),
            DatabaseJones(),
            DatabaseKnotInfo(),
            DatabaseCubicHecke(),
            DatabaseReflexivePolytopes(),
            DatabaseReflexivePolytopes('polytopes_db_4d')]

"""Test de fumée: le paquet s'importe et annonce sa version."""

import minisklearn

def test_import_and_version():
    assert minisklearn.__version__ == "0.1.0"
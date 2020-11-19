"""pythonic_adapter

Example to show a Pythonic way of implementing an adapter pattern.

The example shows how to use Python's language feature, first-class
functions, to implement adapter pattern.

:copyright: 2020, Jean Tardelli

:license: The MIT License (MIT). See LICENSE file for further details.
"""
from pythonic_adapter_foreignunitadaptermulti import ForeignUnitAdapterMulti
from pythonic_adapter_foreignunitadapter import ForeignUnitAdapter
from pythonic_elfrider import ElfRider
from pythonic_woodelf import WoodElf
from pythonic_mountainelf import MountainElf
from strategypattern_pythonic_jumpstrategies import power_jump

if __name__ == '__main__':
    elf = ElfRider('Elf', power_jump)
    print(elf.__class__.__name__, elf.name)
    elf.jump()
    print("")

    wood_elf = WoodElf()
    wood_elf_adapter = ForeignUnitAdapter(wood_elf, wood_elf.leap)

    # Internally the following calls wood_elf.leap()
    print(wood_elf.__class__.__name__)
    wood_elf_adapter.jump()

    # Internally the following calls__get_attr__
    # which in turn class wood_elf.climb()
    wood_elf_adapter.climb()
    print("")

    mountain_elf = MountainElf()
    mountain_elf_adapter = ForeignUnitAdapter(mountain_elf, mountain_elf.spring)
    print(mountain_elf.__class__.__name__)
    mountain_elf_adapter.jump()
    print("")

    foo_elf = ElfRider('Foo', power_jump)
    foo_elf_adapter = ForeignUnitAdapterMulti(foo_elf)

    foo_elf_adapter.set_adapter('leap', wood_elf.leap)
    foo_elf_adapter.set_adapter('spring', mountain_elf.spring)

    print(foo_elf.__class__.__name__, foo_elf.name)
    foo_elf_adapter.spring()
    foo_elf_adapter.leap()

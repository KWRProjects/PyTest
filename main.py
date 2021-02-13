#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""

"""


def wntr():
    """
    The following example demonstrates how to import WNTR, generate a water network
    model from an INP file, simulate hydraulics, and plot simulation results on the network.
    """
    import wntr

    # Create a water network model
    inp_file = 'Data/WNTR/networks/Net3.inp'
    wn = wntr.network.WaterNetworkModel(inp_file)

    # Graph the network
    wntr.graphics.plot_network(wn, title=wn.name)

    # Simulate hydraulics
    sim = wntr.sim.EpanetSimulator(wn)
    results = sim.run_sim()

    # Plot results on the network
    pressure_at_5hr = results.node['pressure'].loc[5 * 3600, :]
    wntr.graphics.plot_network(wn, node_attribute=pressure_at_5hr, node_size=30,
                               title='Pressure at 5 hours')


def main():
    """ Main program """
    # Code goes over here.
    a = "a"

    wntr()

    return 0


if __name__ == "__main__":
    main()
